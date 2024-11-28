import pyttsx3 as s
import pyaudio as py
import wave
import speech_recognition as sr
import pyttsx3 as s
ra = sr.Recognizer()
ma = s.init()
mC = ma.getProperty('rate')
ma.setProperty('rate', 120)
mvoices = ma.getProperty('voices')
ma.setProperty('voices', mvoices[1].id)



                                                                                        # working perfectly
def notes_taker():
    fpb=3200
    f=py.paInt16
    c=1
    r=16000
    p=py.PyAudio()
    st=p.open(format=f,channels=c,rate=r,input=True,frames_per_buffer=fpb)
    ma.say('enter the time duration of the lecture in seconds')
    ma.runAndWait()
    x=int(input('enter the time duration of the lecture in sec'))
    ma.say('enter the audio file name')
    ma.runAndWait()
    y=input('enter the audio file name')
    ma.say('start the lecture')
    ma.runAndWait()
    print('start the lecture')
    sec=x
    fr=[ ]
    for i in range(0,int(r/fpb*sec)):
        da=st.read(fpb)
        fr.append(da)
    st.stop_stream()
    st.close()
    p.terminate()

    o=wave.open(y+'.wav','wb')
    o.setnchannels(c)
    o.setsampwidth(p.get_sample_size(f))
    o.setframerate(r)
    o.writeframes(b"".join(fr))
    o.close()
    print('the lecture is stored successfully')
    ma.say('the lecture is stored successfully')
    ma.runAndWait()
    ma.say('enter the text file name:')
    ma.runAndWait()
    f=input('enter the text file name:')
    tp=sr.AudioFile(y+'.wav')
    with tp as source:
        audio = ra.record(source)
    try:
        s = ra.recognize_google(audio)
        print("Text: "+s)
        
        with open(f+'.txt','w') as tf:
            tf.write(s)

        print('the notes is stored successfully ')
            
        
    except Exception as e:
        print("Exception: "+str(e))



