from win32gui import GetForegroundWindow, GetWindowText
import time
import pyautogui
from git import Repo

def saving(): # Loop over each character in the string
    pyautogui.hotkey('ctrl', 's')

PATH_OF_GIT_REPO = r'path\to\your\project\folder\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'commit'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')   

def is_it_vscode():
    hwnd = GetForegroundWindow()
    window_title = GetWindowText(hwnd)
    if "Visual Studio Code" in window_title:
        return True
    else:
        return False

is_it = is_it_vscode()
if is_it_vscode:
    print("Saving now!")
    saving()
    time.sleep(60)
    git_push()