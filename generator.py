import sys
import time
import random
import os


verison = "\t\t\tYou are on verison 1.00"

introduction = """
===========================================================
Hello, my name is Harrison and I am Python developer. 

This is a generator that I am working on. For now, it will\nbe closed-source. Once I improve on the logic and the aspects\nit will be open-source. 

© FearTheUprising - All Rights Reserved. 
===========================================================
"""

file_path = "passwords.txt"

if not os.path.exists(file_path):
    open(file_path, "w").close()

def save_to_file(data):
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        file.write(data + "\n")

    if file_exists:
        print(f"Appended to existing {file_path}")
    else: 
        print(f"Created a new file called: {file_path}")


def password_generator(mode="spinner"):
    print("I will generate a password for you, based on the specifications that you give.")
    letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    print("""
1). 5 to 10 in length
2). 10 to 30 in length
""")

    choice = int(input("Please choose a number for a choice: "))
    
    if choice == 1:
        user_input = int(input("Enter a password length (e.g., 5 - 10): "))
        if 5 <= user_input <= 10:
            print("Printing your password...", end='', flush=True)
            spinner = '|/-\\'
            start_time = time.time()
            while time.time() - start_time < 3:  # Spinner will run for 3 seconds
                for char in spinner:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.4)
                    sys.stdout.write('\b') 
                    sys.stdout.flush()
                    result = ''.join(random.choices(letters, k=user_input))
            print(f"\nYour generated password is: {result}")
            save_to_file(f"Password: {file_path}")
    elif choice == 2:
        user_input = int(input("Enter a password length (e.g., 10 - 30): "))
        if 10 <= user_input <= 30:
            print("Printing your password...", end='', flush=True)
            spinner = '|/-\\'
            start_time = time.time()
            while time.time() - start_time < 3:
                for char in spinner:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.4)
                    sys.stdout.write('\b') 
                    sys.stdout.flush()
            sys.stdout.write(' \b')
            print('\n')
            result = ''.join(random.choices(letters, k=user_input))
            print(f'Your generated password is: {result}')
            save_to_file(f"Password: {file_path}")
    else: 
        print("No input was entered.")

def email_generator():
    print("I will generate an email for you using various domains\nNote: You will still need to use this email to sign up on the actual website.")
    domains = {
        1: "aol.com",
        2: "gmail.com",
        3: "yahoo.com",
        4: "outlook."
    }

    print("""
1). AOL
2). G-mail
3). Yahoo
4). Outlook
5). Exit
""")

    user_input = int(input("Please enter a number (1 - 5): "))

    letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"

    if user_input in domains:
        yes_or_no = input("Would you like a specific number of characters (Y or N): ").upper()
        if yes_or_no == "Y":
            how_many = int(input("How many characters would you like: "))
            result = ''.join(random.choices(letters, k=how_many))
        else:
            result = ''.join(random.choices(letters, k=random.randint(1, 10)))

        time.sleep(3)
        print("Generating email address...")
        time.sleep(3)
        email_address = f"{result}@{domains[user_input]}"

        print(f'Your generated email address is: {email_address}')

        save_to_file(f"Email: {email_address}")
    elif user_input == 5: 
        print("Returing to main menu...")

    else: 
        print("Invalid input, please try again.")
    

menu_options = {
    '1': password_generator,
    '2': email_generator,
}

def main():
    print(verison)
    time.sleep(3)
    print(introduction)

    print("This is a generator program that I have made for fun, I hope that you enjoy it.")
    print("""
1) Password Generator
2) Email generator
""")
     
    while True:
        choice = input("Please enter a choice: ")
        action = menu_options.get(choice)
        if action:
            action()  # Calls the selected option with the specified mode
        else: 
            print("Invalid choice, please try again.")
main()