import re
out = re.split("and", "vidhun and vidhun and sahayaraj")
print(out)
print(out[0])
out1= re.findall("and", "vidhun and vidhun and sahayaraj")
print(out1)
#out2= re.find("and", "vidhun and vidhun and sahayaraj")
#print(out2)