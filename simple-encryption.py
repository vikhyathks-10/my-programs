def caesar_cipher():
    text = input("Enter text to encrypt: ")
    shift = input("Enter shift number: ")
    if not shift.isdigit():
        print("Invalid shift.")
        return
    shift = int(shift)
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    print("Encrypted text:", result)

caesar_cipher()
def simple_encryption():
    print("Welcome to Simple Encryption Tool")
    while True:
        choice = input("Choose an option: 1. Encrypt 2. Decrypt 3. Exit: ")
        if choice == '1':
            caesar_cipher()
        elif choice == '2':
            print("Decryption is not implemented yet.")
        elif choice == '3':
            print("Exiting the tool.")
            break
        else:
            print("Invalid option, please try again.")