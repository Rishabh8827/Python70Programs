'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to capitalize first and last letters of each word of a given string********\n\n")
string = input("Please Enter String : ")
myList = list(string)
first = ""+string[0].upper()
last = ""+string[len(string)-1].upper()
myList[0] = first
myList[len(string)-1] = last
newString = ''.join(myList)
print("The Max Frequency Of Charcters Is : ",newString)

































































#Name Rishabh Patel