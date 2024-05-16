import csv

def count_hexamers(file_path):
    hexamer_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line in hexamer_count:
                hexamer_count[line] += 1
            else:
                hexamer_count[line] = 1
    return hexamer_count

def write_csv(hexamer_count, output_file_path):
    with open(output_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Hexamer', 'Frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for hexamer, count in hexamer_count.items():
            writer.writerow({'Hexamer': hexamer, 'Frequency': count})

def main():
    file_path = 'ENST00000229239_hexamers.txt'
    output_file_path = 'ENST00000229239_hexamer_frequencies.csv'
    hexamer_count = count_hexamers(file_path)
    write_csv(hexamer_count, output_file_path)
    print("CSV file has been written successfully.")

if __name__ == "__main__":
    main()
