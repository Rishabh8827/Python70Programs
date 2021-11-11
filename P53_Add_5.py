'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def outer_fun(a, b, c):
    def addition(a, b, c):
        return a + b + c
    add = addition(a, b, c)
    return add + 5
print("\t\t**Create an outer function that will accept three parameters, a, b and c**\n\n")

a = int(input("Enter First Number: "))
b = int(input("Enter second Number : "))
c = int(input("Enter Third Number : "))
print("The Sum Is After Calling : ",outer_fun(a,b,c))

































































#Name Rishabh Patel