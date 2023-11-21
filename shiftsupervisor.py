import employee
#
class ShiftSupervisor(employee.Employee):
    #
    def __init__(self, name, number, salary, production_bonus):
        #
        employee.Employee.__init__(self, name, number)
        #
        self.__salary = salary
        #
        self.__production_bonus = production_bonus
    #    
    def set_salary(self, salary):
        self.__salary = salary
    #
    def set_production_bonus(self, production_bonus):
        self.__production_bonus = production_bonus
    #
    def get_salary(self):
        return self.__salary
    #
    def get_production_bonus(self):
        return self.__production_bonus