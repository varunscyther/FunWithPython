import csv
import json

json_data = []
input_files = str(input()).split()
output_file = str(input())
result_data_list = []
for i in input_files:
    with open(i) as f:
        for line in f:
            json_line = json.loads(line)
            json_data.append(json_line)

sorted_json_data = sorted(json_data, key=lambda x: (x["date"], x["consumer_id"]))

for log in sorted_json_data:
    row_list = [log["date"], log["message"]]
    result_data_list.append(row_list)


with open(output_file, 'w', newline='') as write_file:
    output = csv.writer(write_file, delimiter='\t')
    output.writerows(result_data_list)

