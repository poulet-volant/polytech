import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as inputfile :
        data = [column for column in csv.DictReader(inputfile)]
        with open(OUTPUT_FILENAME, 'w') as outputfile :
            json.dump(data, outputfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки            ok
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end='')

