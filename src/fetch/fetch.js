const fs = require('fs') 


//TODO 
/* funcion para extraer la base y el target de un archivo txt */

let base = "USD"
let target = "BTC"
let response


// const urls = `https://exchange-rates.abstractapi.com/v1/live/?api_key=f768b79aa08e48daade82fb9f2c8fab7&base=${base}&target=${target}`
const url = `https://exchange-rates.abstractapi.com/v1/live/?api_key=f768b79aa08e48daade82fb9f2c8fab7&base=${base}`


async function getData() {

  const res = await fetch(url, {  
    method: "GET",
    withCredentials: true,
    headers: {
      "X-Auth-Token": "",
      "Content-Type": "application/json"
    }
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

getData(url)



// console.log('working from javascript')
