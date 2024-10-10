from maya import cmds
import maya.mel as mel

def ResetController():
    create_reset_ctrl_window()

def reset_all():
    selected_objects = get_selects()
    
    for obj in selected_objects:
        cmds.move(0, 0, 0, obj, localSpace = True, absolute = True)
        cmds.rotate(0, 0, 0, obj, absolute=True)
        cmds.scale(1, 1, 1, obj, absolute=True)

def reset_rotate():
    selected_objects = get_selects()
    for obj in selected_objects:
        cmds.rotate(0, 0, 0, obj, absolute=True)

def reset_rotateZ():
    selected_objects = get_selects()
    for obj in selected_objects:
        cmds.rotate(0, obj, absolute=True, z = True)

def reset_rotateXZ():
    selected_objects = get_selects()
    for obj in selected_objects:
        cmds.rotate(0, 0, obj, absolute=True, xz = True)

def reset_translate():
    selected_objects = get_selects()
    for obj in selected_objects:
        cmds.move(0, 0, 0, obj, localSpace = True, absolute = True)

def reset_scale():
    selected_objects = get_selects()
    for obj in selected_objects:
        cmds.scale(1, 1, 1, obj, absolute=True)

def reset_foot():
    selected_objects = get_selects()
    for obj in selected_objects:
        cmds.move(0, obj, localSpace = True, absolute = True, y = True)
        cmds.rotate(0, 0, obj, absolute=True, xz = True)

def get_selects():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.error("not selected")
        return 
    return selected_objects

def create_reset_ctrl_window():
    # ウィンドウが既に存在する場合は削除
    if cmds.window("myWindow", exists=True):
        cmds.deleteUI("myWindow", window=True)

    # ウィンドウの作成
    window = cmds.window("myWindow", title="Reset Controller", widthHeight=(300, 240), sizeable=False)

    # レイアウトの作成
    column_layout = cmds.columnLayout(adjustableColumn=True, parent=window)

    # ボタンの作成
    reset_all_button = cmds.button(label="Reset All", command="reset_all()", parent=column_layout)
    cmds.separator(height=10, style='none')  # スペースを作成
    reset_foot_button = cmds.button(label="Reset Foot", command="reset_foot()", parent=column_layout)
    cmds.separator(height=10, style='none')  # スペースを作成
    reset_rotate_button = cmds.button(label="Reset rotate", command="reset_rotate()", parent=column_layout)
    cmds.separator(height=10, style='none')  # スペースを作成
    reset_rotate_z_button = cmds.button(label="Reset rotateZ", command="reset_rotateZ()", parent=column_layout)
    cmds.separator(height=10, style='none')  # スペースを作成
    reset_rotate_xz_button = cmds.button(label="Reset rotateXZ", command="reset_rotateXZ()", parent=column_layout)
    cmds.separator(height=10, style='none')  # スペースを作成
    reset_translate_button = cmds.button(label="Reset Translate", command="reset_translate()", parent=column_layout)
    cmds.separator(height=10, style='none')  # スペースを作成
    reset_scale_button = cmds.button(label="Reset Scale", command="reset_scale()", parent=column_layout)

    # ウィンドウの表示
    cmds.showWindow(window)

ResetController()