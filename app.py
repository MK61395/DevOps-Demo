import psycopg2
import os

# Database connection parameters (replace with your RDS values)
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"DB_USER: {os.getenv('DB_USER')}")

# Connect to the RDS instance
conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),  # RDS instance endpoint
    port=5432,                  # Default PostgreSQL port
    dbname=os.getenv('DB_NAME'),  # The name of the database
    user=os.getenv('DB_USER'),    # Your RDS master username
    password=os.getenv('DB_PASSWORD')  # Your RDS password
)
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
""")
conn.commit()

# Create another table for testing (test_table_2)
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_table_2 (
    id SERIAL PRIMARY KEY,
    description VARCHAR(100)
);
""")
conn.commit()

# Create a third table to store your name (Muhammad Kashif)
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_table_3 (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100)
);
""")
conn.commit()

# Insert data
cursor.execute("INSERT INTO test_table (name) VALUES (%s)", ("DevOps Class",))
conn.commit()

# Insert data into the second table (test_table_2)
cursor.execute("INSERT INTO test_table_2 (description) VALUES (%s)", ("This is a test table 2",))
conn.commit()

# Insert data into the second table (test_table_2)
cursor.execute("INSERT INTO test_table_2 (description) VALUES (%s)", ("This is a test table 2",))
conn.commit()


# Fetch data
cursor.execute("SELECT * FROM test_table;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fetch data from the second table (test_table_2)
cursor.execute("SELECT * FROM test_table_2;")
rows_2 = cursor.fetchall()
print("\nData from test_table_2:")
for row in rows_2:
    print(row)

# Fetch data from the third table (test_table_3)
cursor.execute("SELECT * FROM test_table_3;")
rows_3 = cursor.fetchall()
print("\nData from test_table_3:")
for row in rows_3:
    print(row)

cursor.close()
conn.close()
