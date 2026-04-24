def calcular_e1(c1, c2):
    if not isinstance(c1, bool) or not isinstance(c2, bool):
        return None

    return c1 or not c2
