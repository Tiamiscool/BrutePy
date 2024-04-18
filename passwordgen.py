import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_numbers(max_length):
    output = []
    for number in range(max_length, 0, -1):
        output.append(str(number))
    return '\n'.join(output) + '\n'

def get_number_letter_combinations(max_length):
    output = []
    for number in range(max_length, 0, -1):
        output.append(str(number))
        for length in range(1, max_length + 1):
            for combination in itertools.product(alphabet, repeat=length):
                output.append(str(number) + ''.join(combination))
    return '\n'.join(output) + '\n'

def generate_letter_combinations(max_length):
    for length in range(1, max_length + 1):
        for combination in itertools.product(alphabet, repeat=length):
            yield ''.join(combination)



