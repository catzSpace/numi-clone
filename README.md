# Numi Clone


Un clon menos desarrollado de la calculadora interpretativa [Numi](https://github.com/nikolaeu/numi) hecho con python
y javascript

---

![Screenshot_2024-11-10-10-40-36_1920x1080](https://github.com/user-attachments/assets/6d7098e9-35e4-457e-b0fc-4b833130c10d)


---

![Screenshot_2024-11-10-10-40-57_1920x1080](https://github.com/user-attachments/assets/76767f30-cc10-4083-9764-abd45bfb53dc)

---

# Uso: 

instalar las dependencias tkinter, sympy

```
pip install tkinter sympy
```

agregar la api key de acceso de la api Exchanges-Rates de [abstractApi](https://www.abstractapi.com/a/home?utm_source=google&utm_medium=cpc&utm_campaign=branded&utm_term=abstract%20api&gad_source=1&gclid=EAIaIQobChMItcegm5bSiQMVfqFaBR2qEzE8EAAYASAAEgK-E_D_BwE)
y ubicarla en el archivo fetch.js en el siguiente fragmento.

```js
const url = `https://exchange-rates.abstractapi.com/v1/live/?api_key=&base=${b}`
```

ejecutar y/o compilar a conveniencia

```
python main.py
```

