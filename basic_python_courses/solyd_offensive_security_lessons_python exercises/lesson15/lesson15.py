import requests
import json
from time import sleep

dados=None

while True:
    try:
        req=requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        dados=json.loads(req.text)
    except Exception as error:
        print(error)

    print('ALTO: '+dados['USDBRL']['high']+'R$'+' , '+'BAIXO: '+dados['USDBRL']['low']+'R$')
    sleep(10)