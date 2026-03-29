import re

def validar_operacao_bancaria(cod_area, prefixo, sufixo, senha, operacao):
    c1 = cod_area == "" or (len(cod_area) == 3 and cod_area.isdigit() and cod_area[0] == '0')
    c2 = len(prefixo) == 3 and prefixo.isdigit() and prefixo[0] != '0'
    c3 = len(sufixo) == 4 and sufixo.isdigit()
    c4 = len(senha) == 6 and senha.isalnum()
    c5 = operacao.lower() in ['c', 'd', 'e']

    return all([c1, c2, c3, c4, c5])