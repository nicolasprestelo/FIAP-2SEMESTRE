/* //Armazenamentos de locais.

/* let mensagem = localStorage.getItem("Boas-vindas");
console.log(mensagem);
let tipo = localStorage.getItem("Válido");
console.log(tipo);

let lista = sessionStorage.getItem("Selecionados").split(",");
console.log(lista); 

localStorage.removeItem("Boas-vindas");
localStorage.clear();


const produto1 = {
    id: 2,
    produto: "Arroz"
};
localStorage.setItem("ChaveProduto", produto1);

Converter Objeto para formado de Json Para conseguir capturar valor.

const produto2 = {
    id: 2,
    produto: "Arroz"
};
const emJSON = JSON.stringify(produto2); //Converte o produto2 (objeto) em string
localStorage.setItem("ChaveProduto", emJSON);


Volta de texto para Objeto Interável.

let produtos = localStorage.getItem("ChaveProduto");
const emObjeto = JSON.parse(produtos);
console.log(emObjeto); */


const listaProdutos = [
    { id: 1, produto: "Arroz", preco: 125 },
    { id: 2, produto: "Macarrão", preco: 70 },
    { id: 3, produto: "Pão", preco: 50 },
    { id: 4, produto: "Pudim", preco: 100 },
];

//Armazena no local storage
const armazenarLocal = (chave, valor) => {
    localStorage.setItem(chave, valor)
};
/* for (const produto of listaProdutos) {
    armazenarLocal(produto.id, JSON.stringify(produto));
} */

armazenarLocal("listaProdutos", JSON.stringify(listaProdutos));

//Obter a lista armazenada
class Produto {   //A classe serve como um molde para criar objetos que representam produtos
    constructor(obj) {
        this.nome = obj.produto.toUpperCase();
        this.preco = parseFloat(obj.preco);
    }
    somaICSM() {
        this.preco = this.preco * 1.21;
    }
}

const armazenados = JSON.parse(localStorage.getItem("listaProdutos"))
const produtos = [];
for (const objeto of armazenados) {
    produtos.push(new Produto(objeto))
}
for (const produto of produtos) {
    produto.somaICSM();
}

console.log(produtos);