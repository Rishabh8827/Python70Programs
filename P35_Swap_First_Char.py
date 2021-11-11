'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a Python program to get a single string from two given strings, separated by a space and swap the first  characters of each string********\n\n")
string1 = input("\tEnter The First String : ")
string2 = input("\tEnter The Second String : ")
strlist1 = list(string1)
strlist2 = list(string2)
temp1 = strlist1[0]
strlist1[0] = strlist2[0];
strlist2[0] = temp1

string1 = ''.join(strlist1)
string2 = ''.join(strlist2)
print("\n\tThe String Is : ", string1 + " " + string2)




































































#Name Rishabh Patel