
from ALL_CODE import Navigate_to_did
from ALL_CODE import login_process
from ALL_CODE import VideoCreation
from ALL_CODE import MAINVIDEO
from ALL_CODE import chatgpt
from ALL_CODE import Move_CursorMove
from ALL_CODE import TextWritingdid
from ALL_CODE import VideoUpload




def perform_actions():
    
    Navigate_to_did.MOUSEUPARJAYE()
    print("Job 1 Done")
    Navigate_to_did.navigate_to_did_and_login()
    print("Job 2 DOne")
    
    login_process.extract_and_copy_email()
    print("Job 3 DOne")
    login_process.newprocess()
    print("Job 4 done")
    login_process.emailprocess()
    print("Job 5 DOne")
    login_process.confirmbuttonclick()
    print("Job 6 DOne")

    VideoCreation.create_video()
    VideoCreation.Again_login()
    VideoCreation.relogin()
    VideoCreation.login_window()
    VideoCreation.bakwash()
    VideoCreation.bakwash2()
    VideoCreation.bakwash3()
    VideoCreation.bakwash4()
    VideoCreation.bakwash5()

    MAINVIDEO.Create_video()
    
    chatgpt.open_firefox()
    chatgpt.open_new_tab()
    chatgpt.switch_tabs()
    chatgpt.close_tab()
    chatgpt.navigate_to_chat_gpt()
    chatgpt.SavingMaetialTotext()
    chatgpt.AskingGPTFORTITLE()
    chatgpt.SavingTitleToText()
    chatgpt.c_losing()
    
    Move_CursorMove.Move_mousetocentre()
    Move_CursorMove.move_mousetoclickablezone()

    TextWritingdid.retrievematerialfromfiletorename()
    TextWritingdid.click_on_screen(1576, 477)
    print("Job Unknown1 Done")
    TextWritingdid.writing()
    TextWritingdid.VoiceSelection()
    print("Job Unknown2 Done")
    TextWritingdid.Generatevideoparclick(1792, 43)
    print("Job Unknown3 Done")
    TextWritingdid.patanahikyahai()
    print("Job Unknown4 Done")
    TextWritingdid.VideoGenerate()
    print("Job Unknown5 Done")

    VideoUpload.clickonscreenagain(485, 285)
    VideoUpload.retrievetitlefromfiletorename()
    VideoUpload.RenameVideo()
    VideoUpload.DownladVideo()
    VideoUpload.Ending_all_Task()

perform_actions()
