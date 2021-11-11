'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program to check whether a given number is an Perfect number or not.********\n\n")
num = int(input("\tEnter The Number To Check Perfect number : "))
count = 0
for i in range(1,num):
    if(num%i == 0):count = count+i
        
if(num == count): print("\n\tThe Given Number Is \"Perfect Number\" : ", num)
else: print("\n\tThe Given Number Is \"Not Perfect Number\" : ", num)



































































#Name Rishabh Patel