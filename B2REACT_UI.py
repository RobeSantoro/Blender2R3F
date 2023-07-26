import bpy


class B2REACT_PT_Init_Panel(bpy.types.Panel):
    """Blender2React Initialization Panel"""

    bl_idname = "B2REACT_PT_Init_Panel"
    bl_label = "Initialization"

    bl_description = "Initialization"
    bl_category = "blender2react"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        # NOT INITIALIZED - INIT
        if not bpy.context.scene.Blender2React.R3F_Initialized:
            col1 = layout.column(align=True, heading="Project_Root")
            col1.prop(context.scene.Blender2React, "R3F_Project_Root", text="")

            col2 = layout.column(align=True, heading="Project_Name")
            col2.prop(context.scene.Blender2React, "R3F_Project_Name", text="")

            row_init = layout.row(align=True)
            row_init.scale_y = 1.2 if context.scene.Blender2React.R3F_Initialized else 2
            row_init.operator("Blender2React.create_r3f_project",
                              text="Create R3F Project" if not context.scene.Blender2React.R3F_Initialized else "Project Created")
            row_init.enabled = not context.scene.Blender2React.R3F_Initialized

        # INITIALIZED - UPDATE TITLE
        else:
            col3 = layout.column(align=False)
            col3.label(text="Project_Title")

            row1 = layout.row(align=True)
            row1.prop(context.scene.Blender2React, "R3F_Project_Title", text="")
            row1.operator("blender2react.update_title", text="", icon='FILE_REFRESH')

        # START DEV SERVER OPERATOR
        row_dev = layout.row(align=False)
        row_dev.operator("Blender2React.start_dev_server")
        row_dev.scale_y = 1.5 if context.scene.Blender2React.R3F_Initialized else 1

        # OPEN IN VS CODE AND OPEN IN EXPLORER OPERATORS
        row_open = layout.row(align=False)
        row_open.operator("Blender2React.open_project_in_vscode")
        row_open.operator("Blender2React.open_project_folder")
        row_open.enabled = context.scene.Blender2React.R3F_Initialized

        # GIT INIT and # RESET OPERATOR
        row_reset = layout.row(align=False)
        row_reset.operator("Blender2React.reset_git")
        row_reset.enabled = context.scene.Blender2React.R3F_Initialized
        row_reset.operator("Blender2React.delete_r3f_project", text="Delete Project")
        row_reset.enabled = context.scene.Blender2React.R3F_Initialized


class B2REACT_PT_Utils_Panel(bpy.types.Panel):
    """Blender2React Utils Panel"""

    bl_idname = "B2REACT_PT_Utils_Panel"
    bl_label = "Utils"

    bl_description = "Blender2React Utils Panel"
    bl_category = "blender2react"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        col1 = layout.column(align=True)
        # col1.label(text="Push Down Actions", icon='ACTION')
        col1.operator("Blender2React.pushdown_actions", text="Push Down Selected", icon='ACTION')

        col2 = layout.column(align=True)
        # col1.label(text="Push Down Actions", icon='ACTION')
        col2.operator("Blender2React.rename_tracks", text="Rename Tracks ", icon='ACTION_TWEAK')

        col3 = layout.column(align=True)
        # col1.label(text="Rename Geometry", icon='MESH_DATA')
        col3.operator("Blender2React.rename_geo", text="Rename Geometry", icon='MESH_DATA')


class B2REACT_PT_Export_Panel(bpy.types.Panel):
    """Blender2React Export Panel"""

    bl_idname = "B2REACT_PT_Export_Panel"
    bl_label = "Export"

    bl_description = "Blender2React Export Panel"
    bl_category = "blender2react"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        col3 = layout.column(align=True, heading="R3F_Export_Path")
        col3.prop(context.scene.Blender2React, "R3F_Export_Path", text="")

        col1 = layout.column(align=True, heading="")
        col1.prop(context.scene.Blender2React, "R3F_Keep_Original_GLB", text="Keep Original GLB")
        col1.prop(context.scene.Blender2React, "R3F_Create_JSX_Component", text="Create JSX Component")

        row1 = layout.row(align=True)
        row1.operator("Blender2React.exportall_glb", text="Export All Collections")

        row2 = layout.row(align=True)
        row2.operator("Blender2React.exportselected_glb", text="Export Active Collection")
