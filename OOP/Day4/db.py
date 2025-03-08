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
    conn = psycopg2.connect(**conn_params)
    cursor=conn.cursor()
    id=int(input('enter id'))
    naem=input('enter naem')
    query="insert into track values ({id},'{name}');"
    cursor.execute(query=query.format(id=id,name=naem))
    conn.commit()
    # print("Connected to the database!")
except Exception as e:
    print(f"Unable to connect to the database: {e}")