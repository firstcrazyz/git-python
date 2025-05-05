# import os 
# folder = 'backup_sql'
# if not os.path.exists(folder):
#     os.makedirs(folder)
    
# with open('pg20230426.sql','r',encoding='utf-8') as file:
#     count = 0
#     output = []
#     for line in file:
#         if line.startswith('CREATE DATABASE'):
#             with open(os.path.join(folder,f'test{count}.sql'),'w',encoding='utf-8')as outfile:
#                 outfile.write(''.join(output))
#             count +=1
#             output = []
#         output.append(line)

import psycopg2
import os
from airflow import DAG


# Connect to PostgreSQL
conn = psycopg2.connect(
    host="10.29.24.245",
    database="postgres",
    user="postgres",
    password="P@ssw0rd"
)

# Loop through all the SQL files in a directory
sql_dir = 'backup_sql'
for sql_file in os.listdir(sql_dir):
    if sql_file.endswith('.sql'):
        sql_path = os.path.join(sql_dir, sql_file)

        # Open the SQL file and read its contents
        with open(sql_path, 'r') as f:
            sql = f.read()

        # Execute the SQL statement
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        # Close the cursor
        cur.close()

# Close the database connection
conn.close()

