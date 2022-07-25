def collatzgen(number):
	while True
		number = number * 3 + 1
		while not(number % 2):
			number / 2
		yield number

def collatz(number):
	return [number] + [num for num in collatzgen(number)]

