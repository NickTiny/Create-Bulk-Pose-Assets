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
    "name" : "Poselib Quick Actions",
    "author" : "Nick Alberelli",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}


import bpy

bpy.types.Scene.target = bpy.props.PointerProperty(type=bpy.types.Object)

classes = []

class PoseActionOperator(bpy.types.Operator):   
    """Run Pose Action1"""
    bl_idname = "view3d.pose_actions"
    bl_label = "Run Pose Action1"

    def execute(self, context):
        sce = bpy.context.scene
        ob = bpy.context.object
        action_name = (ob.animation_data.action.name)
        
        if ob is not None:
            if ob.animation_data is not None and ob.animation_data.action is not None:
                action = ob.animation_data.action
                print()
                print("Keyframes")
                
                for fcu in action.fcurves:
                    print(fcu)
                   



        return {"FINISHED"}

classes.append(PoseActionOperator)

class PoseActionPanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_pose_actions_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "poseaction1"
    bl_label = "poseactions"

    def draw(self, context):
        self.layout.operator("view3d.pose_actions")
            
classes.append(PoseActionPanel)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)    
        