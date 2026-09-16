import json
import os

def carregar_provas():
    if os.path.exists('provas.json'):
        with open ('provas.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    else:
        return []