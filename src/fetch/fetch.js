const fs = require('fs') 


//TODO 
/* funcion para extraer la base y el target de un archivo txt */

let base = ""
let target = ""
let response

fs.readFile('./src/fetch/input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error al leer el archivo:', err);
    } else {
        console.log('Contenido del archivo:', data);
        base = data.slice(0, 3);
    }
});

let b = "USD"


// const urls = `https://exchange-rates.abstractapi.com/v1/live/?api_key=f768b79aa08e48daade82fb9f2c8fab7&base=${base}&target=${target}`
const url = `https://exchange-rates.abstractapi.com/v1/live/?api_key=&base=${b}`


async function getData() {

  const res = await fetch(url, {  
    method: "GET",
  })

  const data = await res.json()
  console.log(data)

  // sobreescribir archivo json con los nuevos datos
  const jsonData = JSON.stringify(data, null, 2);
  fs.writeFile("./src/fetch/data/data.json", jsonData, 'utf8', (err) => {
    if (err){
      console.log('error :C ', err)
    }
  })

}

getData(url)



// console.log('working from javascript')
