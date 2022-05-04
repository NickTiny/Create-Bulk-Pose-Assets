# Create Bulk Pose Assets
**Warning this addon is in an alpha state.**

**Compatability**
- Blender Version: 3.2.0 Beta, branch: master, commit date: 2022-05-02 20:13, hash: `rB62ef1c08af9a` 

# **Usage**

Using **Create Bulk Pose Assets** is very similar to Vanilla Blender's **Create Pose Asset**. The difference is that **Create Bulk Pose Assets** will automatically create new Pose Assets using the "prefix" and current frame number. It uses the frames in the current action to generate the assets. 

1. Select an armature
2. Switch to Pose Mode
3. Open the Drop Sheet, Navitgate to the Pose Library Panel on the Right
4. Find the "**Create Bulk Assets** menu
5. Select the bone(s) in the 3D Viewport. (_Error will occur if no bone is selected!_)
6. Enter a prefix in the text field. The naming convention is PREFIX + Frame Number
7. Hit the **Create Bulk Pose Assets** to generate new assets

Note: There is currently no way to bulk edit assets, or bulk remove assets. Backup your files before usage. Use the Blend File view to remove multiple actions at once.

![demo](https://user-images.githubusercontent.com/86638335/166613734-46a0db33-e06e-4826-8d51-bcd63471e7b5.gif)
