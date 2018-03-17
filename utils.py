def is_even(n):
	return n % 2 == 0


def is_odd(n):
	return n % 2 > 0


def get_prime_factors_list(n):
	if n < 3:
		return [n]

	prime_factors = []
	i = 2

	while i <= n:
		while n % i == 0:
			prime_factors.append(i)
			n = n / i

		i += 1

	return prime_factors
