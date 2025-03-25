"""
UNIVERSITY QUESTION: JUNE 2023 (3 marks)
Write a Python program to count number of even numbers and odd numbers in
a given set of n numbers.
"""
even_c=0
odd_c=0
n=int(input("ENTER COUNT OF NUMBER:"))
print("ENTER  THE NUMBERS ")
for i in range(n):
	x=int(input())
	if x%2==0:
		even_c+=1
	else:
		odd_c+=1
print(f"COUNT OF EVEN NUMBERS:{even_c}")
print(f"COUNT OF ODD NUMBERS:{odd_c}")
