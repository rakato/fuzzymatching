
# compare 2 csvs and return best result
# taken from http://stackoverflow.com/questions/32055817/python-fuzzy-matching-fuzzywuzzy-keep-only-best-match

import pandas as pd
from pandas import DataFrame
from fuzzywuzzy import process
import csv

save_file = open('fuzzy_match_results.csv', 'w')
writer = csv.writer(save_file, lineterminator = '\n')

def parse_csv(path):

with open(path,'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        yield row


if __name__ == "__main__":
## Create lookup dictionary by parsing the products csv
data = {}
for row in parse_csv('names_1.csv'):
    data[row[0]] = row[0]

## For each row in the lookup compute the partial ratio

for row in parse_csv("names_2.csv"):
    #print(process.extract(row,data, limit = 100))
    for found, score, matchrow in process.extract(row, data, limit=100):
    ## Choose a score higher than "x" to look for a better match off the bat, ~80
        if score >= 80:
            print('%d%% partial match: "%s" with "%s" ' % (score, row, found))
            Digi_Results = [row, score, found]
            writer.writerow(Digi_Results)


save_file.close()
