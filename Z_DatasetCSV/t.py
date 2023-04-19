import csv
import random

# generate random passwords


def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(8):
        password += random.choice(chars)
    return password


# create and write data to CSV file
with open("user_passwords.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["user_id", "password"])
    for i in range(1, 100000):
        password = generate_password()
        writer.writerow([i, password])
