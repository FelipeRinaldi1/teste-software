def verificar_contratacao(idade):
    if not isinstance(idade, int) or idade < 0 or idade >= 99:
        return "Entrada Inválida"
    if 0 <= idade < 16:
        return "Não empregar"
    elif 16 <= idade < 18:
        return "Pode ser empregado tempo parcial"
    elif 18 <= idade < 55:
        return "Pode ser empregado tempo integral"
    elif 55 <= idade < 99:
        return "Não empregar"
    return "Entrada Inválida"
