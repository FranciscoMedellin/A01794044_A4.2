"""
Word Counter Program
"""
import sys
import time
from prettytable import PrettyTable
from utils.word_counter import WordCounter

# get start time
start_time = time.time()

# check and get arguments
if len(sys.argv) != 2:
    print("Usage: python wordCount.py fileWithData.txt")
    sys.exit(1)
FILENAME = sys.argv[1]

# object instance WordCounter class
word_counter = WordCounter(FILENAME)

# count_words dict
count_words = word_counter.count()
print(len(count_words))

# table results
results_table = PrettyTable()
results_table.field_names = ['Word, Count']


with open('WordCountResults.txt', 'w', encoding='utf-8') as result_file:
    for word, count in count_words.items():
        result_file.write(f"{word}  {count}\n")
    result_file.write(f"Time Elapsed: {time.time() - start_time:.3f} seconds\n")
