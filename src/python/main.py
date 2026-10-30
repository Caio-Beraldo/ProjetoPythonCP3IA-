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