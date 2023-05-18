
STEPS:-

1.Read data from CSV files:
Read "data.csv" file with columns: data_id (int), Subject_id (int), value1 (int), value2 (int).
Read "subject.csv" file with columns: Subject_id (int), Subject_name (string).

2.Transform the "value2" column of the "data.csv" file:
Square the values in the "value2" column.

3.Save the transformed data to MySQL database:
Established a connection to the MySQL database.
Created a table named "data" with columns: data_id (int), Subject_id (int), value1 (int), value2 (int).
Inserted the transformed data from "data.csv" into the "data" table.

4.Showcase the relationship between "data.csv" and "subject.csv" files:
Merged the "data" and "subject" dataframes based on the common "Subject_id" column.
Created a new dataframe named "result" with columns from both files.
Saved the "result" dataframe to a CSV file named "result.csv".

5.Save the "result.csv" file to the database:
Created a table named "result" with columns: data_id (int), Subject_id (int), value1 (int), value2 (int), Subject_name (string).
Inserted the data from the "result.csv" file into the "result" table.