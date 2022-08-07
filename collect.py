from collections import Counter, deque, namedtuple, OrderedDict, defaultdict, ChainMap
# collections module 
# Counters
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))

# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2}))
    
# with keyword arguments 
print(Counter(A=3, B=5, C=2))
# OrderedDict
  
  
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
    
print('Before Deleting')
# for key, value in od.items(): 
    # print(key, value) 
      
# deleting element
od.pop('a')
  
# Re-inserting the same
od['a'] = 1
  
print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)
# DefaultDict
# ChainMap
  
from collections import ChainMap 
     
     
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d4 =  {'l':2 , 'p': 7}
  
# Defining the chainmap 
c = ChainMap(d1, d2, d3).new_child(d4)
print(c.keys())
print(c)
# NamedTuple
Movie = namedtuple("Movies", ["title", "rating", "length"])
M = Movie("Prey", 9.48, 120)

li = ["Luck", 8.90, 170]
luck = Movie._make(li)
print(luck)
print(M.rating)
# DeQue
de = deque(["meta", "amazon", "apple", "netlify"])
print("Deque before insertion", de)
de.appendleft("google")
print("Deque after insertion", de)
de.pop()
print(de)
de.popleft()
print(de)
# UserDict

# UserList

# UserString