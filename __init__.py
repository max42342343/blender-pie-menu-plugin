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
    "name" : "mode selector",
    "author" : "max", 
    "description" : "",
    "blender" : (4, 2, 0),
    "version" : (0, 1, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
prefrences = {'sna_new_variable': False, }
class SNA_OT_Vertex_Mode__68Ea5(bpy.types.Operator):
    bl_idname = "sna.vertex_mode__68ea5"
    bl_label = "vertex mode "
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if 'EDIT_MESH'==bpy.context.mode:
            if bpy.context.tool_settings.mesh_select_mode[0]:
                bpy.ops.object.editmode_toggle()
            else:
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Edge_Mode_D3C76(bpy.types.Operator):
    bl_idname = "sna.edge_mode_d3c76"
    bl_label = "edge mode"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if 'EDIT_MESH'==bpy.context.mode:
            if bpy.context.tool_settings.mesh_select_mode[1]:
                bpy.ops.object.editmode_toggle()
            else:
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Face_Mode__455F3(bpy.types.Operator):
    bl_idname = "sna.face_mode__455f3"
    bl_label = "face mode "
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if 'EDIT_MESH'==bpy.context.mode:
            if bpy.context.tool_settings.mesh_select_mode[2]:
                bpy.ops.object.editmode_toggle()
            else:
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_MT_88FD1(bpy.types.Menu):
    bl_idname = "SNA_MT_88FD1"
    bl_label = "Modes"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.menu_pie()
        op = layout.operator('sna.vertex_mode__68ea5', text='Vertex Mode ', icon_value=593, emboss=True, depress=(bpy.context.tool_settings.mesh_select_mode[0] and 'EDIT_MESH'==bpy.context.mode))
        op = layout.operator('sna.face_mode__455f3', text='Face Mode ', icon_value=571, emboss=True, depress=(bpy.context.tool_settings.mesh_select_mode[2] and 'EDIT_MESH'==bpy.context.mode))
        op = layout.operator('sna.edge_mode_d3c76', text='Edge Mode', icon_value=565, emboss=True, depress=(bpy.context.tool_settings.mesh_select_mode[1] and 'EDIT_MESH'==bpy.context.mode))
        if 'OBJECT'==bpy.context.mode:
            op = layout.operator('sna.object_mode_toggle_67804', text='Edit Mode', icon_value=163, emboss=True, depress=False)
        else:
            op = layout.operator('sna.object_mode_toggle_67804', text='Object Mode', icon_value=164, emboss=True, depress=False)
        row_02B5E = layout.row(heading='', align=True)
        row_02B5E.alert = False
        row_02B5E.enabled = True
        row_02B5E.active = True
        row_02B5E.use_property_split = True
        row_02B5E.use_property_decorate = False
        row_02B5E.scale_x = 1.25
        row_02B5E.scale_y = 1.25
        row_02B5E.alignment = 'Expand'.upper()
        row_02B5E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_02B5E.operator('sna.xray_toggle_db11b', text='', icon_value=647, emboss=True, depress=False)
        op = row_02B5E.operator('sna.wireframe_mode_b8161', text='', icon_value=646, emboss=True, depress=False)
        op = row_02B5E.operator('sna.solid_mode_ef505', text='', icon_value=644, emboss=True, depress=False)
        op = row_02B5E.operator('sna.material_mode_32ff0', text='', icon_value=205, emboss=True, depress=False)
        op = row_02B5E.operator('sna.render_mode_a1e1d', text='', icon_value=643, emboss=True, depress=False)


class SNA_OT_Object_Mode_Toggle_67804(bpy.types.Operator):
    bl_idname = "sna.object_mode_toggle_67804"
    bl_label = "object mode toggle"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Object_Mode_Toggle001_9470D(bpy.types.Operator):
    bl_idname = "sna.object_mode_toggle001_9470d"
    bl_label = "object mode toggle.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Xray_Toggle_Db11B(bpy.types.Operator):
    bl_idname = "sna.xray_toggle_db11b"
    bl_label = "X-RAY Toggle"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.view3d.toggle_xray()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Solid_Mode_Ef505(bpy.types.Operator):
    bl_idname = "sna.solid_mode_ef505"
    bl_label = "Solid Mode"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.space_data.shading.type = 'SOLID'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Material_Mode_32Ff0(bpy.types.Operator):
    bl_idname = "sna.material_mode_32ff0"
    bl_label = "Material Mode"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.space_data.shading.type = 'MATERIAL'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Render_Mode_A1E1D(bpy.types.Operator):
    bl_idname = "sna.render_mode_a1e1d"
    bl_label = "Render Mode"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.space_data.shading.type = 'RENDERED'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Wireframe_Mode_B8161(bpy.types.Operator):
    bl_idname = "sna.wireframe_mode_b8161"
    bl_label = "Wireframe Mode"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.space_data.shading.type = 'WIREFRAME'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Toggle_Mode_Selector_A417C(bpy.types.Operator):
    bl_idname = "sna.toggle_mode_selector_a417c"
    bl_label = "toggle mode selector"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_modes_pie_menu_setting = (not bpy.context.scene.sna_modes_pie_menu_setting)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_AddonPreferences_9F58B(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        if not (False):
            layout = self.layout 
            op = layout.operator('sna.toggle_mode_selector_a417c', text='modes pie menu', icon_value=0, emboss=True, depress=bpy.context.scene.sna_modes_pie_menu_setting)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_modes_pie_menu_setting = bpy.props.BoolProperty(name='modes pie menu setting', description='', default=True)
    bpy.utils.register_class(SNA_OT_Vertex_Mode__68Ea5)
    bpy.utils.register_class(SNA_OT_Edge_Mode_D3C76)
    bpy.utils.register_class(SNA_OT_Face_Mode__455F3)
    bpy.utils.register_class(SNA_MT_88FD1)
    bpy.utils.register_class(SNA_OT_Object_Mode_Toggle_67804)
    bpy.utils.register_class(SNA_OT_Object_Mode_Toggle001_9470D)
    bpy.utils.register_class(SNA_OT_Xray_Toggle_Db11B)
    bpy.utils.register_class(SNA_OT_Solid_Mode_Ef505)
    bpy.utils.register_class(SNA_OT_Material_Mode_32Ff0)
    bpy.utils.register_class(SNA_OT_Render_Mode_A1E1D)
    bpy.utils.register_class(SNA_OT_Wireframe_Mode_B8161)
    bpy.utils.register_class(SNA_AddonPreferences_9F58B)
    bpy.utils.register_class(SNA_OT_Toggle_Mode_Selector_A417C)
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS',
        ctrl=False, alt=False, shift=False, repeat=False)
    kmi.properties.name = 'SNA_MT_88FD1'
    addon_keymaps['115DC'] = (km, kmi)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_modes_pie_menu_setting
    bpy.utils.unregister_class(SNA_OT_Vertex_Mode__68Ea5)
    bpy.utils.unregister_class(SNA_OT_Edge_Mode_D3C76)
    bpy.utils.unregister_class(SNA_OT_Face_Mode__455F3)
    bpy.utils.unregister_class(SNA_MT_88FD1)
    bpy.utils.unregister_class(SNA_OT_Object_Mode_Toggle_67804)
    bpy.utils.unregister_class(SNA_OT_Object_Mode_Toggle001_9470D)
    bpy.utils.unregister_class(SNA_OT_Xray_Toggle_Db11B)
    bpy.utils.unregister_class(SNA_OT_Solid_Mode_Ef505)
    bpy.utils.unregister_class(SNA_OT_Material_Mode_32Ff0)
    bpy.utils.unregister_class(SNA_OT_Render_Mode_A1E1D)
    bpy.utils.unregister_class(SNA_OT_Wireframe_Mode_B8161)
    bpy.utils.unregister_class(SNA_AddonPreferences_9F58B)
    bpy.utils.unregister_class(SNA_OT_Toggle_Mode_Selector_A417C)
