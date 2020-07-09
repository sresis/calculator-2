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
			if operator == 'q':
				print('you have exit the game')
				return
			elif  operator == '+':
				answer = reduce(add, modified_nums)
			elif operator == '-':
				answer = reduce(subtract, modified_nums)
			elif operator == '*':
				answer = reduce(multiply, modified_nums)
			elif operator == '/':
				answer = reduce(divide, modified_nums)
			elif operator == 'square':
				answer = square(int(tokens[1]))
			elif operator == 'cube':
				answer = cube(int(tokens[1]))
			elif operator == 'power':
				answer = power(int(tokens[1]), int(tokens[2]))
			elif operator == 'mod':
				answer = mod(int(tokens[1]), int(tokens[2]))
			print(answer)
		# if operator is not valid, print failure message
		else:
			print('Invalid input. Please try again')



main()



# Replace this with your code
