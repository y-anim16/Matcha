from maya import cmds
import maya.mel as mel

def MovePivot2Component():
    selected = cmds.ls(selection=True, flatten=True)

    if len(selected) != 1:
        cmds.error("Please make only one selection.")
    
    vertex_list = cmds.filterExpand(selected, selectionMask=31)
    if vertex_list:
        # Get selected vertex position
        vertexPos = cmds.pointPosition(vertex_list[0])

        # Change to object mode
        mel.eval("toggleSelMode")
        mel.eval("changeSelectMode -object")
        
        # Reselect
        selected = cmds.ls(selection=True, objectsOnly=True)
        print(selected)

        # Move pivot
        cmds.move(vertexPos[0], vertexPos[1], vertexPos[2], selected[0] + '.scalePivot', selected[0] + '.rotatePivot', rpr=1)
        return
    
    edge_list = cmds.filterExpand(selected, selectionMask=32)
    if edge_list:
        print("Selected is edge")
        print(edge_list)
        return
    
    face_list = cmds.filterExpand(selected, selectionMask=34)
    if face_list:
        print("Selected is face")
        print(face_list)
        return
    
    cmds.error("Please select vertex or edge or face")