import os  # The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory,
import re  # module included with python primarily used for string searching & impulation 

rootdir = "/home/malyadm/python"
regex = re.compile('(.*py$)|(.*tar$)')

for root,dirs,files in os.walk(rootdir): 
  for file in files: 
   if regex.match(file): 
       print("/home/malyadm/python",file)     