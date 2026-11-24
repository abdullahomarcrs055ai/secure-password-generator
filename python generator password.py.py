import secrets
import string

def generate_password(length=12):
    # Combine uppercase, lowercase, digits, and special symbols
    letters = string.ascii_letters      # A-Z and a-z
    digits = string.digits              # 0-9
    symbols = "!@#$%^&*()-_=+"        # Safe special characters
    
    all_characters = letters + digits + symbols

    # Pick random characters securely for the given length
    password = ""
    for _ in range(length):
        password += secrets.choice(all_characters)

    return password

# Main program execution
print("--- Secure Password Generator ---")
user_length = int(input("Enter desired password length (e.g., 12): "))

new_password = generate_password(user_length)
print("Your generated password is:", new_password)
