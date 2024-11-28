
import mysql.connector as my
import pyttsx3 as s

ma = s.init()
mC = ma.getProperty('rate')
ma.setProperty('rate', 120)
mvoices = ma.getProperty('voices')
ma.setProperty('voices', mvoices[1].id)


    
def swrite():
    a=my.connect(host='localhost',user='root',password='Sch00l@',database='chiranjeevpro')
    c=a.cursor()
    ma.say('enter the schedule:')
    ma.runAndWait()
    s=input('enter the schedule:')
    ma.say('enter the date :')
    ma.runAndWait()
    d=input('enter the date :')
    q=" insert into sreminder values('{}','{}')".format(d,s)
    c.execute(q)
    a.commit()
    a.close()

def sread():
    a=my.connect(host='localhost',user='root',password='Sch00l@',database='chiranjeevpro')
    c=a.cursor()
    ma.say('enter the date at which you want to know the schedule in yyyy-mm-dd formate')
    ma.runAndWait()
    x=input('enter the date at which you want to know the schedule in yyyy-mm-dd formate:')
    q="select schedule from sreminder where rdate='{}'".format(x)
    c.execute(q)
    k=c.fetchone()
    print(k[0])
    a.close()

def ax():
    x=input('do you want to set the schedule / see the schedule')
    if 'see' in x:
        sread()
    elif 'set' in x:
        swrite()

   


