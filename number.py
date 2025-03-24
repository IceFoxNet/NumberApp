def calc(n: int):
    if n == 1: return n
    return n * calc(n-1)