import cv2
import numpy as np
import dlib
#from playsound import playsound
import pyttsx3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def email():
    fromaddr = "drowsy.detection21@gmail.com"
    toaddr = "drowsy.detection21@gmail.com"
   
    # instance of MIMEMultipart
    msg = MIMEMultipart()
  
    # storing the senders email address  
    msg['From'] = fromaddr
  
    # storing the receivers email address 
    msg['To'] = toaddr
  
    # storing the subject 
    msg['Subject'] = "Subject of the Mail"
  
    # string to store the body of the mail
    #body = "Body_of_the_mail"
    body = "The drowsy picture"
  
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
    # open the file to be sent 
    filename = "opencv.jpg"
    attachment = open("F:/Major/opencv.jpg", "rb")
  
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
  
    # To change the payload into encoded form
    p.set_payload((attachment).read())
  
    # encode into base64
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
  
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
    # start TLS for security
    s.starttls()
  
    # Authentication
    s.login(fromaddr, "drowsy@1234")
  
    # Converts the Multipart msg into a string
    text = msg.as_string()
  
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
  
    # terminating the session
    s.quit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def calculate_EAR(eye):
    V1 = np.linalg.norm(np.array(eye[1])-np.array(eye[5]))
    V2 = np.linalg.norm(np.array(eye[2])-np.array(eye[4]))
    H = np.linalg.norm(np.array(eye[0])-np.array(eye[3]))
    eye_aspect_ratio = (V1+V2)/(2.0*H)
    return eye_aspect_ratio
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("F:/Major/shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        face_landmarks = predictor(gray, face)
        leftEye = []
        rightEye = []

        for n in range(36,42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x,y))
            next_point = n+1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(255,0,0),1)


        for n in range(42,48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x,y))
            next_point = n+1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(255,0,0),1)
            


        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)


        EAR = (left_ear + right_ear)/2
        EAR = round(EAR,2)
        if EAR<0.20:
            cv2.putText(frame,"DROWSY",(20,100),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),4)
            cv2.putText(frame,"Are you sleepy?",(20,400),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
            speak('Driver you are sleeping please wake up')
            print('Please Wake Up')
            cv2.imwrite('opencv'+'.jpg',frame)
            email()
            print('DROWSY')
        print(EAR)


    cv2.imshow("Drowsy Detection", frame)
    if  cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
