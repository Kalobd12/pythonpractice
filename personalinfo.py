# PersonalData class holds data about personal information.
class PersonalData:
    # The __init__ method initializes the attributes.
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    # The set_name method accepts an argument for the persons name.     
    def set_name(self, name):
        self.__name = name
    # The set_address method accepts an argument for the persons address.
    def set_address(self, address):
        self.__address = address
    # The set_age method accepts an argument for the persons age.
    def set_age(self, address):
        self.__age = age
    # The set_phone_number method accepts an argument for the persons phone number.
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    # The get_name method returns the persons name.   
    def get_name(self):
        return self.__name
    # The get_address method returns the persons address.
    def get_address(self):
        return self.__address
    # The get_age method returns the persons age.
    def get_age(self):
        return self.__age
    # The get_phone_number method returns the persons phone number.
    def get_phone_number(self):
        return self.__phone_number
    
