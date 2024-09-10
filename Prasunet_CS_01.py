def encrypt_caesar(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((char_code - base + shift_amount) % 26 + base)
            encrypted += new_char
        else:
            encrypted += char  # Non-alphabetic characters remain unchanged
    return encrypted

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def main():
    # Get user input
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    # Ask user for the operation to perform
    choice = input("Do you want to encrypt or decrypt the text? (e/d): ").strip().lower()
    
    if choice == 'e':
        result = encrypt_caesar(text, shift)
        print("Encrypted text:", result)
    elif choice == 'd':
        result = decrypt_caesar(text, shift)
        print("Decrypted text:", result)
    else:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
