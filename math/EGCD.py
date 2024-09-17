def egcd(a : int, b : int) -> list[int, int]:
    if a % b:
        y, x = egcd(b, a % b)
        y += -x * (a // b)
        return x, y
    else:
        return 0, 1