'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program to check whether a given number is an Strong number or not.********\n\n")
num = input("\tEnter The Number To Check Strong number : ")
check = True
strlen = len(num)
for i in range(strlen):
    for j in range(i+1,strlen):
        if(num[i] == num[j] and num[i] != ''):check = False
        
if(check == 1): print("\n\tThe Given Number Is \"Unique Number\" : ", num)
else: print("\n\tThe Given Number Is \"Not Unique Number\" : ", num)



































































#Name Rishabh Patel