import json
import re
import time
import numpy as np
from pyscript import document
from pyodide.ffi import create_proxy

with open("dados.json", encoding="utf-8") as f:
    frutas = json.load(f)["frutas"]

def norma_euclidiana(vetor):
    return float(np.linalg.norm(np.array(vetor)))

def renderizar(lista):
    grid = document.getElementById("grid")
    grid.innerHTML = ""
    for fruta in lista:

        norma = norma_euclidiana(fruta["embedding"])

        card = document.createElement("div")
        card.className = "card"

        imagem = document.createElement("img")
        imagem.src = "src/assets/" + fruta["imagem"]
        imagem.alt = fruta["nome"]

        nome = document.createElement("h3")
        nome.textContent = fruta["nome"]

        preco = document.createElement("p")
        preco.className = "preco"
        preco.textContent = f'R$ {fruta["preco"]:.2f}'

        norma_texto = document.createElement("p")
        norma_texto.className = "norma"
        norma_texto.textContent = f"‖v‖ = {norma:.3f}"

        card.appendChild(imagem)
        card.appendChild(nome)
        card.appendChild(preco)
        card.appendChild(norma_texto)

        grid.appendChild(card)