# armstrong number 
def armstrong(n):
   s = n
   b = len(str(n)) 
   sum1 = 0
   while n != 0:
     r = n%10
     sum1 = sum1+(r**b)  #power(exponential operator)
     n = n//10
   if s == sum1:
      print("the given number", s, "is armstrong number")   
   else:
     print("the given number", s, "is not armstrong number")

print("enter a number:")     
n=int(input())
armstrong(n)