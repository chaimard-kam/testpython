import mysql.connector

try:
    # Establish connection to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mama_store"
    )
    cursor = conn.cursor()

    # Execute SQL query to select product details
    query = "SELECT * FROM products WHERE order_level < 50"
    cursor.execute(query)

    # Fetch the result
    results = cursor.fetchall()

    # Check if result is not empty
    if results:
        print("Products with remaining order below 50:")
        print("---------------------------------------")
        for result in results:
            print("Product ID:", result[0])
            print("Product Name:", result[1])
            print("Price:", result[2])
            print("Remaining Order:", result[3])
            print("------------------------")
    else:
        print("No products found with remaining order below 50.")

    # Close cursor and connection
    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)
