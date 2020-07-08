"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def main():

	while True:
		input_string = input()
		tokens = input_string.split()
		operator, nums* = tokens
		if operator == '+':
			answer = add(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif operator == '-':
			answer = subtract(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif operator == '*':
			answer = multiply(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif operator == '/':
			answer = divide(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif operator == 'square':
			answer = square(int(tokens[1]))
			print(answer)
		elif operator == 'cube':
			answer = cube(int(tokens[1]))
			print(answer)
		elif operator == 'power':
			answer = power(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif operator == 'mod':
			answer = mod(int(tokens[1]), int(tokens[2]))
			print(answer)
		elif operator == 'q':
			return



main()



# Replace this with your code
