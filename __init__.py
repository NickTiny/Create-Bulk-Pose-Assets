# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Create Bulk Pose Assets",
    "author": "Nick Alberelli",
    "description": "Allows for the bulk creation of Pose Library Assets, from the action editor.",
    "blender": (3, 2, 0),
    "version": (0, 0, 1),
    "location": "Dopesheet Editor > Sidebar > Pose Library > Create Bulk Pose Assets",
    "warning": "This addon is in an alpha state",
    "category": "Animation",
}


from cgitb import text
from sys import _current_frames
import bpy
import math


bpy.types.Scene.target = bpy.props.PointerProperty(type=bpy.types.Object)

classes = []


class QueryProps(bpy.types.PropertyGroup):

    query: bpy.props.StringProperty(default="testtest")


classes.append(QueryProps)


class PoseActionOperator(bpy.types.Operator):
    """Create Pose Assets from selected frames on active bones. Naming convention is Prefix+Frame#."""

    bl_idname = "view3d.pose_actions"
    bl_label = "Create Bulk Pose Assets"
    usertext: bpy.props.StringProperty(name="Prefix")

    def execute(self, context):
        ob = bpy.context.object
        sc = bpy.context.scene
        action_name = ob.animation_data.action.name

        # get keyframes of object list
        def get_keyframes(obj_list):
            keyframes = []
            for obj in obj_list:
                anim = obj.animation_data
                if anim is not None and anim.action is not None:
                    for fcu in anim.action.fcurves:
                        for keyframe in fcu.keyframe_points:
                            x, y = keyframe.co
                            if x not in keyframes:
                                keyframes.append((math.ceil(x)))
            return keyframes

        # get all selected objects
        selection = bpy.context.selected_objects

        # check if selection is not empty
        if selection:

            # get all frames with assigned keyframes
            keys = get_keyframes(selection)

            # print all keyframes
            print(keys)

            # print first and last keyframe
            print("{} {}".format("first keyframe:", keys[0]))
            print("{} {}".format("last keyframe:", keys[-1]))

        else:
            print("nothing selected")

        # Execute adding to pose lib

        for key in keys:
            usertext = bpy.data.scenes["Scene"].QueryProps.query
            bpy.context.scene.frame_set(key)
            bpy.ops.poselib.create_pose_asset(activate_new_action=True)
            bpy.context.object.animation_data.action.name = usertext + " - " + str(key)
            bpy.ops.poselib.restore_previous_action()
        return {"FINISHED"}


classes.append(PoseActionOperator)


class PoseActionPanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_pose_actions_panel"
    bl_space_type = "DOPESHEET_EDITOR"
    bl_region_type = "UI"
    bl_label = "Create Bulk Pose Assets"
    bl_category = "Pose Library"

    def draw(self, context):
        if bpy.context.mode == "POSE":
            # self.layout.prop(strings)
            props = bpy.context.scene.QueryProps
            layout = self.layout
            col = layout.column(align=True)
            rowsub = col.row(align=True)
            rowsub.label(text="Prefix:")
            rowsub = col.row(align=True)
            col2 = layout.column()
            rowsub2 = col2.row()
            rowsub2.operator("view3d.pose_actions")
            rowsub.prop(props, "query", text="")


classes.append(PoseActionPanel)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # Register QueryProps
    bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type=QueryProps)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    # $ delete QueryProps on unregister
    del bpy.types.Scene.QueryProps
