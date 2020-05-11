import requests 
import json 


accuweatherAPIKey = 'Seu token'


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

    def pegarclimaAgora(codigoLocal, nomeLocal):
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



    