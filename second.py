import string

alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"


def decrypt():
    encrypted_message = input("Enter the message you would like to decrypt: ")
    print()
    key = 3

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c


    print("Your decrypted message is:\n")
    print(decrypted_message)


decrypt()

