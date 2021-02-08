def square_digits(num):
    output =""
    for digit in str(num):
        output += str(int(digit) ** 2)
    pass
    return int(output)