import datetime as dt
import pyttsx3 as s
import speech_recognition as sr
import pyaudio
def dtf():
    try:
        with sr.Microphone() as source:
            
            d = dt.datetime.now()
            v = str(d)

            a = s.init()
            C = a.getProperty('rate')
            a.setProperty('rate', 120)
            voices = a.getProperty('voices')
            a.setProperty('voices', voices[1].id)

            rx = sr.Recognizer()    
            g = 'enter what you want(date/time/date and time)'
            print(g)
            a.say(g)
            a.runAndWait()
            
            ip=rx.listen(source)

            if rx.recognize_google(ip, language ='en-IN', show_all=True)== 'time':
                a1 = v[11:19:1]
                a_ = v[11:13]
                a2 = int(a_)
                if a2 > 12:
                    a3 = a2 % 12
                    a4 = v[14:16]
                    a5 = v[18:20]
                else:
                    a3 = a2
                    a4 = v[14:16]
                    a5 = v[18:20]
                print(a3, 'hours', a4, 'minuts', a5, 'seconds')
                b = a3, 'hours', a4, 'minuts', a5, 'seconds'
                a.say(b)
                a.runAndWait()



            elif  'date' in rx.recognize_google(ip):           
                b_ = dt.date.today()
                b1 = v[0:4]
                b2 = v[5:7]
                b3 = v[8:10]
                print('today the date is :', b_)
                b =( 'today the date is :', b1, b2, b3)
                a.say(b)
                a.runAndWait()



            elif  'date and time' in rx.recognize_google(ip) or 'both' in rx.recognize_google(ip):          
                b_ = dt.date.today()
                b1 = v[0:4]
                b2 = v[5:7]
                b3 = v[8:10]
                a1 = v[11:19:1]
                a_ = v[11:13]
                a2 = int(a_)
                if a2 > 12:
                    a3 = a2 % 12
                    a4 = v[14:16]
                    a5 = v[18:20]
                else:
                    a3 = a2
                    a4 = v[14:16]
                    a5 = v[18:20]
                print('today the date is :', b_, 'and now the time is:', a3, 'hours', a4, 'minuts', a5, 'seconds')
                b = 'today the date is :', b1, b2, b3, 'and now the time is:', a3, 'hours', a4, 'minuts', a5, 'seconds'
                a.say(b)
                a.runAndWait()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



