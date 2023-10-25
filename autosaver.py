from win32gui import GetForegroundWindow, GetWindowText
import time
import pyautogui

def saving(): # Loop over each character in the string
    pyautogui.hotkey('ctrl', 's')

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




