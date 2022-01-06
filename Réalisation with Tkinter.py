import cv2
import numpy as np
from simple_facerec import SimpleFacerec
import sys


import time

import sqlite3

from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime

root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Reconnaissance Facial')
frame.config(background='light pink')
label = Label(frame, text="Reconnaissance Facial",bg='light pink',font=('Times 35 bold'))
label.pack(side=TOP)
filename = ImageTk.PhotoImage(Image.open("C:\\miniprojet\\demo4.jpg"))
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)


def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Mayur Kadam\n2. Abhishek Ezhava \n3. Rajendra Patil \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   cap = cv2.VideoCapture(0)

   sfr = SimpleFacerec()
   sfr.load_encoding_images("images/")

   while True:
    _,frame = cap.read()


    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)


    key = cv2.waitKey(1)
    if key == 27:
        break
    
   cap.release()
   cv2.destroyAllWindows()
      

def webdet():
  cap = cv2.VideoCapture(0)
  sfr = SimpleFacerec()
  sfr.load_encoding_images("images/")

  while True:
    _,frame = cap.read()


    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    print("press q to capture", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        cv2.imwrite("capture image opencv.jpg", frame)
        print("image captured")
        break
    if key == 27: 
        break
    
  cap.release()
  cv2.destroyAllWindows()

def send():
  dateTimeNow = datetime.datetime.now()

  message = MIMEMultipart()
  message['from'] = "ayabenkhedher84@gmail.com" 
  message['to'] = "daoudwissal2000@gmail.com "
  Password = "Wissalpqt1"
  message['Subject'] = "Face recognition app"
  body = "Welcome to my Face recognition app  " + str(dateTimeNow)
    
  image_open = open('capture image opencv.jpg' ,'rb').read()

  message.attach(MIMEText(body, 'html'))
  message.attach(MIMEImage(image_open, 'jpg', name= 'aya.jpg'))
 


  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(message['From'], Password)
  server.sendmail(message['From'], message['To'], message.as_string())
  server.quit()

  os.system('face recognition')
  cv2.destroyAllWindows()

def data():
    try:
        sqliteConnection = sqlite3.connect('SQLite_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        cursor.execute("SELECT * from Person")
        record = cursor.fetchall()
        profil = 0
        for row in record:
            First_name = row[0]
            Last_name = row[1]
            image = row[2]
            mail = row[3]
            print("First_name =", row[0], "Last_name =", row[1], "img = " , row[2], "mail =" , row[3])
            print("Storing Person image on disk \n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")





   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Detect',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Capture',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=send,text='Send Email',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=data,text='Read From Database',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but6=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but6.place(x=210,y=478)



root.mainloop()
