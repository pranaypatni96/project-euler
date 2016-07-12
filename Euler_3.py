"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the 
number 600851475143 ?
"""

def largest_prime_factor(n):
	factors = []
	i = 2
	while i * i <= n:
		while n % i == 0:
			factors.append(i)
			n = n // i
		i += 1
	if n > 1:
		factors.append(n)

	largest = factors[0]
	for j in factors:
		if j > largest:
			largest = j

	return largest

x = largest_prime_factor(600851475143)
print(x)