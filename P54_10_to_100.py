'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def funProduct(start):
    if(start > 100): return 1
    return start*funProduct(start + 10)
print("\t\t**Write a program to create a recursive function to calculate the product of numbers from 10 to 100.**\n\n")

res = funProduct(90)
print("The Sum Is After Calling : ",res)

































































#Name Rishabh Patel