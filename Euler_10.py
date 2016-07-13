"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

(not an efficient method)
"""

def sum_of_primes(n):
	def is_prime(k):
		for j in range(2, k):
			if k % j == 0:
				return False
		return True

	total = 0
	for i in range(2, n):
		if is_prime(i):
			total += i

	return total

x = sum_of_primes(2000000)
print(x)