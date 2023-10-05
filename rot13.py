import string

# Attempt to recreate the ROT13 cipher in Python

def rot13encrypt(plaintext, length, letters, numbers):
    cipher_text = ''

    # For loop to encrypt your message into rot13
    for index in range(length):
        character = plaintext[index]

        if character == ' ':
            cipher_text += ' '

        if character in numbers:
            cipher_text += character

        if character in letters:
            try:
                cipher = letters.index(character) + 13
                cipher_text += letters[cipher]
            except IndexError:
                cipher = cipher - 26
                cipher_text += letters[cipher]

    return cipher_text


if __name__ == '__main__':
    plaintext = input('Enter a message to encrypt: ')
    plaintext = plaintext.lower()
    length = len(plaintext)

    letters = string.ascii_letters
    letters = list(letters[:26])
    numbers = list(string.digits)
    
    cipher_text = rot13encrypt(plaintext, length, letters, numbers)
    print(cipher_text.capitalize())