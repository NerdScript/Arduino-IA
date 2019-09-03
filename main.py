# Porta que custumo utilizar: /dev/ttyACM0 ou /dev/ttyACM1

import speech_recognition as sr
from pyfirmata import Arduino, util
from assintent import get_microphone, p2s
from time import sleep

placa = Arduino("/dev/ttyACM0")
led = placa.digital[4]


while True:
    voz = get_microphone().lower()
    try:
        if voz == "ligar led":
            p2s("ligando led...")
            led.write(1)
        if voz == "desligar led":
            p2s("desligando led... ")
            led.write(0)
    except sr.UnknownValueError():
        p2s("Não entendi mestre?")
