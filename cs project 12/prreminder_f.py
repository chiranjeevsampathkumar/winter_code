import pyttsx3 as s
import datetime as dt

def reminder():
    ma = s.init()
    mC = ma.getProperty('rate')
    ma.setProperty('rate', 120)
    mvoices = ma.getProperty('voices')
    ma.setProperty('voices', mvoices[1].id)


    print('enter the following requirments to set the reminder')
    ma.say('enter the following requirments to set the reminder')
    ma.runAndWait()
    ma.say('enter the hour:')
    ma.runAndWait()
    
    c1 =  int(input('enter the hour:'))
    ma.say('enter the  minute:')
    ma.runAndWait()
    
    c2 = int(input('enter the  minute:'))
    ma.say('enter AM/PM:')
    ma.runAndWait()
    
    c3 = input('enter AM/PM:')
    ma.say('enter the statement to remind you:')
    ma.runAndWait()
    
    c4 = input('enter the statement to remind you')
    ma.say('enter how many times the statement shoud repeat:')
    ma.runAndWait()
    
    c5 = int(input('enter how many times the statement shoud repeat'))
    if c3 =='pm':
        c1=c1+12
        
    while True :
        if c1 == dt.datetime.now().hour and c2 == dt.datetime.now().minute:
            a = s.init()
            C = a.getProperty('rate')
            a.setProperty('rate', 120)
            voices = a.getProperty('voices')
            a.setProperty('voices', voices[1].id)

            while c5>0:
                c5=c5-1
                print(c4)
                b = c4
                a.say(b)
                a.runAndWait()


            break
