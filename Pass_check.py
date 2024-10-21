import re

# Main function to interact with the user

password = input("Enter a password to check its strength: ")

# Initialize a strength score
strength_score = 0

# Criteria 1: Check length
if len(password) >= 8:
    strength_score += 1
else:
    print("Password should be at least 8 characters long.")

# Criteria 2: Check for uppercase and lowercase letters
if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
    strength_score += 1
else:
    print("Password should contain both uppercase and lowercase letters.")

# Criteria 3: Check for digits
if re.search(r'\d', password):
    strength_score += 1
else:
    print("Password should contain at least one digit.")

# Criteria 4: Check for special characters
if re.search(r'[\W_]', password):  # \W matches any non-alphanumeric character
    strength_score += 1
else:
    print("Password should contain at least one special character (e.g., @, #, $).")

# Provide feedback based on strength score
if strength_score == 4:
    print("Password is strong!")
elif strength_score == 3:
    print("Password is moderate. Consider adding more special characters or length.")
elif strength_score == 2:
    print("Password is weak. Improve by adding uppercase letters, numbers, and symbols.")
else:
    print("Password is very weak. It needs to be longer and contain more complex characters.")



