import sys
import time


class Converter:
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
                        number = int(line.strip())
                        self.data.append(number)
                    except ValueError:
                        print(f"Invalid data found: {line.strip()}")

        except FileNotFoundError:
            print(f"File {filename} not found.")
            sys.exit(1)

    def convert_to_binary(self):
        binary_results = []
        for num in self.data:
            if num < 0:
                # Convertir a binario utilizando complemento a dos
                binary_representation = bin(int(2 ** 32 + num))
                # Cortar los bits adicionales de 1 que bin() agrega para números negativos
                binary_representation = binary_representation[-32:]
            else:
                binary_representation = bin(int(num))
            binary_results.append(binary_representation)
        return binary_results


    def convert_to_hexadecimal(self):
        hexadecimal_results = [hex(int(num)) for num in self.data]
        return hexadecimal_results

    def perform_conversion(self):
        binary_results = self.convert_to_binary()
        hexadecimal_results = self.convert_to_hexadecimal()

        with open('ConversionResults.txt', 'w') as result_file:
            for binary, hexadecimal in zip(binary_results, hexadecimal_results):
                result_file.write(f"Binary: {binary}, Hexadecimal: {hexadecimal}\n")
            result_file.write(f"Time Elapsed: {time.time() - self.start_time} seconds\n")

        for binary, hexadecimal in zip(binary_results, hexadecimal_results):
            print(f"Binary: {binary}, Hexadecimal: {hexadecimal}")
        print(f"Time Elapsed: {time.time() - self.start_time} seconds")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    converter = Converter(filename)
    converter.perform_conversion()

