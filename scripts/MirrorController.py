from maya import cmds
import maya.mel as mel

def MirrorController():
    selected_objects = cmds.ls(sl=True, dag = True, type="transform")

    print(getCtrlName(selected_objects[0]))
    return
    
def getCtrlName(obj):
    counter = 0
    for c in list(reversed(obj)):
        if c == ':':
            break
        counter+=1
    return obj[-counter:]

    if not selected_objects:
        cmds.error("not selected")
        return
    
    for obj in selected_objects:

        cmds.move(0, 0, 0, obj, localSpace = True, absolute = True)
        cmds.rotate(0, 0, 0, obj, absolute=True)
        cmds.scale(1, 1, 1, obj, absolute=True)