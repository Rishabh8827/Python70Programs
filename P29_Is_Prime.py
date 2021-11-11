'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program to check whether a given number is an Prime number or not.********\n\n")
num = int(input("\tEnter The Number To Check Prime number : "))
check = True
if(num == 1):check = False 
for i in range(2,num):
    if(num%i == 0):check = False
if(check): print("\n\tThe Given Number Is \"Prime Number\" : ", num)
else: print("\n\tThe Given Number Is \"Not Prime Number\" : ", num)



































































#Name Rishabh Patel