import os
fp = open("C:\Vidhun\Learning\python\example_pgms\est.txt", "w+")
fp.write("inserting a line into the file")

print(fp.name)
print(fp.closed)
#s = fp.read(5)
print(fp.tell())
#print(s)
fp.close()
os.rename ("C:\Vidhun\Learning\python\example_pgms\est.txt", "C:\Vidhun\Learning\python\example_pgms\file1.txt")
