'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def fact(n):
    if(n <= 0): return 1
    return n*fact(n-1)
print("\t\t**Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts  the number as an argument.**\n\n")
n = int(input("Enter The Number : "))
res = fact(n)
print("The Factorial Of Number Is : ",res)

































































#Name Rishabh Patel