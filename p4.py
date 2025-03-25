"""
UNIVERSITY QUESTION:MAY 2023 (7 marks)
Write a Python program to check whether a number is Armstrong number or not.
An Armstrong number is an n-digit number that is equal to the sum of the n
th
powers of its digits.
Examples: 153 = 1^3+ 5^3+ 3^3, 1634= 1^4+ 6^4+ 3^4+ 4^4

"""
n=input("ENTER A NUMBER:")
l=len(n)
sum=0
x=int(n)
n=x
while x>0:
	digit=x%10
	x=x//10
	sum+=digit**l
if n==sum:
	print(f"{n} IS  AN ARMSTRONG NUMBER")
else:
	print(f"{n} IS NOT AN ARMSTRONG NUMBER")
