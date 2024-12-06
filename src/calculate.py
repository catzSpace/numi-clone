import os
import json
from src.data import *
from sympy import sympify

def basicOperations():

    for i in data:
            
        format = data[i]['entrada'].replace('\x08', '')
            
        try:
            
            out = sympify(format)
            data[i]['salida'] = round(out, 2)

        except:
            pass

        start = data[i]['entrada'][:3].upper() 
        end = data[i]['entrada'][-3:].upper()
        
        num = ''
        # Excluir letras
        num = data[i]['entrada'][:-3]
        num = num[3:]

    if start in codes and end in codes:

        file = open("./src/fetch/input.txt", "w")
        file.write(f'{start}{end}')
        file.close()

        # ejecutar fetch
        os.system('node src/fetch/fetch.js')

        with open('./src/fetch/data/data.json', 'r') as j:
            djson = json.load(j)
            
        change = djson['exchange_rates'][end]

        data[i]['salida'] = f'${round(float(num)*change)}'
