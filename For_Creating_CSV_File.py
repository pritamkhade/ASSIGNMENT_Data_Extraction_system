import pandas as pd

# Creating data for data_df DataFrame
data = {
    'data_id': [1, 2, 3, 4, 5],
    'Subject_id': [101, 102, 103, 101, 102],
    'value1': [10, 15, 12, 8, 20],
    'value2': [5, 8, 6, 3, 10]
}
# Creating data_df DataFrame
data_df = pd.DataFrame(data)
# Saving data_df to 'data.csv' file
data_df.to_csv('data.csv', index=False)


# Creating data for subject_df DataFrame
subject_data = {
    'Subject_id': [101, 102, 103],
    'Subject_name': ['Math', 'Science', 'English']
}

# Creating subject_df DataFrame
subject_df = pd.DataFrame(subject_data)

# Saving subject_df to 'subject.csv' file
subject_df.to_csv('subject.csv', index=False)


