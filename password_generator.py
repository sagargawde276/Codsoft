print("Password generator")

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSTUVWXYZ0123456789@#!$*&"

length = int(input("enter the length of the password: "))

password = ""

for i in range(length):
    password+=random.choice(characters)

print("your password is generated",password)        