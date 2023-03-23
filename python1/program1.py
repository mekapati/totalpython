# accept a number from the user, display whether if it is  strong number or not.

my_sum = 0
my_num = int(input("Enter  number:"))
print("The number is")
print(my_num)
temp = my_num
while(my_num):
   i=1
   fact=1
   remainder = my_num%10
   while(i<=remainder):
     fact=fact*1
     i = i+1
   my_sum = my_sum+fact
   my_num = my_num//10
if(my_sum == temp):
     print("The number is a strong number")    
else:
     print("The number is not a strong number")  

