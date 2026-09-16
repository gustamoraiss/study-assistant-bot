import json
import os
from datetime import datetime

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

def validar_e_formatar_data(data_texto):
    try:
        data_formatada = datetime.strptime(data_texto, "%d/%m/%Y")
        return data_formatada.strftime("%Y-%m-%d")
    except ValueError:
        return None