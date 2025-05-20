#Inhertiance concept

#In python inheritance is very important topic and in Python all classes use inheritance by default
# All classes inherit Object by default
class A():
    pass

class B(object):
    pass
#  Above both the class A and B are same and have same functionality
#  Here Object is the super or parent class and B is the sub or derived class

class Person():
    static_value=0
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        
    
class Employee(Person):
    all_employee=[]
    
    def __init__(self, fname, lname, empId):
        Person.__init__(self, fname, lname)
        self.empId=empId
        print(Employee.static_value)
        Employee.sample(self)
        # self.sample()
        # Can also be written. The Sample() method gets called and self parameter will be passed 
        
        # In order to store the values of all the instances we  can append/add the value in the _init_ function only
        # Employee.all_employee.append(self)
         

    def sample(self):
        Employee.all_employee.append(self)
    
    @staticmethod
    def total():
        for i in Employee.all_employee:
            print(i.fname, i.lname)

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in Employee.all_employee:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees
    
# Here is the explanation of the code.
#  First Class Person() is created and it has 2 attributes "fname" and "lname"
# These attributes are initialized by the __init__function


# Now in class Employee def __init__ function is passed with 3 attributes( paramaters)"fname", "lname", "empId"
# Then the Person.init(self, fname, lname ) function is called and these parameters are passed
# hence, attributes of class Employee are initialized by the init function of the Person
# Then as emp.Id is an another arrtibute and is initiailized inside the init function of Person class
emp1 = Employee("Alice", "Smith", "E001")
emp2 = Employee("Bob", "Johnson", "E002")
emp3 = Employee("Charlie", "Brown", "E003")
# print(emp1.fname)
# print(emp2.fname)
# print(emp2.fname)
Employee.total()
employee_list_instance = EmployeesList([emp1, emp2, emp3]) # Create an instance of EmployeesList with Employee objects
search_results = employee_list_instance.search("Alice")
print(search_results)