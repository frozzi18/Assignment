class Employee:
    def __init__(self, name, base_pay, hours_worked):
        self.name = name
        self.base_pay = base_pay
        self.hours_worked = hours_worked

    def salary(self):
        salary = self.base_pay*self.hours_worked
        print("Total salary for "+self.name+" is "+str(salary)+" dollar")


class Manager(Employee):
    def __init__(self, name, base_pay, hours_worked, office_number):
        Employee.__init__(self, name, base_pay, hours_worked)
        self.officeNumber = office_number

    def office_number(self):
        print("The office number for ", self.name, " is ", self.officeNumber)


John = Employee("John", 7.5, 38)
Annabel = Employee("Annabel", 8.2, 42)
Graham = Employee("Graham", 10.50, 41)
Bill = Manager("Bill", 15.50, 39, "A332")
Gregory = Manager("Gregory", 18.20, 40, "A415")

John.salary()
Annabel.salary()
Graham.salary()
Bill.salary()
Bill.office_number()
Gregory.salary()
Gregory.office_number()