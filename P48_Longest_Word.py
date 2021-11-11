'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
def longest_word(myList):
    length = []
    for n in myList:
        length.append((len(n),n))
    length.sort()
    return length[-1][0], length[-1][1]

print("\t\t********Write a Python program to capitalize first and last letters of each word of a given string********\n\n")
myList = ["hello","hii","welcome"]
longest = longest_word(myList)
print("List : ",myList)
print("The longest word Is : ",longest[1])
print("The Length of longest word Is : ",longest[0])
































































#Name Rishabh Patel