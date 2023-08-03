from maya import cmds
import maya.mel as mel

def MirrorController():
    selected_objects = cmds.ls(sl=True, dag = True, type="transform")

    finishedCtrlNames = []
    for obj in selected_objects:
        namespace = getNamespace(obj)
        ctrlName = getCtrlName(obj)
        symmetryName = getSymmetryName(ctrlName)

        if symmetryName == None:
           mirrorNonSymmetryCtrl(obj)
        else:
            symmetryObj = cmds.ls(namespace + symmetryName)
            if symmetryObj:
                if namespace + symmetryName in finishedCtrlNames:
                    continue
                mirrorSymmetryCtrl(obj, symmetryObj)
                finishedCtrlNames.append(obj)
                finishedCtrlNames.append(namespace + symmetryName)
            else:
                print('failed')
    return
    
def getNamespace(obj):
    counter = 0
    for c in obj:
        counter+=1 #コロンも含めたいのでここでインクリメント
        if c == ':':
            break
    return obj[0:counter]

def getCtrlName(obj):
    counter = 0
    for c in list(reversed(obj)):
        if c == ':':
            break
        counter+=1
    return obj[-counter:]

def getSymmetryName(name):
    prefixL = 'L_'
    prefixR = 'R_'

    if name[:2] == prefixL:
        return name.replace(prefixL, prefixR)
    elif name[:2] == prefixR:
        return name.replace(prefixR, prefixL)
    else:
        return None

def mirrorNonSymmetryCtrl(obj):
        current_position = cmds.xform(obj, query=True, translation=True, objectSpace=True)
        current_rotation = cmds.xform(obj, query=True, rotation=True, objectSpace=True)

        symmetric_position = list(current_position)
        symmetric_position[0] = -current_position[0] # x axis

        symmetric_rotation = list(current_rotation)
        symmetric_rotation[1] = -current_rotation[1] # y axis
        symmetric_rotation[2] = -current_rotation[2] # z axis

        cmds.xform(obj, translation=symmetric_position, rotation=symmetric_rotation, objectSpace=True)

def mirrorSymmetryCtrl(obj, symmetryObj):
        current_position = cmds.xform(obj, query=True, translation=True, objectSpace=True)
        current_rotation = cmds.xform(obj, query=True, rotation=True, objectSpace=True)

        symmetry_current_position = cmds.xform(symmetryObj, query=True, translation=True, objectSpace=True)
        symmetry_current_rotation = cmds.xform(symmetryObj, query=True, rotation=True, objectSpace=True)

        symmetric_position = list(current_position)
        symmetric_position[0] = -current_position[0] # x axis
        symmetric_rotation = list(current_rotation)
        symmetric_rotation[1] = -current_rotation[1] # y axis
        symmetric_rotation[2] = -current_rotation[2] # z axis
        cmds.xform(symmetryObj, translation=symmetric_position, rotation=symmetric_rotation, objectSpace=True)

        swap_symmetric_position = list(symmetry_current_position)
        swap_symmetric_position[0] = -symmetry_current_position[0] # x axis
        swap_symmetric_rotation = list(symmetry_current_rotation)
        swap_symmetric_rotation[1] = -symmetry_current_rotation[1] # y axis
        swap_symmetric_rotation[2] = -symmetry_current_rotation[2] # z axis
        cmds.xform(obj, translation=swap_symmetric_position, rotation=swap_symmetric_rotation, objectSpace=True)