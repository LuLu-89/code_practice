def high_and_low(numbers):
    output = ''
    numbers = [int(x) for x in numbers.split()]
    output = str(max(numbers)) + ' ' + str(min(numbers))
    return output