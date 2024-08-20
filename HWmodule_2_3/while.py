from importlib.metadata import pass_none

numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(numbers) and numbers[i] >= 0:
    if 0 in numbers:
        numbers.remove(0)
    print(numbers[i])
    i += 1









