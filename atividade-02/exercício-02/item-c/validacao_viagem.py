def verificar_permissao_viagem(idade, possui_passaporte, acompanhado_responsavel):
    if not isinstance(idade, int) or idade < 0:
        return "Erro: Entrada Inválida"
    if idade >= 18:
        if possui_passaporte:
            return "Sim"  
        else:
            return "Não"  
    else:
        if possui_passaporte and acompanhado_responsavel:
            return "Sim"  
        else:
            return "Não"  
