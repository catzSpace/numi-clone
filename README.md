# Numi Clone


Un clon menos desarrollado de la calculadora interpretativa [Numi](https://github.com/nikolaeu/numi) hecho con python
y javascript

---

![Screenshot_2024-11-10-10-40-36_1920x1080](https://github.com/user-attachments/assets/666a6f6a-d68a-405e-a2f1-64023e5ad71b)

---

![Screenshot_2024-11-10-10-40-57_1920x1080](https://github.com/user-attachments/assets/cf96777e-21bf-4b1e-a5cb-3b67d39a2427)

---

uso: 

instalar las dependencias tkinter, sympy

```
pip install tkinter sympy
```

agregar la el token de acceso de la api de [abstractApi](https://www.abstractapi.com/a/home?utm_source=google&utm_medium=cpc&utm_campaign=branded&utm_term=abstract%20api&gad_source=1&gclid=EAIaIQobChMItcegm5bSiQMVfqFaBR2qEzE8EAAYASAAEgK-E_D_BwE)
y ubicarla en el archivo fetch.js en el siguiente fragmento.

```js
const res = await fetch(url, {  
    method: "GET",
    withCredentials: true,
    headers: {
      "X-Auth-Token": "",
      "Content-Type": "application/json"
    }
  })
```

ejecutar y/o compilar a conveniencia

```
python main.py
```

