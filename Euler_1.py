"""
If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_mult(x, y, n):
	rv = 0;
	for num in range(n):
		if num % x == 0 or num % y == 0:
			rv += num
	return rv

x = sum_mult(3, 5, 1000)
print(x)