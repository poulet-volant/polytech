numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total = sum(numbers[:4]+numbers[5:])
length = len(numbers)
missing = round(total / length, 2)
numbers[4] = missing

print("Измененный список:", numbers)

