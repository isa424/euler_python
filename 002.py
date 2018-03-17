# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued terms.
import utils

sumOfFib = 0
first = 1
second = 2

while second <= 4e6:
	if utils.is_even(second):
		sumOfFib += second

	first, second = second, first + second

print("%d" % sumOfFib) # 4613732
