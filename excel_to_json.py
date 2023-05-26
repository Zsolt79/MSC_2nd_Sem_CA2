import pandas as pd

# Define the path to the dataset
file_path = '/home/hduser/Downloads/Trump_Tweets.xlsx'
sheet_name = 'Sheet1'

# Read the Excel file into a Pandas dataframe
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Convert the dataframe to JSON and write it to a file
json_file = '/home/hduser/Trump_Tweets.json'
df.to_json(json_file, orient='records') 
