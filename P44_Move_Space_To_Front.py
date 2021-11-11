'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("**Write a Python program to move spaces to the front of a given string.**\n\n")
string = input("Enter A String : ")
count = ""
myList = list(string)
for i in range(len(string)):
    if(myList[i] == " "): count = count+"-"; myList[i] = ""
newString = ''.join(myList)
finalString = count + newString
print("The String After Removing Spaces is : ",finalString)

# [Note:- "-" equals to "<space>"]































































#Name Rishabh Patel