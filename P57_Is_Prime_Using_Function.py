'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def isPrime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             

print("\t\t**Write a Python function to check whether the given integer is a prime number or not.**\n\n")

print("Is Prime : ",isPrime(17))

































































#Name Rishabh Patel