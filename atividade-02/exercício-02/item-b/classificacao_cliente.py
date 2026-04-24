def verificar_vip(tempo_conta_anos, saldo_conta):
    if not isinstance(tempo_conta_anos, (int, float)) or not isinstance(saldo_conta, (int, float)):
        return "Erro: Entrada Inválida"
    if tempo_conta_anos < 0 or saldo_conta < 0:
        return "Erro: Valores Negativos"

    if tempo_conta_anos >= 2 and saldo_conta >= 2000:
        return "Sim"
    return "Não"
