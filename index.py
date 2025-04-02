import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  # Replace with your MySQL host (e.g., localhost, 127.0.0.1, or a remote server address)
  user="root",   # Replace with your MySQL username
  password="LANE", # Replace with your MySQL password
  database="student_registration" # The database you created
)

if mydb.is_connected():
  print("Successfully connected to MySQL database.")
  # Now you can execute queries using the mydb connection object (e.g., cursor = mydb.cursor(); cursor.execute("SELECT * FROM students"); ...)
else:
  print("Connection failed.")

# ... rest of your Python code ...

mydb.close() # Close the connection when you're done

'''--  Key Points about the Connection String:
--  1. Replace the placeholders. Make sure to replace "your_mysql_host", "your_mysql_user", "your_mysql_password" with your actual MySQL credentials.
--  2. Security:  **Never** hardcode your database credentials directly into your code, especially if it's going to be shared or in a public repository. Use environment variables or configuration files to store these sensitive details securely.
--  3. Library: You'll need the appropriate database connector library for your programming language (e.g., `mysql.connector` for Python, JDBC for Java, etc.).
--  4. Close the connection: It's a good practice to close the database connection when you're finished with it to free up resources.
'''
