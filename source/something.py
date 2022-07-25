def collatzgen(number: int) -> int:
    """generator for Collatz function

    Args:
        number (int): number to start Collatz function at

    Yields:
        int: next number in Collatz sequence
    """

    while number != 1:

        number = 3 * number + 1

        while not number % 2:

            number /= 2

        yield int(number)


def collatz(number: int) -> list:
    """returns the Collatz sequence for a given number

    Args:
        number (int): number to start at

    Returns:
        list: list containing the Collatz sequence for a given number
    """

    return [number] + list(collatzgen(number))
