import string

alphabet = set(string.ascii_lowercase)
sentence = input("Enter a sentence: ")    
sentence = sentence.lower() 
missing = ''
for letter in  alphabet: 
  if letter not in sentence: 
    missing = missing+letter 
if (len(missing)!=0): 
  print("missing", missing)
else: 
  print("letter")                     
