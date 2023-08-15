from tkinter import *
from tkinter import ttk
from datetime import *
from pynput.keyboard import Key, Controller
import os, ctypes, subprocess, cv2

root = Tk()
root.title("Lock")
root.geometry("1707x1067")
root.attributes('-topmost',True)     
root.overrideredirect(True)

# -----------------------------------------------------------------------------------------------

loginlog = open("log.txt","a+")

keyboard = Controller()

def keyboardlock():

    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press('m')
    keyboard.release('m')
    keyboard.release(Key.alt_l)
    keyboard.release(Key.ctrl_l)

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

if process_exists("KeyFreeze_x64.exe") == True:
    print("keyfreeze already open")

elif process_exists("KeyFreeze_x64.exe") == False:
    os.startfile(r"C:\Users\jhan7\Downloads\KeyFreeze\KeyFreeze\Keyfreeze.exe")
    print('keyfreeze successfully opened')

else:
    print('STARTING KEYFREEZE ERROR')

def on_closing():
    pass

def passwordentered():
    if passwordbox.get() != "ctrlaltm":
        nowfail = datetime.now()
        loginlog.write(nowfail.strftime('%Y/%m/%d %I:%M:%S:%p') + "    failed to login" + "\n")
        
        video = cv2.VideoCapture(0) 
        check, frame = video.read()
        showPic = cv2.imwrite("failed.jpg",frame)
        video.release()

        keyboardlock()

    else:
        nowpass = datetime.now()
        loginlog.write(nowpass.strftime('%Y/%m/%d %I:%M:%S:%p') + "\n")
        loginlog.close()

        if process_exists("KeyFreeze_x64.exe") == True:
            os.system("TASKKILL /F /IM KeyFreeze_x64.exe")
            print("KeyFreeze is successfully turned off")

        elif process_exists("KeyFreeze_x64.exe") == False:
            print("KeyFreeze is already turned off")

        else:
            print("KEYFREEZE KILL ERROR")

        exit()

def passwordskip():
    skipbutton['state'] = DISABLED
    nowskip = datetime.now()
    loginlog.write(nowskip.strftime('%Y/%m/%d %I:%M:%S:%p') + "    unauthorized" + "\n")
    loginlog.flush()
    os.fsync(loginlog.fileno())
    video = cv2.VideoCapture(0) 
    check, frame = video.read()
    showPic = cv2.imwrite("unauthorized.jpg",frame)
    video.release()
    skipbutton['state'] = NORMAL
    ctypes.windll.user32.LockWorkStation()                          
    
# -----------------------------------------------------------------------------------------------

passwordbox = ttk.Entry(root, show = '*', font="Lato 50", width=10)
passwordbox.place(x=670, y=300)

enterbutton = ttk.Button(root, text="Enter", width=10, command=passwordentered)
enterbutton.grid(ipady=24, padx= 1090, pady=300)

skipbutton = ttk.Button(root, text="SKIP", command=passwordskip)
skipbutton.grid(ipadx=30,ipady = 20, pady =1)

explainlabel1 = ttk.Label(root, font="Lato 70", text="TYPE IN THE PASSWORD")
explainlabel1.place(x=300, y=20)

explainlabel2 = ttk.Label(root, font="Lato 50", text="PRESS SKIP" + "\n" + "DO NOT PRESS ENTER IF YOU DON\'T KNOW THE" + "\n" +"PASSWORD OR IT WILL FREEZE THE COMPUTER")
explainlabel2.place(x=50, y=800)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() 
