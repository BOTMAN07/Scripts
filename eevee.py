bl_info = {
    "name" : "Eevee Rig Addon",
    "author" : "Aftermath#1810",
    "version" : (1, 0),
    "blender" : (2, 92, 0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "3D View",
    
}

import bpy

class MainPanel(bpy.types.Panel):
    bl_label = "Eevee rig script"
    bl_idname = "MYADDON_PT_my_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Eevee Rig'
    
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Click on the buttons to select a dye.")
        row = layout.row()
        row.operator('skin.dye_change')
        row = layout.row()
        row.operator('skin.dye_change1')
        row = layout.row()
        row.operator('skin.dye_change2')
        row = layout.row()
        row.operator('skin.dye_change3')
        row = layout.row()
        row.operator('skin.dye_change4')
        row = layout.row()
        row.operator('skin.dye_change5')
        row = layout.row()
        row.operator('skin.dye_change6')
        row = layout.row()
        row.operator('skin.dye_change7')
        row = layout.row()
        row.operator('skin.dye_change8')
        row = layout.row()
        row.operator('skin.dye_change9')
        row = layout.row()
        row.operator('skin.dye_change10')
        row = layout.row()
        row.operator('skin.dye_change11')
        row = layout.row()
        row.operator('skin.dye_change12')
        row = layout.row()
        row.operator('skin.dye_change13')
        row = layout.row()
        row.label(text="Class dyes")
        row = layout.row()
        row.operator('skin.dye_change14')
        row = layout.row()
        row.operator('skin.dye_change15')
        row = layout.row()
        row.operator('skin.dye_change16')
        row = layout.row()
        row.operator('skin.dye_change17')
        row = layout.row()
        row.operator('skin.dye_change18')
        row = layout.row()
        row.label(text = "By: Aftermath#1810")
        

  
  

    
 #changing dye colors   
class Vantablack(bpy.types.Operator):
    bl_label = "Vantablack"
    bl_idname = 'skin.dye_change'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.000910581, 0.000910581, 0.000910581, 1)
        custom_group.inputs[2].default_value = (0.000910581, 0.000910581, 0.000910581, 1)
        custom_group.inputs[4].default_value = (0.000910581, 0.000910581, 0.000910581, 1)
        custom_group.inputs[5].default_value = (0.000910581, 0.000910581, 0.000910581, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
        
class Spectralon(bpy.types.Operator):
    bl_label = "Spectralon"
    bl_idname = 'skin.dye_change1'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (1, 1, 1, 1)
        custom_group.inputs[2].default_value = (1, 1, 1, 1)
        custom_group.inputs[4].default_value = (1, 1, 1, 1)
        custom_group.inputs[5].default_value = (1, 1, 1, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
 
    
class Crimson(bpy.types.Operator):
    bl_label = "Crimson"
    bl_idname = 'skin.dye_change2'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (1, 0.0561284, 0.0595113, 1)
        custom_group.inputs[2].default_value = (0.00242822, 0.00242822, 0.00242822, 1)
        custom_group.inputs[4].default_value = (0.00242822, 0.00242822, 0.00242822, 1)
        custom_group.inputs[5].default_value = (1, 0.0561284, 0.0595113, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
        
class Amberite(bpy.types.Operator):
    bl_label = "Amberite"
    bl_idname = 'skin.dye_change3'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (1, 1, 0.0331048, 1)
        custom_group.inputs[2].default_value = (0.0116123, 0.0116122, 0.0116122, 1)
        custom_group.inputs[4].default_value = (0.0116123, 0.0116122, 0.0116122, 1)
        custom_group.inputs[5].default_value = (1, 1, 0.0331048, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Coldsnap(bpy.types.Operator):
    bl_label = "Coldsnap"
    bl_idname = 'skin.dye_change4'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.0368893, 0.775823, 1, 1)
        custom_group.inputs[2].default_value = (1,1,1,1)
        custom_group.inputs[4].default_value = (1,1,1,1)
        custom_group.inputs[5].default_value = (0.0368893, 0.775823, 1, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Sugarbear(bpy.types.Operator):
    bl_label = "Sugarbear"
    bl_idname = 'skin.dye_change5'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (1, 0.3564, 0.730461, 1)
        custom_group.inputs[2].default_value = (1, 0.3564, 0.730461, 1)
        custom_group.inputs[4].default_value = (1, 0.3564, 0.730461, 1)
        custom_group.inputs[5].default_value = (1, 0.3564, 0.730461, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    

    
class StreamSuit(bpy.types.Operator):
    bl_label = "StreamSuit"
    bl_idname = 'skin.dye_change6'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.122139, 0.0561285, 0.434154, 1)
        custom_group.inputs[2].default_value = (1,1, 1, 1)
        custom_group.inputs[4].default_value = (1, 1, 1, 1)
        custom_group.inputs[5].default_value = (0.122139, 0.0561285, 0.434154, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Terra(bpy.types.Operator):
    bl_label = "Terra"
    bl_idname = 'skin.dye_change7'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.0116121, 0.791298, 0.0802199, 1)
        custom_group.inputs[2].default_value = (0.0168074, 0.0185002, 0.0193824, 1)
        custom_group.inputs[4].default_value = (0.0168074, 0.0185002, 0.0193824, 1)
        custom_group.inputs[5].default_value = (0.0116121, 0.791298, 0.0802199, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Lavender(bpy.types.Operator):
    bl_label = "Lavender"
    bl_idname = 'skin.dye_change8'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.768152, 0.0561284, 1, 1)
        custom_group.inputs[2].default_value = (0.205079, 0.0561285, 1, 1)
        custom_group.inputs[4].default_value = (0.205079, 0.0561285, 1, 1)
        custom_group.inputs[5].default_value = (0.768152, 0.0561284, 1, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Carotine(bpy.types.Operator):
    bl_label = "Carotine"
    bl_idname = 'skin.dye_change9'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.991102, 0.341914, 0.0595113, 1)
        custom_group.inputs[2].default_value = (0.068478, 0.799103, 0.144129, 1)
        custom_group.inputs[4].default_value = (0.068478, 0.799103, 0.144129, 1)
        custom_group.inputs[5].default_value = (0.991102, 0.341914, 0.0595113, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Cocoa(bpy.types.Operator):
    bl_label = "Cocoa"
    bl_idname = 'skin.dye_change10'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.127438, 0.0382044, 0.0144438, 1)
        custom_group.inputs[2].default_value = (0.0159963, 0.00699541, 0.00367651, 1)
        custom_group.inputs[4].default_value = (0.0159963, 0.00699541, 0.00367651, 1)
        custom_group.inputs[5].default_value = (0.127438, 0.0382044, 0.0144438, 1)
        custom_group.inputs[6].default_value = (0.205079, 0.109462, 0.0578054, 1)
        return{'FINISHED'}

class KPD_Uniform(bpy.types.Operator):
    bl_label = "KPD Uniform"
    bl_idname = 'skin.dye_change11'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.0202886, 0.0307135, 0.0865005, 1)
        custom_group.inputs[2].default_value = (0.0466651, 0.0512695, 0.0528607, 1)
        custom_group.inputs[4].default_value = (0.0466651, 0.0512695, 0.0528607, 1)
        custom_group.inputs[5].default_value = (0.0202886, 0.0307135, 0.0865005, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Dusty(bpy.types.Operator):
    bl_label = "Dusty"
    bl_idname = 'skin.dye_change12'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.219526, 0.238398, 0.254152, 1)
        custom_group.inputs[2].default_value = (0, 0, 0, 1)
        custom_group.inputs[4].default_value = (0, 0, 0, 1)
        custom_group.inputs[5].default_value = (0.219526, 0.238398, 0.254152, 1)
        custom_group.inputs[6].default_value = (0.205079, 0.109462, 0.0578054, 1)
        return{'FINISHED'}
    
class Exotic(bpy.types.Operator):
    bl_label = "Exotic"
    bl_idname = 'skin.dye_change13'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.938686, 0.552011, 0.38643, 1)
        custom_group.inputs[2].default_value = (0.938686, 0.552011, 0.38643, 1)
        custom_group.inputs[4].default_value = (0.938686, 0.552011, 0.38643, 1)
        custom_group.inputs[5].default_value = (0.938686, 0.552011, 0.38643, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}


#class dyes begin here


class Triggerman(bpy.types.Operator):
    bl_label = "Triggerman"
    bl_idname = 'skin.dye_change14'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.130137, 0.138432, 0.155927, 1)
        custom_group.inputs[2].default_value = (1, 1, 1, 1)
        custom_group.inputs[4].default_value = (0.0251869, 0.0273209, 0.028426, 1)
        custom_group.inputs[5].default_value = (0.0251869, 0.0273209, 0.028426, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Marksman(bpy.types.Operator):
    bl_label = "Marksman"
    bl_idname = 'skin.dye_change15'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.158961, 0.250158, 0.124772, 1)
        custom_group.inputs[2].default_value = (0.021219, 0.0307135, 0.017642, 1)
        custom_group.inputs[4].default_value = (0.107023, 0.165132, 0.0822827, 1)
        custom_group.inputs[5].default_value = (0.107023, 0.165132, 0.0822827, 1)
        custom_group.inputs[6].default_value = (0.031896, 0.0343398, 0.0368895, 1)
        return{'FINISHED'}
    
class Detective(bpy.types.Operator):
    bl_label = "Detective"
    bl_idname = 'skin.dye_change16'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.270498, 0.132868, 0.066626, 1)
        custom_group.inputs[2].default_value = (0.0481718, 0.0273209, 0.0144438, 1)
        custom_group.inputs[4].default_value = (0.0886556, 0.127438, 0.212231, 1)
        custom_group.inputs[5].default_value = (0.0886556, 0.127438, 0.212231, 1)
        custom_group.inputs[6].default_value = (0.205079, 0.109462, 0.0578054, 1)
        return{'FINISHED'}
  

class SMG(bpy.types.Operator):
    bl_label = "Run N Gun"
    bl_idname = 'skin.dye_change17'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.135633, 0.412543, 0.799103, 1)
        custom_group.inputs[2].default_value = (1, 1, 1, 1)
        custom_group.inputs[4].default_value = (0.043735, 0.122139, 0.238398, 1)
        custom_group.inputs[5].default_value = (0.043735, 0.122139, 0.238398, 1)
        custom_group.inputs[6].default_value = (0.205079, 0.109462, 0.0578054, 1)
        return{'FINISHED'}
  
class Commando(bpy.types.Operator):
    bl_label = "Commando"
    bl_idname = 'skin.dye_change18'
    
    def execute(self, context):
        #selecting the skin mat
        skin_material = bpy.data.materials["Skin"]
       
        skin_material.use_nodes = True
        

        #Selecting the custom skin group
        custom_group = skin_material.node_tree.nodes.get("Group")
            
        custom_group.location = (-400, 200)
        custom_group.inputs[1].default_value = (0.017642, 0.0193824, 0.021219, 1)
        custom_group.inputs[2].default_value = (0.00604883, 0.00604883, 0.00604883, 1)
        custom_group.inputs[4].default_value = (0.00749903, 0.00802319, 0.00856813, 1)
        custom_group.inputs[5].default_value = (0.00749903, 0.00802319, 0.00856813, 1)
        custom_group.inputs[6].default_value = (0.53948, 0.194618, 0.0451862, 1)
        return{'FINISHED'}
  

def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(Vantablack)
    bpy.utils.register_class(Spectralon)
    bpy.utils.register_class(Crimson)
    bpy.utils.register_class(Amberite)
    bpy.utils.register_class(Coldsnap)
    bpy.utils.register_class(Sugarbear)
    bpy.utils.register_class(StreamSuit)
    bpy.utils.register_class(Terra)
    bpy.utils.register_class(Lavender)
    bpy.utils.register_class(Carotine)
    bpy.utils.register_class(Cocoa)
    bpy.utils.register_class(KPD_Uniform)
    bpy.utils.register_class(Dusty)
    bpy.utils.register_class(Exotic)
    bpy.utils.register_class(Triggerman)
    bpy.utils.register_class(Marksman)
    bpy.utils.register_class(Detective)
    bpy.utils.register_class(SMG)
    bpy.utils.register_class(Commando)



def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(Vantablack)
    bpy.utils.unregister_class(Spectralon)
    bpy.utils.unregister_class(Crimson)
    bpy.utils.unregister_class(Amberite)
    bpy.utils.unregister_class(Coldsnap)
    bpy.utils.unregister_class(Sugarbear)
    bpy.utils.unregister_class(StreamSuit)
    bpy.utils.unregister_class(Terra)
    bpy.utils.unregister_class(Terra)
    bpy.utils.unregister_class(Carotine)
    bpy.utils.unregister_class(Cocoa)
    bpy.utils.unregister_class(KPD_Uniform)
    bpy.utils.unregister_class(Dusty)
    bpy.utils.unregister_class(Exotic)
    bpy.utils.unregister_class(Triggerman)
    bpy.utils.unregister_class(Marksman)
    bpy.utils.unregister_class(Detective)
    bpy.utils.unregister_class(SMG)
    bpy.utils.register_class(Commando)




if __name__ == "__main__":
    register()
