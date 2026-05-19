import random
import string

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Length must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

all_chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(length):
    password += random.choice(all_chars)

print(f"\nGenerated Password: {password}")