import os, subprocess, keyboard, re
from reggisearch import search_values # pip install reggisearch
from gracefully_kill import kill_process
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
creationflags = subprocess.CREATE_NO_WINDOW
invisibledict = {
    "startupinfo": startupinfo,
    "creationflags": creationflags,
    "start_new_session": True,
}

def kill_app(p, hotkey):
    kill_process(p)
    keyboard.remove_hotkey(hotkey)
def execute_app(file:str,path:str|tuple,exit_keys:str='ctrl+alt+q',add_options:tuple|list=(),headless:bool=True,**kwargs) ->subprocess.Popen|None:
    file = os.path.normpath(file)
    if os.path.exists(str(path)):
        path=os.path.normpath(path)
    else:
        try:
            path_ = search_values(mainkeys=path[0],
                          subkeys=path[1])
            path = re.findall(fr'\b\w\w?:\\.*?\.exe\b', path_[path[0]][path[1]], flags=re.I)[0]
        except Exception:
            print('Path not found')
            return
    headlessdict = invisibledict if headless else {}
    p=subprocess.Popen([path,*add_options,file],stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE,**headlessdict,**kwargs)
    if exit_keys in keyboard.__dict__['_hotkeys']:
        keyboard.remove_hotkey(exit_keys)
    keyboard.add_hotkey(exit_keys, lambda:kill_app(p, exit_keys))
    return p

path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
#path = r'HKEY_CLASSES_ROOT\Directory\shell\AddToPlaylistVLC','Icon'
exit_keys = 'ctrl+alt+q'
mp3file = r"F:\4 Promille - Oi the Meeting.mp3"
argumentos = (
    "--input-repeat=0",    "-Idummy",    "--play-and-exit",    "--qt-minimal-view",
)
p=execute_app(file=mp3file,path=path,exit_keys='ctrl+alt+q',add_options=argumentos,headless=True)
file=r"C:\Users\hansc\Downloads\safbdf.txt"
path=r'C:\Windows\system32\notepad.exe'
argumentos=()
p=execute_app(file=mp3file,path=path,exit_keys='ctrl+alt+w',add_options=argumentos,headless=True)









