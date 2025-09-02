# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-2: What happens if the user enters a number/symbol/space?

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    len_alphabet = len(alphabet)

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            ending_position = position + shift_amount
            if ending_position % len_alphabet > 0:
                encrypted_text += alphabet[ending_position % len_alphabet]
            elif ending_position % len_alphabet != 0:
                encrypted_text += alphabet[ending_position]
        else:
            encrypted_text += letter
    print(f"Your encoded text is: {encrypted_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    len_alphabet = len(alphabet)

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            ending_position = position - shift_amount
            if ending_position < 0:
                backward_position = abs(ending_position)
                decrypted_text += alphabet[len_alphabet - backward_position]
            elif ending_position > 0:
                decrypted_text += alphabet[ending_position]
        else:
            decrypted_text += letter

    print(f"Your decoded text is: {decrypted_text}")


def caesar(user_direction):
    if user_direction == "encode":
        encrypt(text, shift)
    elif user_direction == "decode":
        decrypt(text, shift)
    else:
        pass


# TODO-3: Can you figure out a way to restart the cipher program?
game_over = False
while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(logo)
    caesar(direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no: '").lower()
    if again == "no":
        game_over = True

input("\n\nType 'ENTER' to finish")
