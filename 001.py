# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
my_sum = 0
start = 0
end = 1000

for i in range(start, end, 3):
	my_sum += i

for i in range(start, end, 5):
	my_sum += i

for i in range(start, end, 15):
	my_sum -= i

print("%d" % my_sum)  # 233168
