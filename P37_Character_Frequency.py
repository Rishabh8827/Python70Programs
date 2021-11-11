'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to count the number of characters (character frequency) in a string********\n\n")
string = input("Please Enter String : ")
dict = {}
for s in string:
    keys = dict.keys()
    if s in keys:
        dict[s] += 1 
    else:
        dict[s] = 1
print("The Frequency Of Charcters Is : ",dict)

































































#Name Rishabh Patel