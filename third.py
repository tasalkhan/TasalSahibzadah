# #Encryption
plaintext="how are you"
plaintext=''.join(plaintext.split(' '))

key=2
ciphertext=[''] * key
print(len(ciphertext))
for colm in range (key):
    index = colm
    while index < len(plaintext):
        ciphertext[colm]=ciphertext[colm] + plaintext[index]
        index=index + key
print(f"encrypted message is {ciphertext}")

## decryption

ciphertext =('helldf dfjsl')
ciphertext = ''.join(ciphertext.split(' '))
key = 2
rows = 3
plaintext = [""] *rows
for i in range(rows):
    index = i
    while index <len(ciphertext):
        plaintext[i] = plaintext[i] + ciphertext[index]
        index = index + rows
print(f"plain text is : {plaintext}")

