'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program to check whether a given number is a palindrome or not********\n\n")
string = input("\tEnter The String To Check Palindrome : ")
reverse = ""
strlen = len(string)
for i in range(strlen):
    reverse = reverse + string[strlen - i - 1]
if(string == reverse): print("\n\tThe Given String Is \"Palindrome\" : ", reverse ," = ", string)
else: print("\n\tThe Given String Is \"Not Palindrome\" : ", reverse ," != ", string)



































































#Name Rishabh Patel