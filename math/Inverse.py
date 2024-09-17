def egcd(a : int, b : int) -> list[int, int]:
    if a % b:
        y, x = egcd(b, a % b)
        y += -x * (a // b)
        return x, y
    else:
        return 0, 1

def inverse(a : int, b : int):
    x, y = egcd(a, b)
    if a * x + b * y != 1:
        return
    else:
        return(x if x > 0 else b + x)