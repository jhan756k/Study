from tkinter import *
from tkinter import ttk
from datetime import *
from pynput.keyboard import Key, Controller
import os, ctypes, subprocess, cv2
import tkinter.font as font

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

root = Tk()
root.title("Lock")
root.geometry("1536x960")
root.attributes('-topmost',True)     
root.overrideredirect(True)

# -----------------------------------------------------------------------------------------------
'''
# 세션생성, 로그인
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('jhan756k@gmail.com', 'vyuqyrvfpgvffovc')

# 제목, 본문 작성
msg = MIMEMultipart()
msg['Subject'] = 'SUCCESSFUL LOGIN'
msg.attach(MIMEText('본문', 'plain'))

# 메일 전송
s.sendmail("보내는 메일계정", "받는 메일계정", msg.as_string())
s.quit()

# 파일첨부 (파일 미첨부시 생략가능)
attachment = open('파일명', 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)
'''


loginlog = open("log.txt","a+")

myFont = font.Font(size=30)

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
    output = subprocess.check_output(call).decode('EUC-KR')
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
        
        keyboardlock()
        nowfail = datetime.now()
        loginlog.write(nowfail.strftime('%Y/%m/%d %I:%M:%S:%p') + "    failed to login" + "\n")
        
        video = cv2.VideoCapture(0) 
        check, frame = video.read()
        showPic = cv2.imwrite("failed.jpg",frame)
        video.release()

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

        # 세션생성, 로그인
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('jhan756k@gmail.com', 'vyuqyrvfpgvffovc')

        # 제목, 본문 작성   
        msg = MIMEMultipart()
        msg['Subject'] = 'SUCCESSFUL LOGIN'
        msg.attach(MIMEText(nowpass.strftime('%Y/%m/%d %I:%M:%S:%p'), 'plain'))

        # 메일 전송
        s.sendmail("jhan756k@gmail.com", "jhan756kor@gmail.com", msg.as_string())
        s.quit()
        
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

    # 세션생성, 로그인
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('jhan756k@gmail.com', 'vyuqyrvfpgvffovc')

    # 제목, 본문 작성   
    msg = MIMEMultipart()
    msg['Subject'] = 'LOGIN SKIPPED'
    msg.attach(MIMEText(nowskip.strftime('%Y/%m/%d %I:%M:%S:%p'), 'plain'))

    # 파일첨부 (파일 미첨부시 생략가능)
    attachment = open('unauthorized.jpg', 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= unauthorized.jpg")
    msg.attach(part)

    # 메일 전송
    s.sendmail("jhan756k@gmail.com", "jhan756kor@gmail.com", msg.as_string())
    s.quit()

    skipbutton['state'] = NORMAL
    ctypes.windll.user32.LockWorkStation()                          
    
# -----------------------------------------------------------------------------------------------

passwordbox = ttk.Entry(root, show = '*', font="Lato 50", width=10)
passwordbox.place(x=550, y=300)

enterbutton = ttk.Button(root, text="Enter", width=10, command=passwordentered)
enterbutton.grid(ipady=24, padx= 1050, pady=300)

skipbutton = ttk.Button(root, text="SKIP", command=passwordskip)
skipbutton.place(x = 1050, y = 550, height = 70, width = 80)

explainlabel1 = ttk.Label(root, font="Lato 70", text="TYPE IN THE PASSWORD")
explainlabel1.place(x=200, y=20)

explainlabel2 = ttk.Label(root, font="Lato 50", text="PRESS SKIP" + "\n" + "DO NOT PRESS ENTER IF YOU DON\'T KNOW "+ "\n"  +"THE PASSWORD OR IT WILL FREEZE THE" + "\n" + "COMPUTER")
explainlabel2.place(x=20, y=680)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() 
