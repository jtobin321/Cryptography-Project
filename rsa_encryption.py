from helpers import encrypt, decrypt


N, e = 33, 7

key = {
        '!': '0', '?': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8',
        'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17',
        'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'a': '26',
        '@': '27', '$': '28', '#': '29', '%': '30', '&': '31', '*': '32', 'z': '33', '(': '34'
    }

plain_text = "jack mohammad amr judy"
print("Plain Text: " + plain_text)
cipher = encrypt(N, e, plain_text, key)
print("Cipher Text: " + cipher)

decrypted_text = decrypt(N, e, cipher, key)
print("Decrypted Text: " + decrypted_text)


