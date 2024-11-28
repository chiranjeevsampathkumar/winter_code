import pyttsx3 as s
import mysql.connector as m
import random as r                           #for both audio and text this is enough as it doesnot contain any inputs.
                                                         # works perfectly
def joke():
    h=m.connect(host='localhost',user='root',password='Sch00l@',database='chiranjeevpro')
    b=r.randint(1,20)
    c=h.cursor()
    x='select jokes from joke where slno="{}"'.format(b)
    c.execute(x)
    y=c.fetchone()
    print(y[0])
    a = s.init()
    C = a.getProperty('rate')
    a.setProperty('rate', 140)
    voices = a.getProperty('voices')
    a.setProperty('voices', voices[1].id)
    a.say(y[0])
    a.runAndWait()
    h.close()
