'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def x(n):
    return n^2 + 1

print("\t\t********Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'.********\n\n")

string = "Y-tatata-acropolis:0.8475"
finding = string.find("0.8475")
sliced = slice(finding,len(string),1)
newstr = string[sliced]
floated = float(newstr)
print("The str is : ",string)
print("The float is : ", newstr)

































































#Name Rishabh Patel