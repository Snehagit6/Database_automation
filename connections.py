import pymysql


def database_connection():

    try:   # Establish a connection to MySQL database
        con=pymysql.connect\
            ("localhost", "root", "Securepass6!",
                             "MySQL") # Localhost->local machine ,else IP address for remote address
        # Creating a cursor object that handles the records of a particular table
        cursor = con.cursor()
    except Exception as e:
        print("Database could not be connected as :", e.args)
    else:

        print("Database is connected successfully")
        return cursor
def closing_conn():
    database_connection().close()

