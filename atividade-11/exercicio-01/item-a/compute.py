def compute(x, y):
    if y == 0:
        return "y is zero"
    elif x == 0:
        return "x is zero"
    else:
        results = []
        for i in range(1, x + 1):
            if i % y == 0:
                results.append(i)
        return results
