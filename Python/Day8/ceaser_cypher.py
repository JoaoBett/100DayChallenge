end_ceaser = "yes"
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']


while end_ceaser == "yes":
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift%26

    def encrypt(plain_text, shift_ammount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_ammount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The enconded text is {cipher_text}")
        
    def decrypt(cipher_text, shift_ammount):
        plain_text=""
        for letter in cipher_text:
            position=alphabet.index(letter)
            new_position=position-shift_ammount
            plain_text += alphabet[new_position]
        print(f"The decrypted text is {plain_text}")

    if direction == "encode":
        encrypt(plain_text=text, shift_ammount=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_ammount=shift)
    else:
        print("Wrong Spelled!")
        end_ceaser = "no"


    end_ceaser=input("Type 'yes' if you want to go again. Otherwise type 'no'.")