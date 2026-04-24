def calcular_frete_gratis(mesma_cidade, quantidade, valor_total):
    if mesma_cidade:
        return True
    return quantidade > 3 and valor_total >= 200.0
