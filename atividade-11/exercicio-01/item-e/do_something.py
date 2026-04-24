def f(vec): return "f"
def g(vec): return "g"
def ff(vec): return "ff"

def do_something(x, vec):
    y = 0
    if x > 0:
        y = 1
    status = ""
    if x > 100 and y != 0:
        status = "less than 100"
    else:
        y = vec[0]
    if y == 1:
        res = f(vec)
    elif y == 2:
        res = g(vec)
    else:
        res = None
    final = ff(vec)
    return (status, res, final)
