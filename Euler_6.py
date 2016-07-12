"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""

def dif_sum_square(n):
	sum_of_squares = 0
	sums = 0
	for i in range(1, n+1):
		sum_of_squares += i**2
		sums += i

	return sums**2 - sum_of_squares

x = dif_sum_square(100)
print(x)

