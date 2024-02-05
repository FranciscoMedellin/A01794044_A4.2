import sys
import time


class DescriptiveStatistics:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.read_file()
        self.start_time = time.time()

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    try:
                        number = float(line.strip())
                        self.data.append(number)
                    except ValueError:
                        print(f"Invalid data found: {line.strip()}")

        except FileNotFoundError:
            print(f"File {filename} not found.")
            sys.exit(1)

    def mean(self):
        if not self.data:
            return None
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        if not self.data:
            return None
        counts = {}
        for item in self.data:
            counts[item] = counts.get(item, 0) + 1
        max_count = max(counts.values())
        modes = [item for item, count in counts.items() if count == max_count]
        if len(modes) == 1:
            return modes[0]
        return "N/A"

    def variance(self):
        if not self.data:
            return None
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def standard_deviation(self):
        if not self.data:
            return None
        return self.variance() ** 0.5

    def compute_statistics(self):
        mean_value = self.mean()
        median_value = self.median()
        mode_value = self.mode()
        variance_value = self.variance()
        std_deviation_value = self.standard_deviation()

        with open('StatisticsResults.txt', 'w') as result_file:
            result_file.write(f"Mean: {mean_value}\n")
            result_file.write(f"Median: {median_value}\n")
            result_file.write(f"Mode: {mode_value}\n")
            result_file.write(f"Variance: {variance_value}\n")
            result_file.write(f"Standard Deviation: {std_deviation_value}\n")
            result_file.write(f"Time Elapsed: {time.time() - self.start_time} seconds\n")

        print(f"Mean: {mean_value}")
        print(f"Median: {median_value}")
        print(f"Mode: {mode_value}")
        print(f"Variance: {variance_value}")
        print(f"Standard Deviation: {std_deviation_value}")

    def count(self):
        return len(self.data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    statistics = DescriptiveStatistics(filename)
    statistics.compute_statistics()
