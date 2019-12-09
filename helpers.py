'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return None


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def encrypt(N, e, plaintext, key):
    key_list = list(key.keys())
    val_list = list(key.values())

    cipher = ""
    for i in range(0, len(plaintext)):
        if plaintext[i] == " ":
            cipher += " "
        else:
            num = int(key[plaintext[i]])
            num_encrypted = (num ** e) % N
            cipher += key_list[val_list.index(str(num_encrypted))]

    return cipher


def decrypt(N, e, cipher_text, key):
    key_list = list(key.keys())
    val_list = list(key.values())

    # Get the private key
    factors = prime_factors(N)
    p = factors[0]
    q = factors[1]

    alt_mod = (p - 1) * (q - 1)

    # Get the inverse of e with the alt_mod
    e_inv = multiplicative_inverse(e, alt_mod)

    plain_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i] == " ":
            plain_text += " "

        else:
            num = int(key[cipher_text[i]])
            num_decrypted = (num ** e_inv) % N
            plain_text += key_list[val_list.index(str(num_decrypted))]

    return plain_text

