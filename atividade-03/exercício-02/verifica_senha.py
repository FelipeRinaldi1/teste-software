import re

def verificar_senha_forte(senha):
    if not isinstance(senha, str):
        return False

    c1 = len(senha) >= 8
    c2 = re.search(r'[A-Z]', senha) is not None
    c3 = re.search(r'[a-z]', senha) is not None
    c4 = re.search(r'[0-9]', senha) is not None
    c5 = re.search(r'[@#$%]', senha) is not None

    return all([c1, c2, c3, c4, c5])