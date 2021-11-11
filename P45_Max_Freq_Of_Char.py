'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to find the maximum occurring character in a given string.********\n\n")
string = input("Please Enter String : ")
dict = {}
for s in string:
    keys = dict.keys()
    if s in keys:
        dict[s] += 1 
    else:
        dict[s] = 1
res = max(dict,key = dict.get)
print("The Max Frequency Of Charcters Is : ",res)

































































#Name Rishabh Patel