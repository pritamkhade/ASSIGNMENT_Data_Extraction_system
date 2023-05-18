import pandas as pd
import mysql.connector

# Read data from CSV files

data_df = pd.read_csv('D:/SMVITA/PYNOTS/project/data.csv')
subject_df = pd.read_csv('D:/SMVITA/PYNOTS/project/subject.csv')

# Transform the "value2" column
data_df['value2'] = data_df['value2'] ** 2

# Connect to MySQL database
cnx = mysql.connector.connect(host="localhost", user="root", password="Pritam@1999", database="data_extraction_system")
cursor = cnx.cursor()

# Create "data" table
create_data_table_query = '''
CREATE TABLE IF NOT EXISTS data (
    data_id INT PRIMARY KEY,
    Subject_id INT,
    value1 INT,
    value2 INT
);
'''
cursor.execute(create_data_table_query)

# Save data to "data" table
data_values = data_df.values.tolist()
insert_data_query = '''
INSERT INTO data (data_id, Subject_id, value1, value2)
VALUES (%s, %s, %s, %s)
'''
cursor.executemany(insert_data_query, data_values)
cnx.commit()

# Create "subject" table
create_subject_table_query = '''
CREATE TABLE IF NOT EXISTS subject (
    Subject_id INT PRIMARY KEY,
    Subject_name VARCHAR(255)
);
'''
cursor.execute(create_subject_table_query)

# Save data to "subject" table
subject_records = subject_df.values.tolist()
insert_subject_query = '''
INSERT INTO subject (Subject_id, Subject_name)
VALUES (%s, %s)
'''
cursor.executemany(insert_subject_query, subject_records)
cnx.commit()

# Showcase the relationship and save to "result.csv"
result_df = pd.merge(data_df, subject_df, on='Subject_id')
result_df.to_csv('result.csv', index=False)

# Create "result" table
create_result_table_query = '''
CREATE TABLE IF NOT EXISTS result (
    data_id INT,
    Subject_id INT,
    value1 INT,
    value2 INT,
    Subject_name VARCHAR(255)
);
'''
cursor.execute(create_result_table_query)

# Save data to "result" table
result_values = result_df.values.tolist()
insert_result_query = '''
INSERT INTO result (data_id, Subject_id, value1, value2, Subject_name)
VALUES (%s, %s, %s, %s, %s)
'''
cursor.executemany(insert_result_query, result_values)
cnx.commit()

# Close the database connection
cursor.close()
cnx.close()
