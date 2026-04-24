def m(i, obj):
    s = 0
    if obj is None:
        return None
    if i % 2 == 1:
        i += 1
    while i > 0:
        s += obj
        i -= 1
    return s
