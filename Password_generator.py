# Write a python program for a passsword generator

import random
import string

def generate_password(length=8):
     #Define the character sets
     lowercase = string.ascii_lowercase
     uppercase = string.ascii_uppercase
     special_chars = string.punctuation
     digits = string.digits

     #Ensure the password has at least one character from each set
     password = [
          random.choice(lowercase),
          random.choice(uppercase),
          random.choice(special_chars),
          random.choice(digits)
    ]
     
     #Fill the rest of the password length with random choice from all the sets
     if length > 4:
          all_chars = lowercase + uppercase + special_chars + digits
          password += random.choices (all_chars, k=length-4)

     #Shuffle the list to ensure the characters are in random order
     random.shuffle(password)

     #Convert the list to a string to create the password
     password = ''.join(password)

     return password

# Set the desired password length
password_length = 8

# Generate and print the strong password
strong_password = generate_password(password_length)
print("Generated strong Password:", strong_password)
