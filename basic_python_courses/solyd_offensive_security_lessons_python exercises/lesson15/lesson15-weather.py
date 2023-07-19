import requests
import json
import datetime
data=None
date=datetime.datetime.now().date()

while True:
    try:
        req=requests.get(f'https://api.open-meteo.com/v1/forecast?latitude=-28.9357&longitude=-49.4954&hourly=temperature_2m&current_weather=true&start_date={date}&end_date={date}')
        data=json.loads(req.text)
    except Exception as error:
        print(error)
    
    print('\n')
    print('Temperatura em Araranguá: '+str(data['current_weather']['temperature'])+'°C')
    print('Velocidade do vento em Araranguá: '+str(data['current_weather']['windspeed'])+' km/h')

    while True:
        aks=input('\nDid you want to consult again? [y/n]')
        print('\n')
        if aks=='y':break
        elif aks=='n':exit()
        else:print('error');continue
    
    continue
 