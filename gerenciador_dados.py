import json
import os

def carregar_provas():
    if os.path.exists('provas.json'):
        with open ('provas.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    else:
        return []

def salvar_provas(lista_provas):
    with open ('provas.json', 'w') as arquivo:
        json.dump(lista_provas, arquivo, indent=4)