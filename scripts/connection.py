import psycopg2

connection = None

def run_sql(sql, values):
    if connection == None:
        init_connection()
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()

def init_connection():
    global connection
    try:
        connection = psycopg2.connect("dbname='tcc' user='postgres' password='darklord' host='localhost'")
    except:
        print ("I am unable to connect to the database.")
