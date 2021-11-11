'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to get a single string from two given strings, separated by a space and swap the first  characters of each string********\n\n")
physics = int(input("Enter Physics Marks : "))
chemistry = int(input("Enter chemistry Marks : "))
biology = int(input("Enter biology Marks : "))
mathematics = int(input("Enter mathematics Marks : "))
computer = int(input("Enter computer Marks : "))

total = physics+chemistry+biology+mathematics+computer
percentage = total/5
print("\nYour Percentage Is : ",percentage,"%")
if(percentage >= 90): print("Your Grade Is : \"A(Pass)\"")
elif(percentage >= 80): print("Your Grade Is : \"B(Pass)\"")
elif(percentage >= 70): print("Your Grade Is : \"C(Pass)\"")
elif(percentage >= 60): print("Your Grade Is : \"D(Pass)\"")
elif(percentage >= 40): print("Your Grade Is : \"E(Pass)\"")
else: print("Your Grade Is : \"F(Fail)\"")



































































#Name Rishabh Patel