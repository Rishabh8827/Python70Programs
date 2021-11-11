'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def  Is_ArmStrong(num):
    ArmStrong = 0
    inNumber = int(num)
    strlen = len(num)
    for i in range(strlen):
        ArmStrong = ArmStrong + int(num[i])**strlen
    if(inNumber == ArmStrong): return True
    else: return False


print("\t\t**Write a Python function that checks whether a passed interger is armstrong or not.**\n\n")
num = input ("Enter a number :")
if Is_ArmStrong(num):
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")

































































#Name Rishabh Patel