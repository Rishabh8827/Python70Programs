'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a program to Check Is student is allowed to sit in exam or not.********\n\n")
classes = int(input("Please Enter The Total Number Of Classes : "))
clsAttend = int(input("Please Enter The Total Number Of Classes Attended : "))

percentage = (clsAttend*100)/classes

print("\nYour Attendence Percentage Is : ", percentage,"%")

if(percentage >= 80):print("\nCongrats! You Are \"Eligible\" To Sit In Exam..")
else:print("\nSorry! You Are \"Not Eligible\" To Sit In Exam..")

































































#Name Rishabh Patel