import bpy
import math
import random
import os
import sys
import pathlib
subloc=str(pathlib.Path(__file__).parent.absolute())
sys.path.append(subloc)

bpy.data.objects["Final_Snowflake"].hide_viewport = True
bpy.data.objects["Final_Snowflake"].hide_render = True
new_mat = bpy.data.materials["Material.006"]
finhex = open(f"{subloc}/subscripts/hex.txt", "rt")
hexvalue= eval(finhex.read())
print(hexvalue)
bpy.data.materials["Material.006"].node_tree.nodes["Principled BSDF"].inputs[0].default_value  = hexvalue
finhex.close()

finsvg = open(f"{subloc}/subscripts/svg_dir.txt", "rt")
path=finsvg.read()
finsvg.close()
bpy.ops.import_curve.svg(filepath=path)
finrender = open(f"{subloc}/subscripts/renderengine_selector.txt", "rt")
renderer=finrender.read()
finrender.close()
bpy.context.scene.render.engine = renderer
finsamples=open(f"{subloc}/subscripts/samples.txt", "rt")
samplesam=finsamples.read()
if renderer=='CYCLES':
    bpy.context.scene.cycles.samples=int(samplesam)
else:
    bpy.context.scene.eevee.taa_render_samples=int(samplesam)
finrenderdir = open(f"{subloc}/subscripts/render_dir.txt", "rt")
renderdir=finrenderdir.read()
finrenderdir.close()
bpy.context.scene.render.filepath=renderdir

finoptions = open(f"{subloc}/subscripts/optionanim.txt", "rt")
rendertype=finoptions.read()
finoptions.close()
totframes=240 #default
finframes = open(f"{subloc}/subscripts/frames.txt", "rt")
totframes=int(finframes.read())
finframes.close()
if totframes>100:
    onefifth=round(totframes/5)
elif totframes>50 and totframes<100:
    onefifth=round(totframes/3)
else:
    onefifth=round(totframes/2)

bpy.ops.object.select_all(action='DESELECT')
#bpy.data.objects['Curve'].select_set(True)
#bpy.ops.object.delete()
for collection in bpy.data.collections:
    print(collection.name)
    if collection.name=="PREEXISTINGITEMS":
        pass
    else:
        reqcol=collection.name
object = bpy.data.objects['Curve.001']
for o in bpy.data.collections[reqcol].all_objects:
    o.select_set(True)
    o.data.dimensions = '2D'
    o.data.bevel_depth = 0.0025
    o.data.use_fill_caps = True
    o.data.extrude = 0.0001
    o.select_set(False)

bpy.context.view_layer.objects.active = object 
for obj in bpy.data.collections[reqcol].all_objects:
        obj.select_set(True)
bpy.ops.object.convert(target='MESH')
for obj in bpy.data.collections[reqcol].all_objects:
        obj.select_set(False)
for obj in bpy.data.collections[reqcol].all_objects:
    obj.select_set(True)
bpy.ops.object.join()
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
bpy.ops.object.convert(target='MESH')
bpy.data.objects["Curve.001"].location = (0,0,0)
bpy.data.objects["Curve.001"].rotation_euler.x = math.radians(-90)
bpy.data.objects["Curve.001"].scale = (1.392,1.521,2.656)
ob = bpy.context.active_object
ob.active_material = bpy.data.materials.get("Material.001")
if rendertype=="still":
    bpy.context.object.rotation_euler[2] = 0
    bpy.context.scene.frame_set(random.randint(1,240))
    print(rendertype)
    bpy.ops.render.render('INVOKE_DEFAULT', animation=False, write_still=True, use_viewport=False, scene="scene")
else:
    bpy.context.scene.frame_set(1)
    bpy.context.object.rotation_euler[2] = 1.0472
    ob.keyframe_insert("rotation_euler")
    bpy.context.scene.frame_set(onefifth)
    bpy.context.object.rotation_euler[2] = -1.0472
    ob.keyframe_insert("rotation_euler")
    bpy.context.scene.frame_set(onefifth*2)
    bpy.context.object.rotation_euler[2] = 1.0472
    ob.keyframe_insert("rotation_euler")
    bpy.context.scene.frame_set(onefifth*3)
    bpy.context.object.rotation_euler[2] = -1.0472
    ob.keyframe_insert("rotation_euler")
    bpy.context.scene.frame_set(onefifth*4)
    bpy.context.object.rotation_euler[2] = 1.0472
    ob.keyframe_insert("rotation_euler")
    bpy.context.scene.frame_set(onefifth*5)
    bpy.context.object.rotation_euler[2] = -1.0472
    ob.keyframe_insert("rotation_euler")
    bpy.context.object.rotation_euler[2] = -1.0472
    print(rendertype)
    scn = bpy.context.scene
    scn.frame_start = 0
    scn.frame_end = totframes
    bpy.ops.render.render('INVOKE_DEFAULT', animation=True, use_viewport=False, scene="scene")
