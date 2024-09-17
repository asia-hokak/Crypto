def legendre_symbol(a : int, p : int):
    legendre = pow(a, (p - 1) // 2, p)
    return -1 if legendre == p - 1 else legendre

def tonelli_shanks(a, p):
    if legendre_symbol(a, p) != 1:
        return None

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1:
        return pow(a, (p + 1) // 4, p)

    for z in range(2, p):
        if legendre_symbol(z, p) == -1:
            break

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while t != 1:
        for i in range(1, m):
            if pow(t, 2 ** i, p) == 1:
                break

        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p

    return r