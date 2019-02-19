#user/bin/bash ./Open Blender on linux

	#sudo ./
	# Jei nereikia update, uzkomentuoti arba istrinti

	echo'#^^^^^^^^^^^^^^^^^ Updating ^^^^^^^^^^^^^^^^^^^^^^^^#'
	sudo apt-get update -y

	echo'#~~~~~~~~~~~~~~~~ Locating script ~~~~~~~~~~~~~~~~~~#'
	locate Sphere_Square.py
	echo '#^^^^^^^^^^^^^^^ Locating Blender ^^^^^^^^^^^^^^^^#'
	whereis blender
	#blender --factory-startup # svariai atidaro Blenderi 
	#filename = "/home/rita/Sphere_Square.py"
	#exec(compile(open(filename).read(), filename, 'exec'))
	blender --python /home/$USER/Sphere_Square.py
	#import bpy
	#script = bpy.data.texts["Sphere_Square.py"]
	#exec(script.as_string())
	#cd /usr/bin/blender

