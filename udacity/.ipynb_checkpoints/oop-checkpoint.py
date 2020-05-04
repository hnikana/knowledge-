#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:37:47 2020

@author: hniakan
"""




'''
Lesson Outline
    Object-oriented programming syntax

        procedural vs object-oriented programming
        classes, objects, methods and attributes
        coding a class
        magic methods
        inheritance
    Using object-oriented programming to make a Python package

        making a package
        tour of scikit-learn source code
        putting your package on PyPi
        
        
precedural progam vs obkect oriented programming 
Objects :
    Characteristics 
    Action
        
Seller is an object : 
    properties : name, age, sex 
    Method : sell , get money , give back the change 

T-shirt is an object : 
    Propertoies ; color , type , price 
    Action : chnage the price 
    
Class , Object , Method , Attributes :
    characteristics : Attributes 
    Actions : Method 

    Object : a sepecific or aninstance of a clas s


*** What is decorator ? Taking a function as an argument add some other functionality and return another function !!!
    

Modularizing the code , from the same directory import the class or function written there 

When you define a class, you can change the value of attributes directly without going through the definiton of the class. Pythoin is a bit looser than other language 
in that regard. In C++ you can explicitly put if you want the attributes be accessible and changeable or not. 

But it s always better to change the value of attributes by method , why ?

Changing values via a method gives you more flexibility in the long-term. What if the units of measurement change, like the store was originally meant 
to work in US dollars and now has to handle Euros? SO that way with some coeficient in the class definition we can easily take of it . 

dollar 35 ; store wants it euros ===> shirt.price = .81 x 35 , this is the way to change the attribute directly 
however we have change_price (*arg) method . if we change the method it can automatically change the price of $ to euros 

def change_price(self, new_price):
    self.price = new_price * 0.81 # convert dollars to Euros

shirt_one.change_price(10)

Instead, the general object-oriented programming convention is to use methods to access attributes or change attribute values.

These methods are called set and get methods or setter and getter methods.

A get method is for obtaining an attribute value. A set method is for changing an attribute value. If you were writing a Shirt class, the code could look like this:
    

'''
class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price

 '''
 In the class definition, the underscore in front of price is a somewhat controversial Python convention. 
 In other languages like C++ or Java, price could be explicitly labeled as a private variable. 
 This would prohibit an object from accessing the price attribute directly like shirt_one._price = 15. 
 However, Python does not distinguish between private and public variables like other languages. Therefore, there is some controversy about using the underscore
 convention as well as get and set methods in Python. Why use get and set methods in Python when Python wasn't designed to use them?
 
 At the same time, you'll find that some Python programmers develop object-oriented programs using get and set methods anyway. Following the Python convention,
 the underscore in front of price is to let a programmer know that price should only be accessed with get and set methods rather than accessing price directly 
 with shirt_one._price. However, a programmer could still access _price directly because there is nothing in the Python language to prevent the direct access.
 
'''   
    
'''
Below is an example of a class with docstrings and a few things to keep in mind:

Make sure to indent your docstrings correctly or the code will not run. A docstring should be indented one indentation underneath the class or method being described.
You don't have to define 'self' in your method docstrings. It's understood that any method will have self as the first method input.


'''    
    
class Pants:
    """The Pants class represents an article of clothing sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price

    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)
    
    
    
'''
Magic method : let you override and customize default python behaviour 
__add__(self, other ) : Python knows how to add two numebr 10 +12 and actually it does 10 .__add(12) , we can define this behaviour for customized classes as well


In a Guassian Class example : we can add ...
def __add__(self, othetr):
    result = Guassian ()
    result.mean = slef.mean + other.mean 
    result.stdv = self.stdv + other.stdv 
    
So the method instantiate another class with defined mean and std (result)

so anther example is __repr__ method : when we say x = 6 , and then we execute x , python prints out 6 , and actually it it its __repr__ method to control what 
variable from the class should be printed out. so we can add 


def __repr__(self):
    
    retrun ('mean is {} nad standard deviation is {}'.format(self.mean , self.stdv)) 


Note that it shoud be return not print , why ? if we put print then we get an error 


Reemember of Guassian class , guassi = Guassina (10 ,1)

guassi 

it prints 'mean is 10 nad standard deviation is 2'

Python has dozens of magic function s, add, subtract , devide , etc ... that can be done in class definition 



'''

import math
import matplotlib.pyplot as plt

class Gaussian():
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = []


    
    def calculate_mean(self):
    
        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        mean = sum(self.data) / len(self.data)
        #TODO: Calculate the mean of the data set. Remember that the data set is stored in self.data
        # Change the value of the mean attribute to be the mean of the data set
        # Return the mean of the data set  
        self.mean = mean 
        
        return mean
                


    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """

        # TODO:
        #   Calculate the standard deviation of the data set
        #   
        #   The sample variable determines if the data set contains a sample or a population
        #   If sample = True, this means the data is a sample. 
        #   Keep the value of sample in mind for calculating the standard deviation
        #
        #   Make sure to update self.stdev and return the standard deviation as well    
        if sample :
            n = len(self.data) - 1
        else :
            n = len(self.data)
            
        stdv = math.sqrt (sum([(x-self.mean)**2 for x in self.data])/ n)  
        
        self.stdev = stdv 
                        
        return stdv 
        

    def read_data_file(self, file_name, sample=True):
    
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        # TODO: 
        #   Update the self.data attribute with the data_list
        #   Update self.mean with the mean of the data_list. 
        #       You can use the calculate_mean() method with self.calculate_mean()
        #   Update self.stdev with the standard deviation of the data_list. Use the 
        #       calcaulte_stdev() method.
        
        self.data = data_list
                          
        self.mean = self.calculate_mean()
                          
        self.stdev = self.calculate_stdev(sample)
                
        
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        # TODO: Plot a histogram of the data_list using the matplotlib package.
        #       Be sure to label the x and y axes and also give the chart a title
        fig = plt.figure()
        plt.hist(self.data)
        plt.xlabel('data')
        plt.ylabel('frequency')
        plt.title('histogram')
                
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        # TODO: Calculate the probability density function of the Gaussian distribution
        #       at the value x. You'll need to use self.stdev and self.mean to do the calculation
        y = (1/((self.stdev)* math.sqrt(2 * math.pi))) * math.exp(-.5 * ((x-self.mean)/self.stdev) **2 ) 
        
        return y 

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        #TODO: Nothing to do for this method. Try it out and see how it works.
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        
        """Magic method to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """
        
        # TODO: Calculate the results of summing two Gaussian distributions
        #   When summing two Gaussian distributions, the mean value is the sum
        #       of the means of each Gaussian.
        #
        #   When summing two Gaussian distributions, the standard deviation is the
        #       square root of the sum of square ie sqrt(stdev_one ^ 2 + stdev_two ^ 2)
        
        # create a new Gaussian object
        result = Gaussian()
        
        # TODO: calculate the mean and standard deviation of the sum of two Gaussians
        result.mean = self.mean + other.mean # change this line to calculate the mean of the sum of two Gaussian distributions
        result.stdev = math.sqrt((self.stdev)**2 + (other.stdev)**2) # change this line to calculate the standard deviation of the sum of two Gaussian distributions
        
        return result

    def __repr__(self):
    
        """Magic method to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        # TODO: Return a string in the following format - 
        # "mean mean_value, standard deviation standard_deviation_value"
        # where mean_value is the mean of the Gaussian distribution
        # and standard_deviation_value is the standard deviation of
        # the Gaussian.
        # For example "mean 3.5, standard deviation 1.3"
        return ("mean {}, standard deviation {}".format(self.mean , self.stdev))
        
        
    
# Unit tests to check your solution

import unittest

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)

    def test_initialization(self): 
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\
         'pdf function does not give expected result') 

    def test_meancalculation(self):
        self.gaussian.read_data_file('numbers.txt', True)
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.gaussian.read_data_file('numbers.txt', True)
        self.assertEqual(round(self.gaussian.stdev, 2), 92.87, 'sample standard deviation incorrect')
        self.gaussian.read_data_file('numbers.txt', False)
        self.assertEqual(round(self.gaussian.stdev, 2), 88.55, 'population standard deviation incorrect')

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

    def test_repr(self):
        gaussian_one = Gaussian(25, 3)
        
        self.assertEqual(str(gaussian_one), "mean 25, standard deviation 3")
        
tests = TestGaussianClass()

tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

unittest.TextTestRunner().run(tests_loaded)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











 