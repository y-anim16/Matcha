from maya import cmds
import maya.mel as mel

def ResetController():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.error("not selected")
        return
    
    for obj in selected_objects:
        cmds.move(0, 0, 0, obj, localSpace = True, absolute = True)
        cmds.rotate(0, 0, 0, obj, absolute=True)
        cmds.scale(1, 1, 1, obj, absolute=True)