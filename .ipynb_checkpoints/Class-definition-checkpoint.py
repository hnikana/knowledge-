# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


'''
Class Object 
Static Variable: is related to the class itself  ;  raise_amount 
Instance Variable: is related to the instances ; self.first , self.last , …
'''
class Employee:
    raise_amount = 1.04 
    def __init__(self, first, last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def fullname (self):
        return '{} {}'.format (self.first , self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod  # refer to class methods
    def raise_amount(cls, amount ) :
            cls.raise_amount = amount
            
    @classmethod
    def from_string(cls,emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5  or  day.weekday() == 6 :
            return False
        return True
    
    
    
    
    


        
        
# Instance.__dict__ : giving all the instance variable 
#Class.__dict__ : giving all the class variables both instance and static 
    
'''
We can change the static variable of a class by calling 
 class.static_cvariable() = something , and this way obviously it will apply
 to all the instances of that class . 
Also, we van just change a static variable of an instance by calling
 instance.static_variable = something , in that case just that instance will have
 its static_vatriable changed. 
'''

'''
Another useful application for static variable is when you want to keep the track
 or record of something in the class. For example , you want to know how many times
 instances are created from a class, why would we know that ? imagine we want to
 know how many employees we have and obviously the number of employees for all the
 instances should be the same and all should be changed. So , every time an.
 Instance is created on the __init__ method the num_of_employees go up by one.
 However, it could be done in a for loop when the instances are created or through
 any data stream. 
 
Being that said , we can have instance method and class method (static method)
 as well ? 
'''
'''
Regular Methods  : 
They takes in the instance as their argument, the ones which they are defined in
 the class by def regular(self) and while applying them to an instance, they are
 like instance.regular()
'''
'''
CLass Method
-	For class method we have to use decorator to let the class know it is a class
     method 
-	Class method, apparently (not sure yet about the other applications ) are for 
    tweaking the class variables and everything which is related to the class not
    instance. 
-	The function above is more like changing the static variable of a class which
     could be done based on the needs like, the number of employees , or after
     some iteration , etc. 
-	Cls in the function is more like self in regular methods 
-	What is another use of class method? It is something called, alternative
     constructor. What it means is that most of a time we could do some change
     which I want through our static variables as well. But , sometimes we face 
     some sceanrios that fopr initiating the class we need to reform the out
     put , imagin the case in which we face first_last_pay as a string.
     So , in that case there should be another constructor to take care of it. 
     
- So as it is shown above the emp_1 = Employee.from_string(emp_sting) could take care of it . 
- In the class above , the class method , from_string (cls , arg) and return cls(args*)
     meaning that it return the class itself with the proper argument to initialize the class. 
'''
emp_1 = Employee('Corey','Schefer', 50000)

emp_1.raise_amount = 1.06 # setting raise_amount for that especial employee
Employee.raise_amount = 1.05 # Class variable
Employee.raise_amount(1.05) # class method

emp_2 = Employee('leila','tokhmi', 60000)

emp_3 = Employee.from_string('behzad-bokonai-70000') # alternative construction 

'''
Statics Methods
-	In static method , we don’t need any cls, or self as the argument. It is just a normal 
    function within the class as there are some logics in the class necessitate the existence of it. 
-	We usually decorate them with @Staticmethod  and remember we don’t put self (instance) or cls(class)
     as their argument. '
     
-   In the example above, the function is_workday() is a static method and the print statement 
    in the very last line is somehow to test it out. As it is shown it doesnot have anything to 
    do with class and it could be called as a regular function and because it is just a part of a class
    , it should be called by a class . so , here we could understand the difference between class 
    method and static method. 
'''

'''
Class Inheritance:
	Get inheritance from parent and add new method or override the existing methods.
Why is that useful?
	So , imagine we want to create a class for managers and developers , as all of developers and managers are having name , pay and whatever employee class has . So instead of creating a class for each of them , we create a subclass and get inheritance from employee and add (modify) methods. Developer class is a sub_class of Employee.
'''

class Developer(Employee):  # this way we have all the variable and methods of the parent class
    pass

dev_1 = Developer('Corey','Schefer' , 50000)
dev_2 = Developer('Igor','Schefer' , 60000)

print(help(Developer)) # it is really useful to track the class and search the methods 


'''
If we want to have our developers to have 10 percent raise , we can just override the class variable “raise_amount” , raise_amount = 10 % 
Sometimes we want to have sub-class with more info (attribute and methods) , we want to add programming language as another attribute
 to the developer class. SO , in the example below , both , Super method and Employee.__init__ work but the Employee.__init__ should get
 self as its argument as well. So , there is no difference however for single inheritance both work well but for multiple inheritance 
 really we need to stick with Super() method. 
'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# NOw we change the class a little bit by overriding , for that we need ti initialize the class again and get the inheritance fro the parent data 

class Developer(Employee): # this way we have all the variable and methods of the parent class
    raise_amount = 1.10 
    
    def __init__(self, first, last , pay, prog_language):
#        self.first = first  ; we could do that , but we wantto have everything simple 
#        self.last = last
#        self.pay = pay
#        self.email = first+'.'+last+'@company.com'
        super().__init__(first, last , pay)
#        Employee.__init__(self,first, last , pay ) ; we could use this one as well but for multiple inheritance we need to use sper 
        self.prog_language = prog_language
    
dev_1 = Developer('Corey','Schefer' , 50000 , 'python')
dev_2 = Developer('Igor','Schefer' , 60000 , 'java')

# Now we can get the fullname of th edeveloper , it gets inherit from Employee 
dev_1.fullname()

class Manager(Employee):
    
    def __init__(self, first, last , pay, employees = None):
        super().__init__(first, last , pay)
        if employees is None :
            self.employees = []
        else:
            self.employees = employees
                      
    def add_emp (self , emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp (self , emp):
        if emp not in self.employees:
            self.employees.remove(emp)
            
    def print (self) :
        for emp in self.employees:
            print ('---> ' , emp.fullname())
    
        
Mgr_1 = Manager('sue', 'smith', 90000, [dev_1])
print(Mgr_1.email)
print (Mgr_1.print())
Mgr_1.add_emp(dev_2)
print (Mgr_1.print())


isinstance(Mgr_1, Manager) 
isinstance(Mgr_1, Employee)
isinstance(Mgr_1, Developer)

issubclass(Developer, Employee)
issubclass(Manager , Employee)
issubclass(Developer , Manager) 


# Magic Methods 
# __function__ ==> dunder method , like dunder init ; repr and str 
repr (emp_1) ; # more for developers use for debugging 
str(emp_1) ; # more for interface user use  

class Employee:
    raise_amount = 1.04 
    def __init__(self, first, last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    
    @property 
    def email (self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname (self):
        return '{} {}'.format (self.first , self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod  # refer to class methods
    def raise_amount(cls, amount ) :
            cls.raise_amount = amount
        
    @classmethod
    def from_string(cls,emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first,last,pay)
    
   @staticmethod 
    def is_workday(day):
        if day.weekday() == 5  or  day.weekday() == 6 :
            return False
        return True
    # these two functions could be useful to show the info about the object 
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first , self.last , self.pay)
    
    def __str__(self) :
        print ("{} -{}".format(self.fullname , self.email))
    
    def __add__(self, other):
        return int(self.pay) +int( other.pay )
    
    @fullname.setter
    def fullname (self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last 
        
        
    @fullname.deleter
    def fullname (self):
        self.first = None
        self.last = None 
        
        
    
    

emp_1 = Employee('Corey','Schefer', 50000)
emp_2 = Employee('leila','tokhmi', 60000)

emp_3 = Employee.from_string('behzad-bokonai-70000') # alternative construction 


print (emp_1.__repr__())  
print(emp_1.__str__())

print(emp_1.__add__(emp_3))  

'''
Property Decorator - Getter , Setter and Deletter  
Properties are accessed as attributes without parentheses. like self.email
'''         

emp_1.first = 'Jim'   
emp_1.fullname()
emp_1.email()    # Try it first without propert Decorator 
                # here we could see that however we changed the first name, still we have the same old email addresss , how could we fix it ? 
                #         self.email = self.first+'.'+self.last+'@company.com' , still we get the same old email address , An alternative way is to 
                # add a method instead of an attribute , like fullname method. But it is not very useful , because , fisrt of we may need to inform any body
                # who use our class to hey , you need to call that method on that instance , but we need to have it more automatic. 
                # the solution is property decorator , the property decorator we dont need to have paranthesis and without parathesis it works as well .
# Or even we can do that for full name , sometimes people forget to put paranthesis 
                

emp_1.email# here we could see that we face an error 
emp_1.fullname

# So another issue is that , sometimes we need to give a fullname and we need to have every thing , first , last and even email address changed , how ? 
# here is when the setter comes to play 
emp_1.email 
emp_1.fullname = 'Ali Kamali' # Try it without fullname.setter first 
emp_1.email 

# Also sometimes we may need to delet an email but we want to have all the information gine as well. 

del emp_1.fullname

emp_1.email # also we could define a built in function to delet the instance as well


#=============================Built_in DECORATORS ======================================================================
'''
A few built-in class decorators
Some commonly used decorators that are built into Python are @classmethod, @staticmethod, and @property. 
The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that’s not connected 
to a particular instance of that class. The @property decorator is used to customize getters and setters for class attributes. 
Expand the box below for an example using these decorators. You can learn more about built-in decorators here.

'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
    
    
'''
In this class:
.cylinder_volume() is a regular method.
.radius is a mutable property: it can be set to a different value. However, by defining a setter method, we can do some error
 testing to make sure it’s not set to a nonsensical negative number. Properties are accessed as attributes without parentheses.
.area is an immutable property: properties without .setter() methods can’t be changed. Even though it is defined as a method,
 it can be retrieved as an attribute without parentheses.
.unit_circle() is a class method. It’s not bound to a particular instance of Circle. Class methods are often used as factory 
methods that can create specific instances of the class.
.pi() is a static method. It’s not really dependent on the Circle class, except that it’s part of its namespace. Static methods 
can be called on either an instance or the class.
'''

'''
Decorating Classes  https://medium.com/better-programming/decorators-in-python-72a1d578eac4
There are two different ways to use decorators on classes. The first is by decorating the methods of a class or decorating the whole class.
'''
import functools
import time


def timer(func): # it computes the runtime 

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
        return value

    return wrapper


@timer  # on a function 
def doubled_and_add(num):
    res = sum([i*2 for i in range(num)])
    print("Result : {}".format(res))

doubled_and_add(100000)
doubled_and_add(1000000)

'''
Decorate a class method
Here we are using a previously created timer decorator.
'''

class Calculator:

    def __init__(self, num):
        self.num = num

    @timer
    def doubled_and_add(self):
        res = sum([i * 2 for i in range(self.num)])
        print("Result : {}".format(res))

c = Calculator(10000)
c.doubled_and_add()

'''
output
Result : 99990000
Finished 'doubled_and_add' in 0.001 secs
'''

@timer
class Calculator:

    def __init__(self, num):
        self.num = num
        import time
        time.sleep(2)

    def doubled_and_add(self):
        res = sum([i * 2 for i in range(self.num)])
        print("Result : {}".format(res))

c = Calculator(100)



'''
Finished 'Calculator' in 2.001 secs
Decorating a class does not decorate its methods. Here, @timer only measures the time it takes to instantiate the class.
'''




#=============================DECORATORS======================================================================
def decorator_fun(msg):
    def wrapper_fun():
        print (msg)
    return wrapper_fun

a  = decorator_fun('hi')
b = decorator_fun('bye')

# se these a() and b() are waiting to be executed !!!! 
a()
b()

def decorator_fun(original_func):
    def wrapper_fun():
        original_func()
    return wrapper_fun


def display ():
    print ('hello')
    
a = decorator_fun(display)

# a is right now waitng to be executed , a() is the way we execute it !!!


# yet another view 
def decorator_fun(original_func):
    def wrapper_fun(*arg , **kwarg):
        print ('execurion before wrapper runing {}'.format(original_func.__name__))
        original_func(*arg, **kwarg)
    return wrapper_fun

@decorator_fun
def dispaly():
    print ('hello')
    
    
# Now we have :
display = decorator_fun(display) 
display() # decorator_fun(display)()

del display

display() # 


# what if we wanty to have the same wrapper around another function 
# NOTE : WE HAVE TO PUT *arg , **kwarg IN THE DECORATOR FUNCTION OTHERWISE IT WONT RUN 
#QUESTION: WHEN SHOUDL PUT arg , kwarg AND WHEN *arg , **kwarg ??? * and ** i sfor unpacking posiutional (list ) and unpositional (dictionary )
#   And they come in the function as the argument but in the body of the functionthey wil be used as is like for i in arg , or arg[i] or kwarg['var'] ..



@decorator_fun
def display_info(name , age):
    print ('it ran and the age is {} for {}'.format(age , name))
    
display_info('hamed', 34)   


# Some people like to use class  decorator instead of functions

class decorator_class():
    
    def __init__(self, original_func):
        
        self.original_func = original_func
        
    def __call__ (self, *arg , **kwarg):
        print ('execurion before wrapper runing {}'.format(self.original_func.__name__))
        return self.original_func(*arg, **kwarg)
    

@decorator_class
def display_info(name , age):
    print ('it ran and the age is {} for {}'.format(age , name))
    
    
display_info(19, 'Hamed')



# Practical Examples 
# One of the most use cases of decorators is logging . 

def my_logger(original_func):
    import logging 
    logging.basicConfig(filename = '{}.log'.format(original_func.__name__), level = logging.INFO)
    
    def wrapper(*arg, **kwarg):
        logging.info(
            'Run with args : {} and kwargs {}'.format(arg , kwarg) )
        return original_func(*arg, **kwarg)
    return wrapper 
    
    
def my_timer (original_func):
    import time
    
    def wrapper(*arg, **kwarg):
        t1 = time.time()
        result = original_func(*arg , **kwarg)
        t2 = time.time() - t1 
        print ('{} ran in : {} sec'. format(original_func.__name__ , t2))
        return result 
        
        
    return wrapper # resukt as a function goes to warpper and returned and whenever a function is called it executes 

   
    
    
@my_logger
def display_info(name , age):
    print ('it ran and the age is {} for {}'.format(age , name))
    
    
display_info(19, 'Hamed')   # If you see in file you can see th elogging info  , debug it later th efile is created but there is nothing in there 

# What if we want to apply multiple wrapper to a function ; Just simply stack them at the to 
# BUt because of the order of them actually it is gouing to be like that my_timer(my_logger(display_info('10', 'Hamed'))) and the inner wrapper just returnrs a wrapper
#to the outer wrapper , 
#it ran and the age is Hamed for 10
#wrapper ran in : 8.0108642578125e-05 sec


@my_timer
@my_logger       
def display_info(name , age):
    print ('it ran and the age is {} for {}'.format(age , name))
      
display_info('10', 'Hamed')   

#SOLUTION ; 
from functools import wraps 

def my_logger(original_func):
    import logging 
    logging.basicConfig(filename = '{}.log'.format(original_func.__name__), level = logging.INFO)
    
    @wraps(original_func)   #  @wraps(original_func)  takes care of stack decorators later on 
    def wrapper(*arg, **kwarg):
        logging.info(
            'Run with args : {} and kwargs {}'.format(arg , kwarg) )
        return original_func(*arg, **kwarg)
    return wrapper 
    
    
def my_timer (original_func):
    import time
    @wraps(original_func)
    def wrapper(*arg, **kwarg):
        t1 = time.time()
        result = original_func(*arg , **kwarg)
        t2 = time.time() - t1 
        print ('{} ran in : {} sec'. format(original_func.__name__ , t2))
        return result 
        
        
    return wrapper # resukt as a function goes to warpper and returned and whenever a function is called it executes 

    
@my_timer
@my_logger       
def display_info(name , age):
    print ('it ran and the age is {} for {}'.format(age , name))
      
display_info('10', 'Hamed')       

# It print s 
#   it ran and the age is Hamed for 10
#   display_info ran in : 8.082389831542969e-05 sec    it us the name of the function not  awrapper !!!!
    
    
################################################################### arg mm kwarg 

# function (farg, *arg , **kwarg) even for the inner fuctions 



def multiply(number, factor=1, **kwargs):
    return number*factor

def add(number, to_add=0, **kwargs):
    return number+to_add

def multiply_add(number, **kwargs):
    return add(multiply(number, **kwargs), **kwargs)

multiply_add(5, factor=3 , to_add=200)

import numpy as np
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), range(5)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
    
###############################################################################








