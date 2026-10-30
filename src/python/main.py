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
def validar_entrada(texto):
    texto = texto.strip()
    if not texto:
        return False, "Digite o nome de uma fruta."
    if len(texto) > 30:
        return False, "Máximo de 30 caracteres."
    if not re.fullmatch(r"[A-Za-zÀ-ÿ0-9 ]+", texto):
        return False, "Caracteres inválidos."
    return True, texto
def buscar(event):
    texto = document.getElementById("busca").value
    msg = document.getElementById("mensagem")
    if not texto.strip():
        msg.innerText = ""
        renderizar(frutas)
        atualizar_telemetria()
        return
    ok, resultado = validar_entrada(texto)
    if not ok:
        telemetria["bloqueadas"] += 1
        msg.innerText = resultado
    else:
        telemetria["buscas"] += 1
        msg.innerText = ""
        filtradas = [
            fruta for fruta in frutas
            if resultado.lower() in fruta["nome"].lower()
        ]
        renderizar(filtradas)
        if not filtradas:
            msg.innerText = "Nenhuma fruta encontrada."
    atualizar_telemetria()