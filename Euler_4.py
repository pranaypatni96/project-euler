"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the 
product of two 3-digit numbers.
"""

def largest_palindrome(n):
	largest = 0
	for i in range(10**(n-1), 10**n):
		for j in range(10**(n-1), 10**n):
			k = i * j
			if is_palindrome(k) and k > largest:
				largest = k
	return largest

def is_palindrome(y):
	num = y
	opp = 0
	while y > 0:
		d = y % 10
		opp = opp * 10 + d
		y = y / 10
	return num == opp

x = largest_palindrome(3)
print(x)