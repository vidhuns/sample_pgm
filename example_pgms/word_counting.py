import re
count=0
fp = open(r'C:\Vidhun\Learning\python\example_pgms\test.txt', "r+")
save = fp.readlines()
print(save)
for item in save:
   match = len(re.findall('vidhun', item, re.I))
   count+= match
print (count)