import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import subprocess
from playsound import playsound

#Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):  
    engine.say(audio)
    engine.runAndWait()
    

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am virtual assistent jarvis")
    elif hour>=12 and hour<16:
        speak("good afternoon sir i am virtual assistent jarvis") 
    elif hour>=16 and hour<21:
        speak("good eveninig sir i am virtual assistent jarvis") 
    else:
        speak("good night sir i am virtual assistent jarvis")  

#now convert audio to text
# 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.....") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                
        speak("error.....")
        print("Network connection error") 
        return "none"
    return text

                             
if __name__ == "__main__":
    wish()
    
    while True:
        
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  

        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 

        #elif 'open browser' in query:
        #    speak("opening browser")
        #    subprocess.call("C://Program Files//Mozilla Firefox//firefox.exe")

        elif 'open notepad' in query:
            subprocess.call("notepad.exe")
            speak("Closed notepad") 
            

            
        #elif 'music from pc' in query or "play music" in query:
        #    speak("ok i am playing music")
        #    playsound('D://Besabriyaan_320_Kbps.mp3')
        #    nextm = takecom()
        #    if 'next music' in nextm:
        #        playsound("D://Humraah - Malang 128 kbps.mp3")
        #   # if 'stop' in nextm:
                #break
            

        #elif 'video from pc' in query or "open video player" in query or "open media player":
         #   subprocess.call('"C://Program Files (x86)//Windows Media Player//wmplayer.exe"')
          #  speak("closed media player")
            

            

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s') 

        elif 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  

        elif 'who make you' in query or 'who created you' in query or 'who develop you' in query:
            ans_m = " For your information Karamveer Rajput Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Karamveer Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)
    
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        #elif query == 'continue':
        #    continue 

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
        #else:
         #   temp = query.replace(' ','+')
          #  g_url="https://www.google.com/search?q="    
           # res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            #print(res_g)
            #speak(res_g)
            #webbrowser.open(g_url+temp)                       