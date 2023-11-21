import employee
#
class ProductionWorker(employee.Employee):
    #
    def __init__(self, name, number, shift_number, pay_rate):
        #
        employee.Employee.__init__(self, name, number)
        #
        self.__shift_number = shift_number
        #
        self.__pay_rate = pay_rate
    #    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    #
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    #
    def get_shift_number(self):
        return self.__shift_number
    #
    def get_pay_rate(self):
        return self.__pay_rate