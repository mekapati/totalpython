# strong number
def strongnum(my_num):
  my_sum=0
  temp = my_num
  while(my_num):
    i=1
    fact=1
    remainder = my_num%10
    while(i<=remainder):
     fact=fact*i
     i = i+1
    my_sum = my_sum+fact
    my_num = my_num//10
  if(my_sum == temp):
      print("the number is a strong number")  
  else:
      print("the number is not a strong number")

my_num = int(input("enter a number: "))
print("the number is:",my_num)
strongnum(my_num)