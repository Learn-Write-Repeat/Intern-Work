# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:16:57 2021

@author: 91703
"""

import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image
#import anim


print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()

def record_audio(ask = False):
#user voice record
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :'+ voice_data)
        except Exception:
            print('Oops something went Wrong')
            #lee_voice('Oops something went Wrong')
        return voice_data
    

def lee_voice(audio_string):
    #Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
    
    
class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDS


    
    def __init__(self):
        
        root = Tk()
        root.title('lena')
        root.geometry('520x320')
        root.colspan="3"
        
        #img=anim.ImageLabel( ImageTk.PhotoImage(anim.ImageLabel.load('lena.jpg')))
        img = ImageTk.PhotoImage(Image.open('lena.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('JARVIS- THE VOICE ASSISTANT FOR STUDENTS')
        userFrame = LabelFrame(root, text='JARVIS', font=('Railways', 24,
        'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='#203647',
        fg='white')
        top.config(font=("Arial", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        # compFrame = LabelFrame(root, text="Lena", font=('Railways',
        #10, 'bold'))
        # compFrame.pack(fill="both", expand='yes')
        
        btn2 = Button(root, text='Close', font=('railways', 10,
        'bold'), bg='yellow', fg='blue', command=root.destroy).pack(
        fill='x', expand='no')
        lee_voice('How can i help you Group13?')
        
        
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),
        bg='red', fg='white', command=lambda:self.clicked()).pack(fill='x', expand='no')
        
        root.mainloop() 
        
    def clicked(self):
    #BUTTON CALLING
        print("working...")
        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'who are you' in voice_data:
            lee_voice('My name is Lena ')
        if 'search' in voice_data:
            search = record_audio('What do you want to search for ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            lee_voice('Here is what i found' + search)
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is location' + location)
        if 'what is the time' in voice_data:
            lee_voice("Sir the time is :" + ctime())
        if 'exit' in voice_data:
            lee_voice('Thanks have a good day ')
            
        if 'who' in voice_data:
            lee_voice("I was built by batch No 13,Praveen,sanjay,amrez,satish")
            
            
        if "good bye" in voice_data or "ok bye" in voice_data or "stop" in voice_data:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            



        if 'wikipedia' in voice_data:
            speak('Searching Wikipedia...')
            voice_data =voice_data.replace("wikipedia", "")
            results = wikipedia.summary(voice_data, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in voice_data:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening Youtube")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in voice_data:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
            
        elif 'open college website' in voice_data or 'open gokaraju website' in voice_data or 'open college' in voice_data:
            webbrowser.open_new_tab("http://www.griet.ac.in/")
            print("Opening College Portal")
            speak("College Portal is open now")
            print("Griet portal is open now")
            time.sleep(5)

        elif 'open gmail' in voice_data:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in voice_data:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in voice_data:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in voice_data or 'what can you do' in voice_data:
            speak('I am jarvis version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in voice_data or "who created you" in voice_data or "who discovered you" in voice_data:
            speak("I was built by Batch No 13")
            print("I was built by Batch No 13")

        elif "stack overflow" in voice_data:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in voice_data:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

       
        elif 'search'  in voice_data:
            voice_data = voice_data.replace("search", "")
            webbrowser.open_new_tab(voice_data)
            time.sleep(5)

        elif 'ask' in voice_data:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
            
            
        elif 'hello' in voice_data:
            
            speak("Opening Github")
            webbrowser.open_new_tab("https://eventsindia.net")


        elif "log off" in voice_data or "sign out" in voice_data:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
        
            exit()
    
    
    
    
    
    
if __name__== '__main__':
    widget = Widget()
time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)

speaker.runAndWait()
    
    
    
    
    
    
    
    
    
    
    