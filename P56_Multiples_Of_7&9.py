'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''
myList = []
def multiOfsevAndNine(start):
    if(start > 500):return
    if(start%7 == 0 and start%9 == 0):myList.append(str(start))
    return multiOfsevAndNine(start+1)
print("\t\t**Write a Python function to display all the multiples of 7 & 9 within the range 100 to 500.**\n\n")
multiOfsevAndNine(100)
final = ','.join(myList)
print("The Multiples are : ",final)

































































#Name Rishabh Patel