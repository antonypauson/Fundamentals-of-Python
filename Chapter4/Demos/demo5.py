#encryption using Caesar's Cipher
#using only small letters of english alphabet
plainText = input("Enter the text:")
msg_distance = int(input("Message Distance:"))
cipherCode = ""

for char in plainText:
    ascii_code = ord(char)
    char_code = ascii_code + msg_distance
    if char_code > ord('z'):
        char_code = ord('a') + msg_distance - (ord('z') - ascii_code + 1) #if the ciphar exceeds z ie the end of alphabet
    cipherCode += chr(char_code)

print(cipherCode)
