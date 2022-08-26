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

# def is_valid_walk(walk):
#     #determine if walk is valid
#     walk_time = len(walk)
#     routes = set(walk)
#     print(routes)
#     if walk_time <= 10:
#         return True
#     else:
#         return False

# def is_valid_walk(walk):
#     #determine if walk is valid
#     ns, ew = 0, 0
#     if len(walk) == 10:
#         for i in walk:
#             if i == 'n': ns+=1
#             if i == 's': ns-=1
#             if i == 'w': ew+=1
#             if i == 'e': ew-=1
#     else:
#         return False
#     return ns == 0 and ew == 0

from math import sqrt
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if isinstance(sq, int):
        sqr = sqrt(sq)
        next = sqr + 1
        return  next ** next
    else:
        return -1

print(find_next_square(1219))