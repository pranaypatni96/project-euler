"""
2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without 
any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

(brute force solution)
"""

i = 2520
while True:
	if ( i%1==0 and i%2==0 and i%3==0 and i%4==0 and
		 i%5==0 and i%6==0 and i%7==0 and i%8==0 and
		 i%9==0 and i%10==0 and i%11==0 and i%12==0 and
		 i%13==0 and i%14==0 and i%15==0 and i%16==0 and
		 i%17==0 and i%18==0 and i%19==0 and i%20==0):
			break
	else:
		i += 2520

print(i)

