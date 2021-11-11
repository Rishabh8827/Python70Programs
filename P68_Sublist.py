'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046
'''
def sub_lists (l):
	lists = [[]]
	for i in range(len(l) + 1):
		for j in range(i):
			lists.append(l[j: i])
	return lists
print("\t\t**Python program to insert a number to given position in a list.**\n\n")
list = [11, 5, 17, 18, 23]
print("List : ",list)
print("Sublist Of List : ",sub_lists(list))

































































#Name Rishabh Patel