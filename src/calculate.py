from src.data import *
from sympy import sympify

def basicOperations():

    for i in data:
        if data[i]['entrada'][0].isnumeric():
            
            #start = data[i]['entrada'].find('\x08')
            #data[i]['entrada'].replace(data[i]['entrada'][start],'',1)
            
            format = data[i]['entrada'].replace('\x08', '')
            
            try:
                print(format)
                out = sympify(format)
                #print(out)
                data[i]['salida'] = round(out, 2)
                print(data)
            except:
                pass

        for code in codes:
            if data[i]['entrada'][:3].upper() == code:
                print('eureca')

        else:
            pass
            #data[i]['salida'] = '\n'


#basicOperations()
