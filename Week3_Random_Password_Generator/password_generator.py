import random
import string

print("===== Random Password Generator =====")

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = [
    random.choice(letters),
    random.choice(digits),
    random.choice(symbols)
]

password += random.choices(all_characters, k=length-3)

random.shuffle(password)

print("\nGenerated Password:")
print("".join(password))