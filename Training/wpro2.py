def collatz_conjecture(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

number = 13
print(collatz_conjecture(number))