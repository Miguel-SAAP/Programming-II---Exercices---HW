alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"

message = ""
with open("secret.txt") as f:
    for line in f:
        count = sum(1 for char in line if char in vowel)
        message += alphabet[count]

print("Decoded message:", message)
