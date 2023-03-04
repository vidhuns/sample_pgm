import pprint
message = "vidhun"
new_dict={} # its empty  dictionary

for char in message:
    new_dict.setdefault(char, 0)
    new_dict[char] = new_dict[char] + 1

pprint.pprint(new_dict)
