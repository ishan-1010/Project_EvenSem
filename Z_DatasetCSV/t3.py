import csv
import random

# Define the CSV file name
csv_file = "user_points.csv"

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["username", "points"])

    # Generate data for 1000 usernames
    for i in range(1, 1001):
        # Generate a random number of points between 0 and 100
        points = random.randint(0, 100)

        # Write the username and points to the CSV file
        writer.writerow([f"username_{i}", points])

print(f"CSV file '{csv_file}' has been generated successfully.")
