'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def middle(a,b,c):
    mini = min(a,b,c)
    maxi = max(a,b,c)
    if(mini != a and maxi != a): return a 
    elif(mini != b and maxi != b): return b 
    else: return c

print("\t\t**Write a function that returns the middle value among three integers. (Hint: make use of min() and max()).  Write code to test this function with different inputs.**\n\n")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
print("The middle is : ",middle(a,b,c))

































































#Name Rishabh Patel