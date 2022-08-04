"""Collatz conjecture related things

This file can be imported into another python file.

collatz_gen is a generator for the Collatz sequence of a number.

collatz returns a list containing the entire Collatz sequence of a given number.
"""

def collatz_gen(number: int) -> int:
	"""generator for Collatz function

	Args:
		number (int): number to start Collatz function at

	Yields:
		int: next number in Collatz sequence
	"""

	while number != 1:

		yield int(number)

		number = 3 * number + 1

		while not number % 2:

			number /= 2


def collatz(number: int) -> list:
	"""returns the Collatz sequence for a given number

	Args:
		number (int): number to start at

	Returns:
		list: list containing the Collatz sequence for a given number
	"""

	return list(collatz_gen(number))
