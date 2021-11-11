'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to change a given string to a new string where the second and last chars have been  exchanged********\n\n")
string = input("Please Enter String : ")
myList = list(string)
temp = myList[1]
myList[1] = myList[len(string) - 1]
myList[len(string) - 1] = temp

newString = ''.join(myList)

print("The New String Is : ",newString)
































































#Name Rishabh Patel