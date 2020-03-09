# Python program to convert 
# JSON file to CSV 


import json 
import csv
from os import path
from pandas import json_normalize

INPUT_JSON = "foresee_full_input.json"
OUTPUT_CSV = "scripts/data/foresee_full_output.csv"

# Opening JSON file and loading the data 
# into the variable data
if not path.exists(INPUT_JSON):
	raise SystemExit(INPUT_JSON + " does not exist")

with open(INPUT_JSON) as json_file:
	data = json.load(json_file) 

json_data = data['items'] 

# now we will open a file for writing
mode = 'x'
if path.exists(OUTPUT_CSV):
	mode = 'w'
data_file = open(OUTPUT_CSV, mode)

# create the csv writer object 
csv_writer = csv.writer(data_file) 

# Counter variable used for writing 
count = 0
# List variable for all the "responses" blocks
all_responses = []

for item in json_data:
	# Remove unnecessary keys
	keys_to_remove=("id","responseTime","experienceDate","latentScores")
	list(map(item.__delitem__, filter(item.__contains__,keys_to_remove)))
	count += 1
	all_responses.append(item)

# Dict variable for all the objects flattened with one "responses" key
questions_and_answers = dict()
# Another counter variable
another_count = 0

for response in all_responses:
	questions_and_answers.update(response)

for single in questions_and_answers['responses']:
	# Writing headers of CSV file
	if another_count == 0:
		print(single)
		header = single.keys() 	
		csv_writer.writerow(header)
	count += 1
	# Writing data of CSV file 
	csv_writer.writerow(single.values()) 

data_file.close()
