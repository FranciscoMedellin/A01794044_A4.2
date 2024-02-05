"""
Convert Numbers Program
"""

import sys
import time
from prettytable import PrettyTable
from utils.number_converter import Converter


# start time
start_time = time.time()

# check and get arguments
if len(sys.argv) != 2:
    print("Usage: python convertNumbers.py fileWithData.txt")
    sys.exit(1)
FILENAME = sys.argv[1]

# instace of Converter class
converter = Converter(FILENAME)

# get binaries
binary_results = converter.convert_to_binary()

# get hex
hexadecimal_results = converter.convert_to_hexadecimal()

# table results
table_results = PrettyTable()
table_results.field_names = ['Number', 'Decimal', 'Binary', 'Hexadecimal']

for i, (decimal, binary, hexadecimal) in enumerate(
    zip(converter.data,binary_results,hexadecimal_results)):
    table_results.add_row([i + 1, decimal, binary, hexadecimal])

# execution time
execution_time = time.time() - start_time
total_time = f'TOTAL TIME OF EXECUTION: {execution_time:.3f} SECONDS'

# print results and time
print(table_results)
print(total_time)
result = f'{table_results} \n\n {total_time}'

# Write the results on a text file
with open('ConvertionResults.txt', 'w', encoding='utf-8') as output:
    output.write(result)
