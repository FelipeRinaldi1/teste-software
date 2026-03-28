def verificar_permissao_viagem(idade, possui_passaporte, acompanhado_responsavel):
    if not isinstance(idade, int) or idade < 0:
        return "Erro: Entrada Inválida"
    
    if idade >= 18:
        if possui_passaporte:
            return "Sim"  # T1 e T2
        else:
            return "Não"  # T3 e T4
            
    else:
        if possui_passaporte and acompanhado_responsavel:
            return "Sim"  # T5
        else:
            return "Não"  # T6, T7 e T8