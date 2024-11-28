import playsound
import datetime as dt
import pyttsx3 as s

   
                                                                       #perfectly works
na = s.init()
nC = na.getProperty('rate')
na.setProperty('rate', 120)
nvoices = na.getProperty('voices')
na.setProperty('voices', nvoices[1].id)
def alarm():
    print('enter the following requirments to set the alarm')
    na.say('enter the following requirments to set the alarm')
    na.runAndWait()
    
    na.say('enter the hour:')
    na.runAndWait()
    c1 = int(input('enter the hour:'))
    na.say('enter the  minute:')
    na.runAndWait()
    c2 = int(input('enter the  minute:'))
    na.say('enter AM/PM:')
    na.runAndWait()
    c3 = input('enter AM/PM:')
    if c3.lower() == 'pm':
        c1 = c1 + 12
    while True:
        if c1 == dt.datetime.now().hour and c2 == dt.datetime.now().minute:
            print('alarm music is playing')
            playsound.playsound('alarmsong.mp3')
            
            
            break
    

