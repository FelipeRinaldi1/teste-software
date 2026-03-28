import string

def verificar_senha(senha):
    PALAVRAS_RESTRITAS = ["teste", "funcional", "unidade", "integracao"]
    
    if not isinstance(senha, str):
        return "Entrada Inválida"
    
    if len(senha) < 6 or len(senha) > 10:
        return "Erro: Tamanho inválido (deve ser 6-10)"
    
    primeiro = senha[0]
    permitidos_inicio = string.ascii_letters + string.digits + "?"
    if primeiro not in permitidos_inicio:
        return "Erro: Primeiro caractere inválido"
    
    if any(ord(c) < 32 or ord(c) == 127 for c in senha):
        return "Erro: Contém caracteres de controle"
        
    if senha.lower() in PALAVRAS_RESTRITAS:
        return "Erro: Senha consta na lista de termos restritos"
        
    return "Senha Válida"