'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to remove the characters which have even index values of a given string********\n\n")
string = input("Please Enter String : ")
myList = list(string)
for i in range(len(string)):
    if(i%2 == 0): myList[i+1] = ''
newString = ''.join(myList)
print("The New String Is : ",newString)
































































#Name Rishabh Patel