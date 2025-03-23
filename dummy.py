import random
import string
import mysql.connector

# Connect to your database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='hemakesh',
    database='rcisaaw_mcc'
)

cursor = connection.cursor()

# Function to generate random names
def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Generate 2 lakh unique names
unique_names = set()
while len(unique_names) < 200000:
    unique_names.add(generate_random_name())

# Prepare data for insertion
data = [(name,) for name in unique_names]

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS dummy_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
)
""")

# Insert data into the table
batch_size = 1000  # Insert in batches for better performance
for i in range(0, len(data), batch_size):
    cursor.executemany("INSERT INTO dummy_data (name) VALUES (%s)", data[i:i + batch_size])

# Commit and close connection
connection.commit()
cursor.close()
connection.close()

print("2 lakh unique records inserted successfully!")
