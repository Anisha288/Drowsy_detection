Objective :

•	Driver drowsiness detection is a car safety technology which helps to save the life of the driver by preventing accidents when the driver is getting drowsy.
•	The main objective is to first design a system to detect driver’s drowsiness by	continuously monitoring retina of the eye.
•	The system works in spite of driver wearing spectacles and in various lighting	conditions.
•	To alert the driver on the detection of drowsiness by using buzzer or alarm.

Packages :

Numpy : NumPy stands for Numerical Python.NumPy is a Python library used for working with arrays. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

Opencv : OpenCV is a huge open-source library for computer vision, machine learning, and image processing. It can process images and videos to identify objects, faces, or even the handwriting of a human.

Pyaudio : PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms.

Smtplib : smtplib creates a Simple Mail Transfer Protocol client session object which is used to send emails to any valid email id on the internet. Different websites use different port numbers.

Pyttsx3: pyttsx3 is a text-to-speech conversion library in Python. it is a very easy to use tool which converts the entered text into speech.
Dlib: The computer engineer researching how they identify the face of a human in an image. For this, we need to identify first where the human face is located in the whole image. The face detector is the method which locates the face of a human in an image and returns as a bounding box or rectangle box values.
![image](https://user-images.githubusercontent.com/87173661/126486822-4804decc-6d73-4421-b5ef-74f6b5361058.png)

Implementation :

The system starts with opening of the front camera of the device. The real-time video of the person infront of the camera is divided into frames. The first motive is to detect the face in the frame. The entire face is marked by 68 points of Dlib 68 points Face landmark Detection. The main focus is on the eyes. Each eye is represented by 6 points. The Euclidean distance is to be calculated to find out the Eye Aspect Ratio(EAR).Based on the EAR it is decided whether the eyes are closed or not.Text message written as “Drowsy” and “Are you sleepy?” is shown on the screen.If the person is in a drowsy state then the corresponding image of the drowsiness is sent to the mail id of the company where he works. Along with these an alert sound will be played to notify that the driver that he has fallen asleep.

