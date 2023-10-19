import fuckit
import requests
from bs4 import BeautifulSoup




#La clase de los minutos puede ser minutos, minuto2 = < 20 & > 10, minuto3 = 20 o mas minutos
@fuckit
def bustimes():
    page = requests.get('https://www.emtmalaga.es/emt-mobile/informacionParada.html?codParada=3325')
    soup = BeautifulSoup(page.text, 'html.parser')
    uls = soup.find_all('div', {'class':'informacion-parada'})

    for i in enumerate(uls):
        minutos = soup.find('span', {'class': 'minutos'}).getText()
    (minutos)

    for i in enumerate(uls):
        minutos1 = soup.find('span', {'class': 'minutos1'}).getText()
        minutos1.replace(" ","")
    print(minutos1)
    for i in enumerate(uls):
        minutos2 = soup.find('span', {'class': 'minutos2'}).getText()
    print(minutos2)   

    for i in enumerate(uls):
        minutos3 = soup.find('span', {'class': 'minutos3'}).getText()
    print(minutos3)

    for i in enumerate(uls):
        minutos3 = soup.find('span', {'class': 'minutos4'}).getText()
    print(minutos3)
bustimes()


		                		    