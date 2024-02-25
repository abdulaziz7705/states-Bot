import psycopg2
from psycopg2 import Error

def create_tables():
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="bot_db")

        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE Users
            (id SERIAL PRIMARY KEY,
            full_name VARCHAR(128) NOT NULL,
            username VARCHAR(128),
            tg_id INT NOT NULL UNIQUE)""")
        
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE Adv
            (id SERIAL PRIMARY KEY,
            full_name VARCHAR(128) NOT NULL,
            age INT NOT NULL    ,
            status VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL)""")


        connection.commit()
        print("Table created successfully!")

    except Error  as error:
        print("Error:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL closed!")

create_tables()

def insert_user_data( tg_id,full_name ,username=None):
        try:
            connection =psycopg2.connect(
                                  user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="bot_db"
            )

            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Users(tg_id,full_name ,username)
            VALUES (%s, %s, %s);""",(tg_id,full_name ,username))
            connection.commit()
            print("Data inserted successfully!")

        except Error as error:
            print("Error:", error)
        finally:
            if connection:
                cursor.close()
            connection.close()
            print("PostgreSQL closed!")    


# dcscsc52222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

def insert_adv_data(full_name, age, status, phone):
        try:
            connection =psycopg2.connect(
                                  user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="bot_db"
            )

            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Adv(full_name, age, status, phone)
            VALUES (%s, %s, %s, %s);""",(full_name, age, status, phone))
            connection.commit()
            print("Data inserted successfully!")

        except Error as error:
            print("Error:", error)
        finally:
            if connection:
                cursor.close()
            connection.close()
            print("PostgreSQL closed!")  