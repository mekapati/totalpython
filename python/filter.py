numList = [30, 2, -15, 17, 9, 100]
print(type(numList))

greater_than_10 = filter(lambda n: n > 10, numList)

print(greater_than_10)