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
        changeModeToObject()

        # Move pivot
        movePivot(vertexPos)
        return
    
    edge_list = cmds.filterExpand(selected, selectionMask=32)
    if edge_list:
        # Get vertex positions from selected edge
        vertexes = cmds.polyListComponentConversion(fromEdge=True, toVertex=True)
        vertexPositions = [cmds.xform(vertex, query=True, translation=True, worldSpace=True) for vertex in vertexes]
        if len(vertexPositions) == 1:
            vertexPositions = getPositionsFromSlice(vertexPositions)
        newVertexPos = getCenterPosition(vertexPositions)

        # Change to object mode
        changeModeToObject()

        # Move pivot
        movePivot(newVertexPos)
        return
    
    face_list = cmds.filterExpand(selected, selectionMask=34)
    if face_list:
        # Get vertex positions from selected face
        vertexes = cmds.polyListComponentConversion(fromFace=True, toVertex=True)
        vertexPositions = [cmds.xform(vertex, query=True, translation=True, worldSpace=True) for vertex in vertexes]
        if len(vertexPositions) < 4:
            vertexPositions = getPositionsFromSlice(vertexPositions)
        newVertexPos = getCenterPosition(vertexPositions)

        # Change to object mode
        changeModeToObject()

        # Move pivot
        movePivot(newVertexPos)
        return
    
    cmds.error("Please select vertex or edge or face")

def getPositionsFromSlice(vertexPositions):
    positionListTable = []
    for positions in vertexPositions:
        positionList = [positions[i:i+3] for i in range(0, len(positions), 3)]
        for pos in positionList:
            positionListTable.append(pos)
    return positionListTable

def changeModeToObject():
    mel.eval("toggleSelMode")
    mel.eval("changeSelectMode -object")

def movePivot(newPos):
    # Reselect
    selected = cmds.ls(selection=True, objectsOnly=True)

    # Move pivot
    cmds.move(newPos[0], newPos[1], newPos[2], selected[0] + '.scalePivot', selected[0] + '.rotatePivot', rpr=1)

def getCenterPosition(vertexes):
    positionX = 0
    positionY = 0
    positionZ = 0

    for vertex in vertexes:
        positionX += vertex[0]
        positionY += vertex[1]
        positionZ += vertex[2]

    vertexesCount = len(vertexes)
    return [positionX/vertexesCount, positionY/vertexesCount, positionZ/vertexesCount]