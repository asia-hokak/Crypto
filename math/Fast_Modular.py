def fast_modular(a : int, b : int, c : int):
    num = 1
    while b > 0:
        if b & 1:
            num = num * a % c
        b >>= 1
        a **= 2
    return num