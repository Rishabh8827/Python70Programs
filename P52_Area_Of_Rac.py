'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def AreaOfRactangle(w,l):
    return w*l
def callThreeTime(w,l,h):
    return 2*((w*l)+(h*l)+(h*w))
print("\t\t**Write a function that returns the middle value among three integers. (Hint: make use of min() and max()).  Write code to test this function with different inputs.**\n\n")

w = int(input("Enter Width of ractangle: "))
l = int(input("Enter Length of ractangle : "))
h = int(input("Enter Height of ractangle : "))
print("The Area Of Ractangle is : ",AreaOfRactangle(w,l))
print("The Area Of Ractangular Solid is : ",callThreeTime(w,l,h))

































































#Name Rishabh Patel