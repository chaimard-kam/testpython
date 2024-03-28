import mysql.connector

# Establish connection to MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mama_store"
    )
    cursor = conn.cursor()

    # Execute SQL query to select username and password
    query = "SELECT name, password FROM members WHERE name = %s AND password = %s"
    cursor.execute(query, ("john1", "1234"))

    # Fetch the result
    result = cursor.fetchone()

    # Check if result is not empty
    if result:
        username, password = result
        print("Username:", username)
        print("Password:", password)
    else:
        print("Username and password not found in the database.")

    # Close cursor and connection
    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)
