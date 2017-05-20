import psycopg2

connection = None
last_cursor = None

def run_sql(sql, values = None):
    global last_cursor
    if connection == None:
        init_connection()
    last_cursor = connection.cursor()
    last_cursor.execute(sql, values)
    connection.commit()

def results():
    return last_cursor.fetchall()

def init_connection():
    global connection
    try:
        connection = psycopg2.connect("dbname='tcc' user='postgres' password='darklord' host='localhost'")
    except:
        print ("I am unable to connect to the database.")
