'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a program to add 'polis' at the end of given string********\n\n")
string = input("Please Enter String : ")
strlen = len(string)
tempstr = string.lower().find("polis")
if(strlen < 3): print("String After Modification : ",string)
elif(tempstr != -1): print("String After Modification : ",string + "CS")
else: print("String After Modification : ",string + "polisCS")

































































#Name Rishabh Patel