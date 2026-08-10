/* setTimeout( () => {
    console.log("Processo Assíncrono")
}, 1500); 

console.log("1 - Início do processo");

setTimeout(() => {
    console.log("2 - Meio do processo")
}, 0);

console.log("3 - Fim do processo");

const btn = document.getElementById("botao");
const popup = document.getElementById("popup");

btn.addEventListener("click", () => {
    popup.classList.add("popup-active");

    setTimeout(() => {
        popup.classList.remove("popup-active")
    }, 2500)
})

 for (let letra of "olá") {
    setTimeout(() => { 
        console.log(letra)
    }, 1000)
}
for (let letra of "mundo") {
    setTimeout(() => {
        console.log(letra)
    }, 2000)
} 
 setInterval( () => {
    console.log("Tic")
}, 1000); 

let counter = 0
const interval = setInterval(() => {
    counter++
    console.log("Counter: ", counter);

    if (counter >= 5) {
        clearInterval(interval);
        console.log("O intervalo foi removido")
    }
}, 1000); */

const eventoFuturo = (res) => {
    return new Promise((resolve, reject) => {

        /*         if(res === true) {
                    resolve("Promessa Resolvida")
                } else{
                    reject("Promessa Rejeitada")
                } */

        setTimeout(() => {
            res ? resolve("Promessa Reslvida") : reject("Promessa Rejeitada")
        }, 2000)
    })
}
// console.log(eventoFuturo());
//console.log(eventoFuturo(true));
//console.log(eventoFuturo(false));

eventoFuturo(true)
    .then((response) => {console.log(response)})
    .catch((error) => { console.log(error) })
    .finally(() => {console.log("Fim do processo")})

eventoFuturo(false)
    .then((response) => { console.log(response) })
    .catch((error) => {console.log(error)})