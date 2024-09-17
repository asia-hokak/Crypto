def legendre_symbol(a : int, p : int):
    legendre = pow(a, (p - 1) // 2, p)
    return -1 if legendre == p - 1 else legendre