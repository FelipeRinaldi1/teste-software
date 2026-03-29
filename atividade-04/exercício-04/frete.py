def calcular_frete_gratis(mesma_cidade, quantidade, valor_total):
    c1 = mesma_cidade
    c2 = quantidade > 3
    c3 = valor_total >= 200.0
    
    return c1 or (c2 and c3)