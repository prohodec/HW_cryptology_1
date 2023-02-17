import string


class LinearCipher:
    def __init__(self, a, alphabet=string.ascii_uppercase):
        self.a = a
        self.alphabet = alphabet
        self.alph_len = len(self.alphabet)

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        ciphertext = ""
        for char in plaintext:
            if char not in self.alphabet:
                ciphertext += char
            else:
                idx = self.alphabet.index(char)
                idx_cipher = (self.a * idx) % self.alph_len
                ciphertext += self.alphabet[idx_cipher]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        plaintext = ""
        for char in ciphertext:
            if char not in self.alphabet:
                plaintext += char
            else:
                idx_cipher = self.alphabet.index(char)
                idx = (self.mod_inv() * idx_cipher) % self.alph_len
                plaintext += self.alphabet[idx]
        return plaintext

    def mod_inv(self):
        a = self.a % self.alph_len
        for x in range(1, self.alph_len):
            if (a * x) % self.alph_len == 1:
                return x
        raise Exception("Modular inverse does not exist")

