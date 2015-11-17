import json


DataPath = '../../data/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

# Read JSON objects
record = [json.loads(line) for line in open(DataPath)]

# Show first record
print record[0]





























