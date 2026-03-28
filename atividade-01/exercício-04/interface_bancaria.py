def processar_operacao(cod_area, prefixo, sufixo, senha, comando):
    if cod_area != "":
        if not (len(cod_area) == 3 and cod_area.isdigit() and cod_area.startswith('0')):
            return "Erro: Código de área inválido"

    if not (len(prefixo) == 3 and prefixo.isdigit() and not prefixo.startswith('0')):
        return "Erro: Prefixo inválido"

    if not (len(sufixo) == 4 and sufixo.isdigit()):
        return "Erro: Sufixo inválido"

    if not (len(senha) == 6 and senha.isalnum()):
        return "Erro: Senha inválida"

    comandos_validos = {'c': 'Cheque', 'd': 'Depósito', 'e': 'Extrato'}
    cmd = str(comando).lower()
    if cmd not in comandos_validos:
        return "Erro: Comando inválido"

    return f"Operação {comandos_validos[cmd]} autorizada"