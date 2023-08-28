import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    # Define character pools based on user preferences
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type")
        return

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator :) ")

    # Get user preferences for character types
    use_letters = input("Do you want to include letters (yes/no)? ").lower() == 'yes'
    use_digits = input("Do you want to include digits (yes/no)? ").lower() == 'yes'
    use_symbols = input("Do you want to include symbols (yes/no)? ").lower() == 'yes'

    password_length = int(input("Please enter the desired length of the password: "))
    
    if password_length <= 0:
        print("The password length must be greater than 0.")
        return
    
    generated_password = generate_password(password_length, use_letters, use_digits, use_symbols)
    if generated_password:
        print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()