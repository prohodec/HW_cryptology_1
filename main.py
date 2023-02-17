from caesar_cipher import CaesarCipher
from affine_cipher import AffineCipher
from linear_cipher import LinearCipher

if __name__ == "__main__":
    while True:
        choice = input("Which cipher do you want to check:\n1 - caesar\n2 - affin\n3 - linear\n0 - exit\n:::")

        if choice == "1":
            shift = int(input("Enter shift for caesar cipher: "))
            word = input("Enter word to encrypt: ")
            caesar_ciph = CaesarCipher(shift)
            enc_word = caesar_ciph.caesar_cipher(word)

            print("encrypted word:", enc_word)
            print("decrypted word:", caesar_ciph.caesar_decipher(enc_word))
        elif choice == "2":
            a = int(input("Enter 1st key: "))
            b = int(input("Enter 2nd key: "))
            word = input("Enter word to encrypt: ")
            affine_ciph = AffineCipher(a, b)
            enc_word = affine_ciph.encrypt(word)

            print("encrypted word:", enc_word)
            print("decrypted word:", affine_ciph.decrypt(enc_word))
        elif choice == "3":
            a = int(input("Enter a key: "))
            word = input("Enter word to encrypt: ")
            linear_ciph = LinearCipher(a)
            enc_word = linear_ciph.encrypt(word)

            print("encrypted word:", enc_word)
            print("decrypted word:", linear_ciph.decrypt(enc_word))
        elif choice == "0":
            break

