from tkinter import *
from tkinter import ttk
from datetime import *
import os, ctypes, cv2, smtplib
import tkinter.font as font
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

root = Tk()
root.title("Lock")

x = root.winfo_screenwidth()
y = root.winfo_screenheight()
screen_resolution = str(x)+'x'+str(y)
root.geometry(screen_resolution)

root.attributes('-topmost',True)     
root.overrideredirect(True)
# -----------------------------------------------------------------------------------------------

loginlog = open("log.txt","a+")

myFont = font.Font(size=30)

def on_closing():
    pass

def send_email(type, time):
    # type   1-> successful   2-> fail    3-> skip

    # 세션생성, 로그인
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('jhan756k@gmail.com', 'vyuqyrvfpgvffovc')

    # 제목, 본문 작성 
    if type == 1:
        msg = MIMEMultipart()
        msg['Subject'] = 'SUCCESSFUL LOGIN'
        msg.attach(MIMEText(time))

        # 파일첨부 (파일 미첨부시 생략가능)
        attachment = open('success.jpg', 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= success.jpg")
        msg.attach(part)

    elif type == 2:

        msg = MIMEMultipart()
        msg['Subject'] = 'LOGIN FAILED'
        msg.attach(MIMEText(time))

        attachment = open('failed.jpg', 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= failed.jpg")
        msg.attach(part)

    elif type == 3:

        msg = MIMEMultipart()
        msg['Subject'] = 'LOGIN SKIPPED'
        msg.attach(MIMEText(time))

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

def passwordentered():
    if passwordbox.get() != "stupidmonkey":

        enterbutton['state'] = DISABLED
        
        nowfail = datetime.now()
        loginlog.write(nowfail.strftime('%Y/%m/%d %I:%M:%S %p') + "    failed to login" + "\n")
        
        video = cv2.VideoCapture(0) 
        check, frame = video.read()
        showPic = cv2.imwrite("failed.jpg",frame) 
        video.release()

        send_email(2, nowfail.strftime('%Y/%m/%d %I:%M:%S %p'), 'plain')

        enterbutton['state'] = NORMAL

        ctypes.windll.user32.LockWorkStation()    

    else:
        enterbutton['state'] = DISABLED
    
        nowpass = datetime.now()
        loginlog.write(nowpass.strftime('%Y/%m/%d %I:%M:%S %p') + "\n")
        loginlog.close()
        
        video = cv2.VideoCapture(0) 
        check, frame = video.read()
        showPic = cv2.imwrite("success.jpg",frame)
        video.release()

        send_email(1, nowpass.strftime('%Y/%m/%d %I:%M:%S %p'))
        print()
        enterbutton['state'] = NORMAL

        exit()

def passwordskip():
    skipbutton['state'] = DISABLED
    nowskip = datetime.now()
    loginlog.write(nowskip.strftime('%Y/%m/%d %I:%M:%S %p') + "    unauthorized" + "\n")
    loginlog.flush()
    os.fsync(loginlog.fileno())
    video = cv2.VideoCapture(0) 
    check, frame = video.read()
    showPic = cv2.imwrite("unauthorized.jpg",frame)
    video.release()

    send_email(3, nowskip.strftime('%Y/%m/%d %I:%M:%S %p'))

    skipbutton['state'] = NORMAL
    ctypes.windll.user32.LockWorkStation()                          


# -----------------------------------------------------------------------------------------------

passwordbox = ttk.Entry(root, show = '*', font="Lato 50", width=10)
passwordbox.place(x=550, y=300)

passwordbox.focus()

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