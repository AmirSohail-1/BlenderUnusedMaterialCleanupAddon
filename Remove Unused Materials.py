bl_info = {
    "name": "Scene Material Cleanup Tool",
    "blender": (3, 6, 0),
    "category": "Object Materials",
    "author": "Amir",
}

import bpy

class RemoveUnusedMaterialsOperator(bpy.types.Operator):
    """Remove Unused Materials from the Scene"""
    bl_idname = "object.remove_unused_materials"
    bl_label = "Remove Unused Materials"
    bl_options = {'REGISTER'}

    def execute(self, context):
        # Identify and remove unused materials
        unused_materials = [mat for mat in bpy.data.materials if not mat.users]
        
        for mat in unused_materials:
            bpy.data.materials.remove(mat)

        self.report({'INFO'}, f"Removed {len(unused_materials)} unused materials.")
        return {'FINISHED'}


class RemoveUnusedTexturesOperator(bpy.types.Operator):
    """Remove Unused Textures from the Scene"""
    bl_idname = "object.remove_unused_textures"
    bl_label = "Remove Unused Textures"
    bl_options = {'REGISTER'}

    def execute(self, context):
        # Identify and remove unused textures
        unused_textures = [tex for tex in bpy.data.images if not tex.users]
        
        for tex in unused_textures:
            bpy.data.images.remove(tex)

        self.report({'INFO'}, f"Removed {len(unused_textures)} unused textures.")
        return {'FINISHED'}


class SceneCleanupPanel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport sidebar"""
    bl_label = "Scene Material Cleanup Tool"
    bl_idname = "VIEW3D_PT_scene_cleanup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Cleanup"

    def draw(self, context):
        layout = self.layout
        layout.operator(RemoveUnusedMaterialsOperator.bl_idname, text="Remove Unused Materials")
        layout.operator(RemoveUnusedTexturesOperator.bl_idname, text="Remove Unused Textures")

def register():
    bpy.utils.register_class(RemoveUnusedMaterialsOperator)
    bpy.utils.register_class(RemoveUnusedTexturesOperator)
    bpy.utils.register_class(SceneCleanupPanel)

def unregister():
    bpy.utils.unregister_class(SceneCleanupPanel)
    bpy.utils.unregister_class(RemoveUnusedTexturesOperator)
    bpy.utils.unregister_class(RemoveUnusedMaterialsOperator)

if __name__ == "__main__":
    register()
