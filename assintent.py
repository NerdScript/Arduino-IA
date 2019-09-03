# -*- coding: utf-8 -*-

import subprocess as s
import speech_recognition as sr
from os import system
from gtts import gTTS

def get_microphone():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio, language='pt-BR')
        return frase
        
def p2s(text, language="pt", name="voice.mp3"):
    DIR = "/var/tmp/" + name
    sv = gTTS(text, lang=language)
    sv.save(DIR)
    s.call(['mplayer', DIR])
    system("rm " + DIR)
