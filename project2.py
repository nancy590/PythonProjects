# PASSWORD STRENGTH CHECKER

import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 0
    if not length_error: score += 1
    if not uppercase_error: score += 1
    if not lowercase_error: score += 1
    if not digit_error: score += 1
    if not special_char_error: score += 1

    if score == 5:
        return "✅ Strong Password"
    elif 3 <= score < 5:
        return "⚠️ Medium Password"
    else:
        return "❌ Weak Password"

print("=== PASSWORD STRENGTH CHECKER ===")
password = input("Enter a password to check: ")
strength = check_password_strength(password)
print(strength)
