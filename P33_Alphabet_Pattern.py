'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program To Print following pattern: A BB CCC DDDD EEEEE FFFFFF GGGGGGG HHHHHHHH********\n\n")
num = int(input("\t\t\t\tEnter The Number(< 26) : "))#to print Above Pattern Input '8'
myint = 65
char = chr(myint)
for i in range(1,num+1):
    if(i > 26): break
    for j in range(i):
       print(char,end = '')
       
    myint = myint+1
    char = chr(myint)
    print('')


































































#Name Rishabh Patel