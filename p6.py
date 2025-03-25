"""
UNIVERSITY QUESTION:MAY 2024(7 marks)
Write a python program to find out the eldest and youngest of three individuals ,
with their ages being input through the keyboard.(without using max, min
functions)
"""
age1=int(input("ENTER TH EAGE OF FIRST PERSON:"))
age2=int(input("ENTER THE AGE OF SECOND PERSON:"))
age3=int(input("ENTER THE AGE OF THIRD PERSON:"))
if age1>age2 and age1>age3:
	print("FIRST PERSON IS ELDEST")
elif age2>age1 and age2>age3:
	print("SECOND PERSON IS ELDEST")
else:
	print("THIRD PERSON IS ELDEST")
if age1<age2 and age1<age3:
	print("FIRST PERSON IS YOUNGEST")
elif age2<age1 and age2<age3:
	print("SECOND PERSON IS YOUNGEST")
else:
	print("THIRD PERSON IS YOUNGEST")
