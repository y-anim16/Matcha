from maya import cmds
import maya.mel as mel

def MirrorController():
    selected_objects = cmds.ls(sl=True, dag = True, type="transform")

    for obj in selected_objects:
        ctrlName = getCtrlName(obj)
        print(ctrlName)

        prefix = getSymmetryPrefix(ctrlName)
        print(prefix)

        if prefix == None:
           mirrorNonSymmetryCtrl(obj)
    return
    
def getCtrlName(obj):
    counter = 0
    for c in list(reversed(obj)):
        if c == ':':
            break
        counter+=1
    return obj[-counter:]

def getSymmetryPrefix(name):
    if name[:2] == 'L_':
        return 'R_'
    elif name[:2] == 'R_':
        return 'L_'
    else:
        return None

    # if not selected_objects:
    #     cmds.error("not selected")
    #     return
    
    # for obj in selected_objects:

    #     cmds.move(0, 0, 0, obj, localSpace = True, absolute = True)
    #     cmds.rotate(0, 0, 0, obj, absolute=True)
    #     cmds.scale(1, 1, 1, obj, absolute=True)

def mirrorNonSymmetryCtrl(obj):
        current_position = cmds.xform(obj, query=True, translation=True, objectSpace=True)
        current_rotation = cmds.xform(obj, query=True, rotation=True, objectSpace=True)
        print(current_rotation)

        symmetric_position = list(current_position)
        symmetric_position[0] = -current_position[0] # x axis

        symmetric_rotation = list(current_rotation)
        symmetric_rotation[1] = -current_rotation[1] # y axis
        symmetric_rotation[2] = -current_rotation[2] # z axis

        cmds.xform(obj, translation=symmetric_position, rotation=symmetric_rotation, objectSpace=True)