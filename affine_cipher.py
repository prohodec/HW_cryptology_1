import string


class AffineCipher:
    def __init__(self, a, b, alphabet=string.ascii_uppercase):
        self.a = a
        self.b = b
        self.alphabet = alphabet
        self.alph_len = len(self.alphabet)

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.upper() in self.alphabet:
                char_index = self.alphabet.index(char.upper())
                encrypted_index = (self.a * char_index + self.b) % self.alph_len
                encrypted_message += self.alphabet[encrypted_index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        a_inverse = self.mod_inv()
        for char in message:
            if char.upper() in self.alphabet:
                char_index = self.alphabet.index(char.upper())
                decrypted_index = a_inverse * (char_index - self.b) % self.alph_len
                decrypted_message += self.alphabet[decrypted_index]
            else:
                decrypted_message += char
        return decrypted_message

    def mod_inv(self):
        a = self.a % self.alph_len
        for x in range(1, self.alph_len):
            if (a * x) % self.alph_len == 1:
                return x
        raise Exception("Modular inverse does not exist")


if __name__ == "__main__":
    while True:
        a = int(input("Enter 1st key(0 - exit): "))
        if a == 0:
            break
        b = int(input("Enter 2nd key: "))
        word = input("Enter word: ")

        cipher = AffineCipher(a, b)
        encrypted = cipher.encrypt(word)
        print('зашифрований:', encrypted)

        print('розшифрований:', cipher.decrypt(encrypted))
