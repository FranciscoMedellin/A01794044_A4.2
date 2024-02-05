"""
Compute Statistics
"""
import sys
import time
from prettytable import PrettyTable
from utils.descriptive_statistics import DescriptiveStatistics


# start time
start_time = time.time()

# check and get arguments
if len(sys.argv) < 2:
    print("Error, Please Usage: python computeStatistics.py fileWithData.txt")
    sys.exit(1)
FILENAME = sys.argv[1]

# instance descriptive statistics
statistics = DescriptiveStatistics(FILENAME)

# pretty table object
table_results = PrettyTable()

# column names
table_results.field_names = ['Count', 'Mean', 'Median', 'Mode',
                       'Standard deviation', 'Variance']

# row data
table_results.add_row([statistics.count(),
                      statistics.mean(),
                      statistics.median(),
                      statistics.mode(),
                      statistics.standard_deviation(),
                      statistics.variance()])

# execution time
total_time = f'TOTAL TIME OF EXECUTION: {time.time() - start_time} SECONDS'

# print results and time
print(table_results)
print(total_time)
result = f'{table_results} \n\n {total_time}'


# write the results on a text file
with open('StatisticsResults.txt', 'w', encoding='utf-8') as output:
    output.write(result)