import requests 
import json 
#biblioteca para trabalhar com dias da semana.
from datetime import date

accuweatherAPIKey = 'Seu token'

dias_semana= ['Domingo', 'Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sabado']

class clima():
    def pegarCoordenadas():
        r = requests.get('http://geoplugin.net/json.gp')
        if (r.status_code != 200):
            print('Não foi possivel obter a localização.')
            return None
        else:
            try:
                localizacao = json.loads(r.text)
                coordenadas = {}
                coordenadas['lat'] = localizacao['geoplugin_latitude']
                coordenadas['lon'] = localizacao['geoplugin_longitude']
                return coordenadas
            except:
                return None


    def pegarCodigoLocal(lat, lon):
        locationAPIIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey="+ accuweatherAPIKey +"&q="+lat+"%2C"+lon+"&language=pt-br"
        r = requests.get(locationAPIIUrl)
        if(r.status_code != 200):
            print('Não foi possivel obter a localização.')
            return None
        else:
            try:
                locationResponse = json.loads(r.text)
                infolocal = {}
                infolocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " +locationResponse['AdministrativeArea']['LocalizedName'] +". " + locationResponse['Country']['LocalizedName']
                infolocal['codigoLocal'] = locationResponse['Key']
                return infolocal
            except:
                return None

    def pegarTempoAgora(codigoLocal, nomeLocal):
        CurremtConditionsAPIUrl =  "http://dataservice.accuweather.com/currentconditions/v1/"+codigoLocal+'?apikey='+accuweatherAPIKey+'&language=pt-br'
        r = requests.get(CurremtConditionsAPIUrl)
        if(r.status_code != 200):
            print('Não foi possivel obter a Temperatura.')
            return None
        else:
            try:
                CurrentConditionsResponse = json.loads(r.text)
                infoClima = {}
                infoClima['textoClima'] = CurrentConditionsResponse[0]['WeatherText']
                infoClima['temperatura'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
                infoClima['nomeLocal']  = nomeLocal
                return infoClima
            except:
                return None

    def pegarPrevisao5Dias(codigoLocal):
       DailyAPIUrl =  "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"+codigoLocal+'?apikey='+accuweatherAPIKey+'&language=pt-br&metric=true'
       r = requests.get(DailyAPIUrl)
       if(r.status_code != 200):
           print('Não foi possivel obter a Temperatura.')
           return None
       else:

           try:
               DailyResponse = json.loads(r.text)
               infoClima5 = []
               for dia in DailyResponse['DailyForecasts']:
                   climaDia={}
                   climaDia['max'] = dia['Temperature']['Maximum']['Value']
                   climaDia['min'] = dia['Temperature']['Minimum']['Value']
                   climaDia['clima'] = dia['Day']['IconPhrase']
                   diaSemana = date.fromtimestamp(dia['EpochDate']).strftime('%w')
                   climaDia['dia'] = dias_semana[int(diaSemana)]
                   infoClima5.append(climaDia)
               return infoClima5
           except:
               return None

    ##Incio do programa 

coordenadas = clima.pegarCoordenadas()
try:
    local = clima.pegarCodigoLocal(coordenadas['lat'], coordenadas['lon'])
    climaAtual = clima.pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])
    print ('Clima atual em: ' + climaAtual['nomeLocal'])
    print ( climaAtual['textoClima'])
    print ('Temperatura: ' + str(climaAtual['temperatura'])+ "\xb0"+"C")
    print('\nClima para hoje e para os proximos dias: \n')
    previsao5dias = clima.pegarPrevisao5Dias(local['codigoLocal'])
    for dia in previsao5dias:
        print(dia['dia'])
        print('Minima: ' + str(dia['min']) + '\xb0'+'C')
        print('Maxima: ' + str(dia['max']) + '\xb0'+'C')
        print('Clima: ' + dia['clima'])
        print('-----------------------------------------')
except:
    print("Erro ao  executar , favor falar com o desenvolvedor")

  