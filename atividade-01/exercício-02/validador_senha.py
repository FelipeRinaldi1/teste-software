import re

def verificar_senha_forte(senha):
    if not isinstance(senha, str):
        return "Entrada Inválida"
    
    if len(senha) < 8:
        return "Senha Fraca: Mínimo 8 caracteres"
    
    if not any(c.isupper() for c in senha):
        return "Senha Fraca: Falta letra maiúscula"
        
    if not any(c.islower() for c in senha):
        return "Senha Fraca: Falta letra minúscula"
        
    if not any(c.isdigit() for c in senha):
        return "Senha Fraca: Falta número"
        
    if not re.search(r"[@#$%!^&*(),.?\":{}|<>]", senha):
        return "Senha Fraca: Falta símbolo"
        
    return "Senha Forte"

