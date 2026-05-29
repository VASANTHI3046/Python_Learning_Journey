numbers = [15, 8, 23, 42, 7]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)