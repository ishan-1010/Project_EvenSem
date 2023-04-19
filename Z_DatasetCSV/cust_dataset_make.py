import csv
import random

first_names = ['Emily', 'Michael', 'Jessica', 'David', 'Amanda',
               'Christopher', 'Ashley', 'Joshua', 'Jennifer', 'Matthew']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones',
              'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

# Generate 200 users
users = []
for i in range(200):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    birthday = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(1950, 2010)}"
    gender = random.choice(['Male', 'Female'])
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    phone_number = f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    users.append((i+1, first_name, last_name, birthday,
                 gender, email, phone_number))

# Write users to CSV
with open('users.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['UserId', 'First Name', 'Last Name',
                    'Birthday', 'Gender', 'Email', 'Phone Number'])
    for user in users:
        writer.writerow(user)
