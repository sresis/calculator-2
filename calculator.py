"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce

#function to determine if the number inputs are valid
def valid_input_check(nums):
	for num in nums:
		if not num.isdigit():
			return False
	return True

def main():
	# test
	print(reduce(subtract, [1, 2, 3, 4]))
	#main function to perform calculations
	while True:
		input_string = input()
		tokens = input_string.split()
		operator, *nums = tokens
		#checks to make sure operator is valid
		approved_operators = ['+', '-', '*', '/', 'square', 'cube', 'power', 'mod', 'q']
		# operation to convert each num in nums to a float
		modified_nums = []
		for num in nums:
			modified_nums.append(float(num))
		# determine if nums input is not valid (is not a digit)
		if operator in approved_operators and valid_input_check(nums):
		# can put print function at end instead of in each if statement
			if operator == '+':
				answer = reduce(add, modified_nums)
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
			print('Invalid input. Please try again')



main()



# Replace this with your code
