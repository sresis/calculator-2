"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def main():

	while True:
		input_string = input()
		tokens = input_string.split()
		operator, *nums = tokens
		#checks to make sure operator is valid
		approved_operators = ['+', '-', '*', '/', 'square', 'cube', 'power', 'mod', 'q']
		if operator in approved_operators:
		# can put print function at end instead of in each if statement
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
		# if operator is not valid, print failure message
		else:
			print('Invalid operation. Please try again')



main()



# Replace this with your code
