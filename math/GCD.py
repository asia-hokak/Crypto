def gcd(a : int, b : int):
    return gcd(b, a % b) if a % b else b