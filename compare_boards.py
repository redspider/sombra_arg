"""
Compare the new and old arrival boards, generate a list of changes
"""
import json

data = json.load(open('data.json', 'r'))

for i, row in enumerate(data['airline_boards_original']):
    for k in row.keys():
        if row[k] != data['airline_boards_new'][i][k]:
            print(i, k, row['time'], row[k], '->', data['airline_boards_new'][i][k])
