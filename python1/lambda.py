# lambda function to print even number in the given range

evennumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

even= filter(lambda n : n%2==0, evennumber)
odd= filter(lambda n : n%2!=0, evennumber  )
square= map(lambda n : n**2, evennumber)

print(even)
print(odd)
print(square)