def contains(x, a, b):
    res = []
    if a <= b:
        if a <= x and x <= b:
            res.append("x is an interior point")
        if x <= a or x >= b:
            res.append("x is outside the interval")
    else:
        res.append("the interval is empty")
    return res
