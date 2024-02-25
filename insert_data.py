import psycopg2
from psycopg2 import Error

def insert_data(id, firstname, age, about, lastname=None):
        try:
            connection =psycopg2.connect(
                                  user="db",
                                  password="db",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="db")

            cursor = connection.cursor()
            cursor.execute("""INSERT INTO users(id, firstname, age, about, lastname
            )VALUES(%s, %s, %s, %s, %s);""",(id, firstname, age, about, lastname))
            connection.commit()

            print("Data inserted successfully!")

        except Error as error:
            print("Error:", error)

        finally:
            if connection:
                cursor.close()
            connection.close()  

insert_data(id=2, firstname="abdulaziz", age=15, about="Test Message")