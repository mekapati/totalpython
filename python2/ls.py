pos = -1 

def serach(list, n): 
    i = 0 

    while i< len(list): 
       if list[i] == n:
           globals()['pos'] = i 
           return True 
       i = i + 1 
    return False 

list = [5,8,4,6,9,2]
n = 9 

if serach(list, n): 
    print("found at ", pos+1)
else:
    print("Not Found")    
