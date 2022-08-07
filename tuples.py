#create a tuple
tuplex = ("w", "3", "r", "e", "s", "o", "u", "r", "c", "e") 
print(tuplex.count("e"))
#get item (4th element)of the tuple by index
item = tuplex[3]
print(item)

#get item (4th element from last)by index negative
item1 = tuplex[-4]
print(item1)

from copy import deepcopy

deep_tuple = deepcopy(item)
print("".join(tuplex))