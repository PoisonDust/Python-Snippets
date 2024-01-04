import random
import string

def generate_password(length=12, include_symbols=False):
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation.replace('_', '')

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Custom Password Generator")
    length = int(input("Enter the length of the password: "))
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, include_symbols)
    print(f"Generated Password: {password}")

    input("Press Enter to exit...")  

if __name__ == "__main__":
    main()
