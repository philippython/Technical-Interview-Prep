class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.email = "%s+%s@gmail.com" % (firstname, lastname)
        self.salary = salary
    

    def raiseSalary(self, salary):
        self.salary = salary


class Developer(Employee):

    def __init__(self, firstname, lastname, salary, programming_lang):
        super().__init__(firstname, lastname, salary)
        self.programming_language = programming_lang



