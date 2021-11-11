'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("**Write a Python program to count occurrences of a substring in a string.**\n\n")
string = input("Enter A String : ")
num = int(input("Enter A Number To Lowecase : "))
ascii  = 0
newString = ""
for i in range(len(string)):
    if(i < num):ascii = ord(string[i])+32; newString += chr(ascii)
    else: newString += string[i]
print("The Number Of SubString in Given String is : ",newString)
































































#Name Rishabh Patel