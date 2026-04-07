import json


FILENAME = 'input.json'


def task() -> float:
    sum = 0
    with open(FILENAME, 'r') as file :
        data = json.load(file)
        for dict in data :
            sum += dict['score'] * dict['weight']
    return sum

print(f'{task():.3f}')

