numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)

print(numbers)
