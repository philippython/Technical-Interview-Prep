student = [ ("Aitch" ,"computer engineering") ,  ("philip", "eduaction") ] 
a = 3
a = 9
print(a)
print(student[0][0])
student.append(("maryam", "HR"))
print(student)

diction = {"input.txt" : "Randy", "code.py" : "stan" , "output.txt": "Randy"}

print(diction.values())
def group_by_name(dicitionary):
    names = set(dicitionary.values())
    print(names)
    # return { owner: file for (owner,file) in names }
    # return {owner: file_list.append(file) for (file, owner) in names if owner == file}



group_by_name(diction)
# group_by_name =  { file: owner for (file, owner) in diction}
# name = "philip", "kola", "john"
# print(name.count("kola"))
# name = "johjhfln"
# print(bytes(name, "utf-8"))
# print(name[2])
sets = set([3, 8, 8, 3, 0, 5, 6, "p"])
print(sets)
sets.remove(0)
sets.update("k")
print(sets)
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list[x])

# def function(b):
#     return 10 % b

# y = map(function, (5, 2))
# print(list[y])
num = [7]