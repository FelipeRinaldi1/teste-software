import re

def validar_senha(senha):
    dicionario = ["teste", "qa", "bug", "software"]
    if not isinstance(senha, str):
        return False

    c1 = 6 <= len(senha) <= 10
    primeiro = senha[0] if len(senha) > 0 else ""
    c2 = primeiro.isalnum() or primeiro == "?"
    c3 = all(ord(char) >= 32 for char in senha)
    c4 = senha.lower() not in dicionario

    return all([c1, c2, c3, c4])
