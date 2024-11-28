import speech_recognition as sr
import pyttsx3 as s
r = sr.Recognizer()                                                            #perfectly works                        
with sr.Microphone() as source:                                                                       
    print("now you can Speak:")                                                                                   
    audi = r.listen(source)
    
    
try:
    print("You said: " ,r.recognize_google(audi))
   
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
