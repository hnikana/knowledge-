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
'''
