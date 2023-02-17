class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def caesar_cipher(self, text):
        result = ""

        for char in text:
            if char.isalpha():
                num = ord(char.upper()) - ord("A")
                num = (num + self.shift) % 26

                result += chr(num + ord("A"))
            else:
                result += char

        return result

    def caesar_decipher(self, text):
        result = ""

        for char in text:
            if char.isalpha():
                num = ord(char.upper()) - ord("A")
                num = (num - self.shift) % 26

                result += chr(num + ord("A"))
            else:
                result += char

        return result

