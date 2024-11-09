import psycopg2
import os

# Database connection parameters (replace with your RDS values)
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Connect to the RDS instance
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
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

# Insert data
cursor.execute("INSERT INTO test_table (name) VALUES (%s)", ("DevOps Class",))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM test_table;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()