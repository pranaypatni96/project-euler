"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10001st prime number?

(not an efficient method)
"""

def nth_prime(n):
	def prime(m):
		for i in range(2, m):
			if m % i == 0:
				return False
		return True

	counter = 0
	j = 2
	while counter < n:
		if(prime(j)):
			counter += 1
		j += 1
	return j - 1

x = nth_prime(10001)
print(x)

