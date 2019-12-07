import pdb

class Name:
    class_variable = 'name_test'

    def __init__(self, first_name, last_name):
        # constructor to pass in first_name and last_name
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        print(self.first_name)

    def get_last_name(self):
        print(self.last_name)

    def hello(self):
        print('hello', self.first_name, self.last_name)

    @staticmethod
    def say_hi():
        # by itself, does not use anything inside the class.
        # use this when you want the function by itself.
        # don't need to initialize
        print('saying hi')

    @classmethod
    def say_hi_class(cls):
        # class method allows you to use class variables.
        # don't need to initialize
        print(cls.class_variable)



# # initialize
# name = Name(first_n`ame='Huy', last_name='Truong')

# name.get_first_name()
# name.get_last_name()

# print(name.first_name)

# another_name = Name(first_name='Test', last_name='test123')

# another_name.get_first_name()

# Name.say_hi()

# Name.say_hi_class()



### Class inhieritance

class BaseName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name


class CoolName(BaseName):
    def __init__(self, first_name, last_name, date_of_birth):
        super().__init__(first_name, last_name)
        self.date_of_birth = date_of_birth

    def get_date_of_bith(self):
        return self.date_of_birth



cool_name = CoolName(first_name='Huy', last_name='Truong', date_of_birth='12345')

print(cool_name.get_date_of_bith())