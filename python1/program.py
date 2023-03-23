#display common factors for the given multiple parameters/inputs.

a = 10
b = 50
n = 0 
z = [] 
for i in range(1,min(a,b)+1):
    if a%i==b%i==0:
       n+=1
       z.append(i)
    print("common factors for given inputs:",z)
    print("no of common factors:",n)
