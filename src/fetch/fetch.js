const fs = require('fs') 


//TODO 
/* funcion para extraer la base y el target de un archivo txt */

async function getData(base) {

  let url = `https://exchange-rates.abstractapi.com/v1/live/?api_key=&base=${base}`
  

  const res = await fetch(url, {  
    method: "GET"
  })

  const data = await res.json()

  // sobreescribir archivo json con los nuevos datos
  const jsonData = JSON.stringify(data, null, 2);
  fs.writeFile("./src/fetch/data/data.json", jsonData, 'utf8', (err) => {
    if (err){
      console.log('error :C ', err)
    }
  })

}


// leer datos de conversion
fs.readFile('./src/fetch/input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error al leer el archivo:', err);
    } else {
        let target = ''
        let base = ''

        console.log(data)
        
        let = base = data.slice(0, 3);

        getData(base)
    }
});
