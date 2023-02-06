import itertools

def find_combinations(digits):
    digits = [str(d) for d in digits]
    return [''.join(combination) for combination in itertools.permutations(digits, 3)]
if __name__ == '__main__':
    digits = [int(input('Enter a digit: ')) for i in range(3)]
    combinations = find_combinations(digits)
    print('All possible combinations:', combinations)
