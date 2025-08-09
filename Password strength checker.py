import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[^A-Za-z0-9]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    if any(errors):
        print("❌ Weak password. Try including:")
        if length_error:
            print("  - At least 8 characters")
        if digit_error:
            print("  - A number")
        if uppercase_error:
            print("  - An uppercase letter")
        if lowercase_error:
            print("  - A lowercase letter")
        if symbol_error:
            print("  - A special character (e.g. !@#$)")
    else:
        print("✅ Strong password!")

if __name__ == "__main__":
    user_input = input("Enter a password to check: ").strip()
    check_password_strength(user_input)