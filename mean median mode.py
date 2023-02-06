
def mean_median_mode(numbers):
    # Mean
    mean = sum(numbers) / len(numbers)

    # Median
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        median = numbers[len(numbers) // 2]

    # Mode
    from collections import Counter
    number_counts = dict(Counter(numbers))
    max_count = max(number_counts.values())
    modes = [number for number, count in number_counts.items() if count == max_count]
    if len(modes) == len(numbers):
        mode = "No mode found"
    elif len(modes) > 1:
        mode = "Multiple modes found: " + str(modes)
    else:
        mode = modes[0]

    return mean, median, mode

numbers = [int(x) for x in input("Enter a list of numbers, separated by spaces: ").split()]
mean, median, mode = mean_median_mode(numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

