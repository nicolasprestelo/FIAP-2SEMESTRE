const express = require('express')
const cors = require('cors')

const app = express()

const PORT = 3001

app.use(express.json())
app.use(cors())

const precos = {
    bicicleta: '0.75',
    carro: '0.25',
    drone: '1',
    moto: '0.65',
    aviao: '3.65',
    jato: '2',
    foguete: '5.25',

}

app.post('/calcularfrete', (req, res) => {
    const { distancia, tipoTransporte } = req.body;

    if (distancia === undefined || tipoTransporte === undefined) {
        return res.status(400).json({ error: 'Distância e tipo de transporte são obrigatórios' })
    }

    const precoPorKm = precos[tipoTransporte.toLowerCase()];

    if (precoPorKm === undefined) {
        return res.status(400).json({ error: 'Tipo de transporte inválido' })
    }

    let valorTotal = distancia * precoPorKm

    if (distancia > 50) {
        valorTotal = valorTotal + (valorTotal * 0.2)
    }

    res.json({ valorTotal: valorTotal.toFixed(2) })
})
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`)
})