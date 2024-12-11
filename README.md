# Numi Clone


Un clon menos desarrollado de la calculadora interpretativa [Numi](https://github.com/nikolaeu/numi) hecho con python
y javascript

---

![Screenshot_2024-11-11-19-08-32_1920x1080](https://github.com/user-attachments/assets/896f97f3-07d0-4f41-8e36-0cb6cc00df7b)

---

# Uso: 

instalar las dependencias tkinter, sympy

```py
pip install tkinter sympy
```

Cambio monetario (Sintaxis)

```
[START] [VALUE] [CHANGE]
```

ejemplo

```py
btc 23 usd # salida: 23 btc -> usd
```


---

agregar la api key de acceso de la api Exchanges-Rates de [abstractApi](https://www.abstractapi.com/a/home?utm_source=google&utm_medium=cpc&utm_campaign=branded&utm_term=abstract%20api&gad_source=1&gclid=EAIaIQobChMItcegm5bSiQMVfqFaBR2qEzE8EAAYASAAEgK-E_D_BwE)
y ubicarla en el archivo fetch.js en el siguiente fragmento.

```js
const url = `https://exchange-rates.abstractapi.com/v1/live/?api_key=&base=${base}`
```

ejecutar y/o compilar a conveniencia

```
python main.py
```

