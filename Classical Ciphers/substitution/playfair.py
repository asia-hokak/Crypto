def gen_key(key:int):
    key = key.replace('J', 'I')
    matrix = []
    used = set()
    
    for ch in key.upper():
        if ch not in used and ch.isalpha():
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix:list, ch:str):
    for y in range(5):
        for x in range(5):
            if matrix[y][x] == ch:
                return y, x
    return None

def preprocess_text(text:str):
    text = text.replace('J', 'I').upper().replace(' ', '')
    processed = ""
    
    i = 0
    while i < len(text):
        ch = text[i]
        ch2 = text[i+1] if i+1 < len(text) else 'X'

        if ch == ch2:
            processed += ch
            processed += 'X'
            i += 1
        else:
            processed += ch
            processed += ch2
            i += 2

    return processed

def encrypt(plaintext:str, key:str):
    matrix = gen_key(key)
    plaintext = preprocess_text(plaintext)

    cipher = []
    for i in range(0, len(plaintext), 2):
        ch1, ch2 = plaintext[i], plaintext[i+1]
        y1, x1 = find_pos(matrix, ch1)
        y2, x2 = find_pos(matrix, ch2)

        if y1 == y2:
            cipher += matrix[y1][(x1 + 1) % 5]
            cipher += matrix[y2][(x2 + 1) % 5]
        elif x1 == x2:
            cipher += matrix[(y1 + 1) % 5][x1]
            cipher += matrix[(y2 + 1) % 5][x2]
        else:
            cipher += matrix[y1][x2]
            cipher += matrix[y2][x1]
        cipher += ' '
    return ''.join(cipher)

def decrypt(cipher, key):
    matrix = gen_key(key)
    plaintext = []
    cipher = cipher.replace(' ', '')
    
    for i in range(0, len(cipher), 2):
        y1, x1 = find_pos(matrix, cipher[i])
        y2, x2 = find_pos(matrix, cipher[i+1])

        if y1 == y2:
            plaintext += matrix[y1][(x1 - 1) % 5]
            plaintext += matrix[y2][(x2 - 1) % 5]
        elif x1 == x2:
            plaintext += matrix[(y1 - 1) % 5][x1]
            plaintext += matrix[(y2 - 1) % 5][x2]
        else:
            plaintext += matrix[y1][x2]
            plaintext += matrix[y2][x1]
        plaintext += ' '

    return ''.join(plaintext)

if __name__ == '__main__':
    cipher = encrypt('HI DE TH EG OL DI NT HE TR EX ES TU MP', 'PLAYFAIR EXAMPLE')
    plaintext = decrypt(cipher, 'PLAYFAIR EXAMPLE')
    print(cipher)
    print(plaintext)
