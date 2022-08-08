import csv
import os

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 10, 'c': 30}

with open('./sample_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(f, ['a', 'b', 'c'])
    writer.writeheader()
    writer.writerow(d1)
    writer.writerow(d2)


# os.remove('./sample_dictwriter.csv')

