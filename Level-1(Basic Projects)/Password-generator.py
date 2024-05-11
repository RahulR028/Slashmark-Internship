This Python script generates secure, random passwords for you!

Features:

Generates a specified number of passwords (default: 1)
*Allows customization of password length for each password (default: 8 characters)
*Creates passwords with a mix of lowercase letters, numbers, and uppercase letters
*User-friendly interface for choosing password lengths

How to Use:

1.Run the script.
2.Enter the desired number of passwords (press Enter for default: 1).
3.For each password, you can choose a specific length (press Enter for default: 8 characters).
4.The script will generate and display the requested passwords.
    
Security:

This script uses random number generation to create unpredictable passwords.
The script encourages strong passwords by including a mix of character types (lowercase, uppercase, numbers).

import random

def generate_password(pw_length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []
    for length in pw_length:
        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    return passwords

def replace_with_number(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword))
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword

def replace_with_uppercase_letter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword

def main():
    num_passwords = int(input("How many passwords do you want to generate? (Default is 1): ") or 1)
    print("Generating", num_passwords, "password(s)")
    
    password_lengths = []
    default_length = 8  # Default password length
    print("Default length of password is", default_length)
    
    for i in range(num_passwords):
        length_input = input("Enter the length of Password #" + str(i + 1) + " (Default is " + str(default_length) + "): ")
        if length_input:
            length = int(length_input)
        else:
            length = default_length
        password_lengths.append(length)
    
    passwords = generate_password(password_lengths)

    for i, password in enumerate(passwords):
        print("Password #" + str(i + 1) + " =", password)

main()
