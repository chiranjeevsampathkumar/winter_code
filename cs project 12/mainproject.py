import speech_recognition as sr
import pyttsx3 as s
import playsound
import datetime as dt
import mysql.connector as m
import random as r

import pralarm_f as z1
import prreminder_f as z2
import prdt_f as z3
import prjoke_f as z4
import prnotestaker as z5
import prschedulereminder_f as z6
import Tprdt_f as tz3


ma = s.init()
mC = ma.getProperty('rate')
ma.setProperty('rate', 120)
mvoices = ma.getProperty('voices')
ma.setProperty('voices', mvoices[1].id)

try:
    with sr.Microphone() as source:
        rx = sr.Recognizer()           
        print('you can give the input to this project by voice as well as text .which way do you prefer to select the task:')
        ma.say('you can give the input to this project by voice as well as text .')
        ma.say('which way do you prefer  to select the task')
        ma.runAndWait()
        inp= rx.listen(source)
        
        if 'voice' in rx.recognize_google(inp):                                                         
            print('you can do the following tasks with this program just by saying the name of that task')
            ma.say("you can do the following tasks with this program just by saying the name of that task")
            print('THEY ARE')
            ma.say('they are')
            print('1) alarm')
            ma.say( '1) alarm')
            print('2) reminder')
            ma.say('2) reminder')
            print('3) joke')
            ma.say('3) joke')
            print('4) date and time')
            ma.say('4) date and time')
            print('5) record lectures')
            ma.say('5) record lectures')
            print('6) set schedule in preyer')
            ma.say('6) set schedule in preyer')
            print('now you can say the name of the task:')
            ma.say('now you can say the name of the task:')
            ma.runAndWait()
            audio =sr.listensource()
            try:
                if 'alarm' in rx.recognize_google(audio):
                    z1.alarm()
                elif 'reminder' in rx.recognize_google(audio):
                    z2.reminder()
                elif 'time' in rx.recognize_google(audio) or 'date' in rx.recognize_google(audio):
                    z3.dtx()
                elif 'joke' in rx.recognize_google(audio):
                    z4.joke()
                elif 'lecture' in rx.recognize_google(audio) or 'record' in rx.recognize_google(audio) :
                    z5.notes_taker()
                elif 'schedule' in rx.recognize_google(audio):
                    z6.prschedulereminder_f()
                    
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

        elif 'text' in rx.recognize_google(inp):
            try:
                with sr.Microphone() as source:
                    rx = sr.Recognizer()           
                    print('you can do the following tasks with this program just by entering the name of that task')
                    ma.say("you can do the following tasks with this program just by entering the name of that task")
                    print('THEY ARE')
                    ma.say('they are')
                    print('1) alarm')
                    ma.say( '1) alarm')
                    print('2) reminder')
                    ma.say('2) reminder')
                    print('3) joke')
                    ma.say('3) joke')
                    print('4) date and time')
                    ma.say('4) date and time')
                    print('5) record lectures')
                    ma.say('5) record lectures')
                    print('6) set schedule in preyer')
                    ma.say('6) set schedule in preyer')
                    ma.say('now you can enter the name of the task:')
                    ma.runAndWait()
                    X1=input('enter the name of the task:')
                    if 'alarm'==X1:
                        z1.alarm()
                    elif 'reminder'==X1:
                        z2.reminder()
                    elif 'time'==X1 or 'date'==X1:
                        tz3.dtx()
                    elif 'joke' in X1:
                        z4.joke()
                    elif 'lecture' in X1 or 'record' in X1 :
                        z5.notes_taker()
                    elif 'schedule' in X1:
                        z6.ax()
                         
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

                
                
