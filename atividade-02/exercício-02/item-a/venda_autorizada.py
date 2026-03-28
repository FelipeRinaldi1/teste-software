def verificar_permissao_venda(idade):
    if not isinstance(idade, int) or idade < 0 or idade > 120:
        return "Entrada Inválida"
    
    if idade >= 18:
        return "Sim"
    else:
        return "Não"