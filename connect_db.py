import mysql.connector

def connect_db():
    db_name = "library_db"
    user = "root"
    password = "jesica123"
    host = "localhost"

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host 
        )
        print("Connected Succesfully")
        return conn

    except mysql.connector.Error as e:
        print(f"Error: {e}")