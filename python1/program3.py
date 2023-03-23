# Accept 5 numbers and sort them in ascending order

NumList = []

Number = int(input("enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("Element After Sorting List in Ascending Order is : ", NumList)
 
