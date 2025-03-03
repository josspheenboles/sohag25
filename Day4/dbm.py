import psycopg2

def connect(**kargs):
    try:
        conn = psycopg2.connect(**kargs)
        return conn
        # print("Connected to the database!")
    except Exception as e:
        return (f"Unable to connect to the database: {e}")

def ddl(connection,query):
    cursor = connection.cursor()
    cursor.execute(query=query)
    connection.commit()

#dml--->select & (insert,updat,delete)
def dmlcrud(connection,query,*values):
    cursor = connection.cursor()
    cursor.executemany(query,values)
    connection.commit()

def select (connection,query,where =None):
    cursor = connection.cursor()
    if(where is not None):
        cursor.execute(query=f'{query} {where}')
    else:
        cursor.execute(query=query)
    return cursor.fetchall()