import sys
import time


class WordCounter:
    def __init__(self, filename):
        self.filename = filename
        self.word_count = {}
        self.data = []

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    try:
                        l = line.strip()
                        if not line:
                            print
                            continue
                        self.data.append(l)
                   
                    except ValueError:
                        print(f"Invalid data found: {line.strip()}")

        except FileNotFoundError:
            print(f"File {filename} not found.")
            sys.exit(1)


    def count(self):
        self.read_file()

        word_count = {}
        # iterate over data and get count words using key dictionaries and values
        for w in self.data:
            self.word_count[w] = self.word_count.get(w, 0) + 1
        word_count = self.word_count.copy()
        
        return word_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    word_counter = WordCounter(filename)
    word_counter.count_words()
