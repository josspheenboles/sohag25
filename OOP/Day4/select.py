import psycopg2

# Database connection parameters
conn_params = {
    'dbname': 'sohagdemo',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': 5432
}

# Establish a connection
try:
    # connect
    conn = psycopg2.connect(**conn_params)
    #
    cursor=conn.cursor()
    query="select * from track"
    cursor.execute(query=query)
    tracks=cursor.fetchall()
    print('ID , Name')
    print('-----------')
    for id,track in tracks:
        print(f'{id} , {track}')
        print('-----------')
    # print("Connected to the database!")
except Exception as e:
    print(f"Unable to connect to the database: {e}")


#sql select * from track
#execuate query
#featch

#close connection