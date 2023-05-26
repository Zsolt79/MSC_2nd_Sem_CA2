import json

def transform_to_jsonl(input_file, output_file):
    with open(input_file, 'r') as json_file, open(output_file, 'w') as jsonl_file:
        for line in json_file:
            data = json.loads(line)
            jsonl_file.write(json.dumps(data) + '\n')

# Path to your original JSON dataset file
input_file = "/home/hduser/Trump_Tweets.json"

# Path to the output JSONL file
output_file = "/home/hduser/Trump_Tweets.jsonl"

# Call the function to transform the dataset
transform_to_jsonl(input_file, output_file)

