#imports necesarios, fechas, audio recognition, tts audio voz, controlador web, wikipedia api, wolframalpha api.
from datetime import datetime
import speech_recognition as sr
import pyttsx3      #import TTS Audio
import webbrowser
import wikipedia    #import Wikipedia Search
import wolframalpha
import pywhatkit as pwt
from playsound import playsound #Import play music
import pygame          
import pygame.camera #IMPORTS CAMARA
import requests     #Import Request Url para scrapeo
from bs4 import BeautifulSoup   #Import Scrapeo
import fuckit #No mostrar errores cambio de clase minutos bus
import python_weather #libreria del tiempo
import asyncio #libreria del tiempo asyncrona
import os #ni puta idea pero es de la libreria del tiempo¿¿¿

pygame.camera.init() 

wikipedia.set_lang('es')
#inicialización de TTS voz
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id) #voice onfiguration
activationword = 'bmo' #activation word

#futbol = r"C:\Users\luisl\OneDrive\Escritorio\bmo\futbol.mp3"
#Metodo TTS
def speak(text, rate = 120):
    engine.setProperty('rate', rate) #Rate propiedad que cambia la velocidad del tts
    engine.say(text)
    engine.runAndWait()

#Metodo escucha de comandos
def parseCommand():
    listener = sr.Recognizer()

    print('Escuchando comando')
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        print('Reconociendo voz')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'El reconocimiento es: {query}')

    except Exception as exception:
        print('Error de reconocimiento')
        speak('Error')
        print(exception)
        return None
    
    return query

#############
##Funciones##
#############

def tiempoFarenheits():
    ciudad = "Spain-Malaga"

    async def getweather():
        # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            # fetch a weather forecast from a city
            weather = await client.get(ciudad)
        
            Fahrenheit = weather.current.temperature
            celsius = (weather.current.temperature - 32)*5/9

                
            # returns the current day's forecast temperature (int)
            print("Hace una tempertatura de:", Fahrenheit, "Grados Farenheits en Málaga")  
            print("Hace una tempertatura de:", celsius, "Grados Farenheits en Málaga")  
     


        if __name__ == '__main__':
        # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
        # for more details
            if os.name == 'nt':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        asyncio.run(getweather())



def sacarFoto():
    # make the list of all available cameras 
    camlist = pygame.camera.list_cameras() 
    
    # if camera is detected or not 
    if camlist: 
    
        # initializing the cam variable with default camera 
        cam = pygame.camera.Camera(camlist[0], (640, 480)) 
    
        # opening the camera 
        cam.start() 
    
        # capturing the single image 
        image = cam.get_image() 
    
        # saving the image 
        pygame.image.save(image, "filename.jpg") 
    
    # if camera is not detected the moving to else part 
    else: 
        print("No camera on current device") 



@fuckit
def bus33():
    page = requests.get('https://www.emtmalaga.es/emt-mobile/informacionParada.html?codParada=3325')
    soup = BeautifulSoup(page.text, 'html.parser')
    uls = soup.find_all('div', {'class':'informacion-parada'})

    for i in enumerate(uls):
        minutos = soup.find('span', {'class': 'minutos'}).getText()
    print(minutos)
    speak(minutos)
    for i in enumerate(uls):
        minutos1 = soup.find('span', {'class': 'minutos1'}).getText()
    print(minutos1)
    speak(minutos1)
    for i in enumerate(uls):
        minutos2 = soup.find('span', {'class': 'minutos2'}).getText()
    print(minutos2)   
    speak(minutos2)
    for i in enumerate(uls):
        minutos3 = soup.find('span', {'class': 'minutos3'}).getText()
    print(minutos3)

    for i in enumerate(uls):
        minutos3 = soup.find('span', {'class': 'minutos4'}).getText()
    print(minutos3)


#Metodo bucle main
if __name__ == '__main__':
    playsound(r'futbol.mp3')

    while True:
        #Instrucciones parseadas y separadas
        query = parseCommand().lower().split()

        #
        if query[0] == activationword:
            query.pop(0)
            #Querrys  Música
            if query[0] == 'play':
                    if 'boa' in query:
                        speak ('playing duvet')
                        #pwt.playonyt("Duvet by Boa")
                        playsound(r'duvet.mp3')
                    if 'love' in query:
                        playsound(r'cupid.mp3')
                    else:
                        query.pop(0)
                        speech = ' '.join(query)
                        speak(speech)
            #Querry Sacar Foto
            if query[0] == 'take':
                    if 'photo' in query:
                        sacarFoto()
                    else:
                        query.pop(0)
                        speech = ' '.join(query)
                        speak(speech)
            #Querry Buscar en Wikipedia
            if query[0] == 'wikipedia':
                    if 'search' in query:
                        speak('searching in wikipedia')
                        resultado = wikipedia.summary("Absolute zero", sentences = 2)
                        speak(resultado)
                        print(resultado)
                    else:
                        query.pop(0)
                        speech = ' '.join(query)
                        speak(speech)

            #Querry Bus manuela  
            if query[0] == 'bus':
                    if 'time' in query:
                         bus33()
                    else:
                        query.pop(0)
                        speech = ' '.join(query)
                        speak(speech)

            #Query Temperatura en málaga
            if query[0] == 'temperature':
                    if 'farenheits' in query:
                         tiempoFarenheits()
                         #print("Hace una tempertatura de:", fahrenheit, "Grados Farenheits en Málaga")  

                    if 'celsius':
                         tiempoFarenheits()
                         #speak("Hace una tempertatura de:", celsius, "Grados Farenheits en Málaga")
                    else:
                        query.pop(0)
                        speech = ' '.join(query)
                        speak(speech)
            
             #Query precipitaciones en málaga
            if query[0] == 'is':
                    if 'rain' in query:
                         print("En proceso")
                    else:
                        query.pop(0)
                        speech = ' '.join(query)
                        speak(speech)


        if query[0] == activationword:
            parseCommand()
        else:
            parseCommand()