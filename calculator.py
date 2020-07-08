"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def main():

	while True:
		input_string = input()
		tokens = input_string.split()
		if tokens[0] == '+':
			answer = add(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif tokens[0] == '-':
			answer = subtract(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif tokens[0] == '*':
			answer = multiply(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif tokens[0] == '/':
			answer = divide(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif tokens[0] == 'square':
			answer = square(int(tokens[1]))
			print(answer)
		elif tokens[0] == 'cube':
			answer = cube(int(tokens[1]))
			print(answer)
		elif tokens[0] == 'power':
			answer = power(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif tokens[0] == 'mod':
			answer = mod(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif tokens[0] == 'q':
			return



main()



# Replace this with your code
