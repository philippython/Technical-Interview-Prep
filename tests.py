# unordered_list = ["I>E", "M>I", "A>M", "D>A", "E>N"]

# def findWord(array):
#     list = [n.replace('>', "") for n in array ]
#     return list

# def sorter(unordered_array):
#     new_list = []
#     for n in unordered_array:
#         new_list.extend(n.split(">"))
#     return list(set(new_list))

# #
# word = findWord(unordered_list)
# print(word)
# letters = sorter(unordered_list)
# print(letters)

# final_word = []
# for alphabet in letters:
#     for n in word:
#         if alphabet == n[0]:
#                 if alphabet == n[1]:
#                     print(alphabet)
#                     del word[word.index(n)]
#                     final_word.append(alphabet)
# print(final_word)


# 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
# print(position)
# # Write your code below this row
#  # 👇
# horizontal = int(position[0])
# # horizontal = 32[0] = 3
# vertical = int(position[1])
#  vertical = 32[1] = 2

# # selected_row = map[ 2 - 1]
# # map[1]
# selected_row = map[vertical-1]
# # selected_row[3 - 1]
# # selected_row[2]
# selected_row[horizontal-1] = 'x'
#
#
# print(f"{row1}\n{row2}\n{row3}")
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below


from math import sqrt


file = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}


def group_by_owners(files):
    new_dict = {}
    for k, v in files.items():
        if  v in new_dict.keys():
            new_dict[v] = new_dict[v] + [k]
        else:    
            new_dict[v] = [k]

        
    return new_dict


print(group_by_owners(file))
# def find_roots(a, b, c):
#     ans1 = sqrt(-b ** 2 + 4 * a * c)  / 2 * a
#     return ans1

# print(find_roots(2, 10, 8))
# class IceCreamMachine:
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings
#         self.result = []

#     def scoops(self):
#         if self.ingredients != []:
#             for ingredients in self.ingredients:
#                 new = [ingredients] + self.toppings
#                 self.result.append(new)
#             return self.result
#         return self.result

        
            


# machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
# def unique_names(names1, names2):
#     return list(set(set(names1).union(set(names2))))



# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia







