import random
import string

def get_positive_integer(prompt, min_val=8):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Error: Password length must be at least {min_val} characters. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid whole number.")

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    guaranteed_chars = []
    
    if use_upper:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))
        
    remaining_length = length - len(guaranteed_chars)
    remaining_chars = [random.choice(char_pool) for _ in range(remaining_length)]
    
    password_list = guaranteed_chars + remaining_chars
    random.shuffle(password_list)
    
    return "".join(password_list)

def main():
    print("=" * 45)
    print("       RANDOM PASSWORD GENERATOR       ")
    print("=" * 45)
    
    while True:
        length = get_positive_integer("\nEnter desired password length (minimum 8): ", min_val=8)
        
        print("\nSelect character types to include (Yes/No):")
        while True:
            use_upper = input("Include Uppercase letters (A-Z)? (y/n): ").strip().lower() in ['y', 'yes']
            use_lower = input("Include Lowercase letters (a-z)? (y/n): ").strip().lower() in ['y', 'yes']
            use_digits = input("Include Numbers (0-9)? (y/n): ").strip().lower() in ['y', 'yes']
            use_symbols = input("Include Special Symbols (!@#$)? (y/n): ").strip().lower() in ['y', 'yes']
            
            selected_count = sum([use_upper, use_lower, use_digits, use_symbols])
            if selected_count >= 2:
                break
            else:
                print("\nError: You must select at least 2 character types for a secure password. Please choose again.\n")
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        
        print("\n" + "-" * 45)
        print(f"Generated Password: {password}")
        print("-" * 45)
        
        choice = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("\nThank you for using the Password Generator! Stay secure.")
            break

if __name__ == "__main__":
    main()
