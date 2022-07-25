def collatzgen(number):

    while number != 1:

        number = 3 * number + 1

        while not (number % 2):

            number /= 2

        yield int(number)


def collatz(number):

    return [number] + [num for num in collatzgen(number)]
