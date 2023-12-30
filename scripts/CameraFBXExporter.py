from maya import cmds
import maya.mel as mel
import os

def ExportCameraFBX():
    rig_cam_name = "CameraRig:RenderCamera"
    renderer_name = "RenderCamera"

    SelectRenderer(rig_cam_name)
    DuplicateRenderer(renderer_name)
    SetParentConstraint(rig_cam_name, renderer_name)
    BakeSimulation(renderer_name)
    Export(renderer_name)

def SelectRenderer(rig_cam_name):
    cmds.select(clear=True)
    cmds.select(rig_cam_name)

def DuplicateRenderer(renderer_name):
    cmds.duplicate(rr=True, un=True)
    cmds.parent(w=True)

    constraints = cmds.listRelatives(renderer_name, type="constraint")
    if constraints:
        # コンストレイントを解除
        cmds.delete(constraints)
        print("Removed constraint")
    else:
        print(renderer_name + " don't has constraint")

    # リグ自体をコンストレイントで動かしていたらlockかかっているので解除
    cmds.setAttr(renderer_name + ".translateX", lock=False)
    cmds.setAttr(renderer_name + ".translateY", lock=False)
    cmds.setAttr(renderer_name + ".translateZ", lock=False)
    cmds.setAttr(renderer_name + ".rotateX", lock=False)
    cmds.setAttr(renderer_name + ".rotateY", lock=False)
    cmds.setAttr(renderer_name + ".rotateZ", lock=False)

def SetParentConstraint(rig_cam_name, renderer_name):
    cmds.parentConstraint(rig_cam_name, renderer_name)

def BakeSimulation(renderer_name):
    start_frame = cmds.playbackOptions(query=True, minTime=True)
    end_frame = cmds.playbackOptions(query=True, maxTime=True)
    cmds.bakeResults(renderer_name, t = (start_frame, end_frame))

def Export(renderer_name):
    scene_file_name = cmds.file(query=True, sceneName=True)
    # シーンファイルのディレクトリ部分を取得
    scene_file_dir = os.path.dirname(scene_file_name)

    # カメラを選択
    cmds.select(renderer_name, replace=True)

    # エクスポート先のFBXファイル名を設定
    file_name_without_extension, _ = os.path.splitext(os.path.basename(scene_file_name))
    export_path = scene_file_dir + "/"  + file_name_without_extension + "_camera.fbx"

    # FBXファイルでエクスポート
    mel.eval('file -force -options \"v=0;\" -typ \"FBX export\" -pr -es \"%s\";' % export_path)

