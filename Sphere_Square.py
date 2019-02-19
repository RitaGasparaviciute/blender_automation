import getpass
import bpy
from bpy import context
from bpy import ops
from bpy import data

#username esamo pc useris
username ='rita'
#isjungia splash screen'a
bpy.context.user_preferences.view.show_splash = False
# istrina kuba 
bpy.ops.object.delete(use_global=False)

#blenderis neleidzia paleist auto scriptingo su skriptu... reikia manually leisti
#bpy.ops.screen.userpref_show()

class blue_square:
	bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0.400, 0.300, 0.3500), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
color = bpy.data.materials.new('blue')
color.diffuse_color = (0.0,0.0,10.0)
color.diffuse_shader = 'LAMBERT'
color.diffuse_intensity = 10.0

square = bpy.data.objects['Plane']

#sukuria spalva
color = bpy.data.materials['blue']

#prideda spalva
square.data.materials.append(color)

class red_sphere:
	bpy.ops.mesh.primitive_uv_sphere_add(view_align=False, enter_editmode=False,location=(0.400, 0.300, 3.3500), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#bpy.context.scene.objects.active
color = bpy.data.materials.new('red')
color.diffuse_color = (20.0,0.0,0.0)
color.diffuse_shader = 'LAMBERT'
color.diffuse_intensity = 20.0

sphere = bpy.data.objects['Sphere']

# prideda spalva
color = bpy.data.materials['red']
sphere.data.materials.append(color)

# bent man linuxai neleidzia issaugot be passwordo, sitas snipetas tik echoina passworda
#class save_file:
#getpass()
#bpy.ops.wm.save_mainfile(filepath="/home/%username", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=False)
##### jei veikia reikia palaukt
