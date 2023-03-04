import re
a = "cat is better than dog but cat is not that good dog"
matchobj = re.match('dog', a)
if matchobj:
 print(matchobj.group(0))
else:
 print("No match for dog")
matchobj1 = re.search(r'dog', a)
if matchobj1:
 print(matchobj1.group())