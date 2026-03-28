def verificar_contratacao(idade):
    if not isinstance(idade, int) or idade < 0 or idade > 99:
        return "Entrada Inválida"
    
    if 0 <= idade <= 15:
        return "Não empregar"
    elif 16 <= idade <= 17:
        return "Pode ser empregado tempo parcial"
    elif 18 <= idade <= 54:
        return "Pode ser empregado tempo integral"
    elif 55 <= idade <= 99:
        return "Não empregar"
    
    return "Entrada Inválida"