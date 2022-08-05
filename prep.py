class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.email = "%s%s@gmail.com" % (firstname, lastname)
        self.salary = salary
    

    def raiseSalary(self, salary):
        self.salary += salary


class Developer(Employee):

    def __init__(self, firstname, lastname, salary, programming_lang):
        super().__init__(firstname, lastname, salary)
        self.programming_language = programming_lang

    def addLang(self, lang):
        self.programming_language += [lang]
employee1 = Employee('philip', 'odulaja', 13000)
# print(employee1.email)

employee1.raiseSalary(3444)
# print(employee1.salary)

dev1 = Developer('philip', 'odulaja', 13000, ['python'])
dev1.addLang('Nodejs')
# print(dev1.programming_language)

# lists and list comprehension
string = "Practice Problems to Drill List Comprehension in Your Head."

numbers = [num for num in range(1, 1001)]
numbers_divisible_by_8 = [ num for num in numbers if num % 8 == 0]
numbers_has_six = [ num for num in numbers if "6" in str(num) ]
# print(numbers_has_six)
# print(numbers_divisible_by_8)

empty_spcae = [ space for space in string if space == " "]
# print(len(empty_spcae))

vowels = [alpha for alpha in string if alpha in ["a", "e", "i", "o", "u" ] ]
words = [ word for word in string.split(" ") ]
print(words)
less_than_five = [letter for letter in words if len(letter) <= 4]
letters_lenght = [ len(letter) for letter in words ]
print(less_than_five)
print(letters_lenght)
print(len(vowels), len(string))
