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

    
###############    
    
    
class Distribution:
    
    def __init__(self, mu =0, sigma=1):
    
        """ Generic distribution class for calculating and 
        visualizing a probability distribution.
    
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
            """
        
        self.mean = mu
        self.stdev = sigma
        self.data = []


    def read_data_file(self, file_name):
    
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
            
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list   
        
        
import math
import matplotlib.pyplot as plt

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu=0, sigma=1):
        
        Distribution.__init__(self, mu, sigma)   # another way is super().__init(mu, sigma)
    
        
    
    def calculate_mean(self):
    
        """Function to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                    
        avg = 1.0 * sum(self.data) / len(self.data)
        
        self.mean = avg                           # we could.define self.mean at top and put = None but if it does not exist it makes it 
        
        return self.mean



    def calculate_stdev(self, sample=True):

        """Function to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
    
        mean = self.calculate_mean()
    
        sigma = 0
    
        for d in self.data:
            sigma += (d - mean) ** 2
        
        sigma = math.sqrt(sigma / n)
    
        self.stdev = sigma
        
        return self.stdev
        
        
        
    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')
        
        
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
        

    def plot_histogram_pdf(self, n_spaces = 50):

        """Function to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
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
        
        """Function to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """
        
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
    
    
    
    
'''##################################################          MODULARIZING       ################################################'''    
'''
A Module is a simple python file containing some fuctions and classes
A package is a collection of moduls collected in a directory 
 Python package also needs an __init__.py file.
 __init__.py tells python that this folder contains a package 
 each package and their subpackage should have __init__.py otherwise they cannot be imported
 
 SO , fo just a sake of loval programing , if we want to import a function from a module existed in the same directory 
 we need to just import it 
 
 root /
     module_1.py 
     module_2.py 
     test.py 
     
     
so in test.py I can write 
import class from module_1 

but for a package purposes , we need to have init and if we want to import from the same directory there should be a . 
showing the relavative path , 

Still I dont know how to import from a parent package to sub package 

MAY BE we need to change the path !!!! 

In order to make a package setup.py shoudl be in the same directory that the package folder exist 

setup.py is necessary for installing 

In order to install it , we have to go to the same directory that the package folder exist and then pip install . 
the . (dot) tells pip to look for setup.py 

no w we can use the python package like the other packages 

now you might ask yourself where it is installed ? wherever the pip install packages 

we can import the packag e

import mypackage 
mypackage.__file__


if we have a python package under develpment or for educational purposes and we want to intsall it locally we may need to create a virtual envorionemnt 

If you decide to install your package on your local computer, you'll want to create a virtual environment. A virtual environment is a silo-ed Python 
installation apart from your main Python installation. That way you can install packages and delete the virtual environment without affecting your main 
Python installation

Let's talk about two different Python environment managers: conda and venv

Conda
Conda does two things: manages packages and manages environments.

There are other environmental managers and package managers besides conda. For example, venv is an environment manager that comes pre-installed with Python 3.
 Pip is a package manager.

Pip can only manage Python packages.

Whether you choose to create environments with venv or conda will depend on your use case. Conda is very helpful for data science projects,
 but conda can make generic Python software development a bit more confusing; that's the case for this project.

If you create a conda environment, activate the environment, and then pip install the distributions package, you'll find that the system installs 
your package globally rather than in your local conda environment. However, if you create the conda environment and install pip simultaneously, 
you'll find that pip behaves as expected installing packages into your local environment:
    
    conda create --name environmentname pip 
    
    
So , for datascience stuff cond ais the best way but th eproblem is that conda cannot take care of all installation packages and for that you have to use pip 

then pip would install packages globally however the created environment is activated . but we wont hav ethis problem with enve and pip , they are match and pip 
packages in the active environment created by env 

How to confirm type of installation ? 
if we run conda list , it shows all the packages installed and shows Anaconda is the installation set up 
or if in the terminal type paython , it would show the version and the set up installation 

How to create a vurtual environemt ? 

python -m env virtual-name '
source virtual-name/bin/activate  ==> activate the virtual envirinment and if we install anythinhg using pip , then it would install in this folder of virtual
environement instead of globally 


SO likewise before we can move to the directory that contains our python package and setup.py and install in via pip , then it would install it withon the virtual
envirinment 


1- create a folder called distributions 
2- create setup.py 
     
3- in distriburtion foder we put our modules and __init__.py , if it has sub folder within each subfolder we have to have __init__.py if we want to 
    import them later on 
    
4-  Npw we can create an envoronemet inorder to avoid messing up with original python installation 
5- we can go to the directory and say pip install . ; as I mentoned before this . (dot ) will look for setup.py and install the package and in the python shell or 
    IDE we can just import as usuall 



The reason why we put 'from .guassiandistribution import guassian' in __init__.py or even importing more ? why ?

    _ technically we are saying from realtive address (.) from module guassiandistribution.py import function or class Guassina 
    - if we dont do that also it works but we have to give it the exact address ==> where to giv eit the exact address ?
        In our notebook , python file we are writing and we want to make use of that function for instance 
        if it exiusted in __init__.py ==> in the python shell
            from distribution import Guassian 
        if it does not exist 
            from distribution.guassiandistribution import guassian 
            
        This way we can make short cut and provide just useful classes for the user instaed of giving him ll the information as they might not need and make them confused
        Right ? So , we using pip install distributions we install it and __init__.py just gives us some calsses we need 
        


'''

###  test.py 

import unittest

from distributions import Gaussian
from distributions import Binomial

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.gaussian.read_data_file('numbers.txt')

    def test_initialization(self): 
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_readdata(self):
        self.assertEqual(self.gaussian.data,\
         [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 92.87, 'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 88.55, 'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\
         'pdf function does not give expected result') 
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(round(self.gaussian.pdf(75), 5), 0.00429,\
        'pdf function after calculating mean and stdev does not give expected result')      

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)
        
class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('numbers_binomial.txt')

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.n, 20, 'n value incorrect')

    def test_readdata(self):
        self.assertEqual(self.binomial.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')
    
    def test_calculatemean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)
    
    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.19)
        
    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p,3), .615)
        self.assertEqual(n, 13)
        
    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)
    
        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two
        
        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)
        
    
if __name__ == '__main__':
    unittest.main()


'''
Shoudl we pass the parent required argument in the child class definition, yes , if they dont have default value 
but in super init we can use arg , kwarg ??????
'''
    
'''
PyPi vs. Test PyPi
Python package index 
Pypi website has test repository as well as regular repository 
it is suggested to have an account in test and regular , first try it on to test and then publish it to the regular 
the package to publish shoudl have the license.txt , README.md , setup.cfg

setup.py 
package folder
    - __init__.py
    - license.txt 
    - setup.cfg
    - README.md
    
    
cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# command to upload to the pypi repository
twine upload dist/*
pip install dsnd-probability


INTERESTING : if you are upload a package with a underscore in ithe name , so the package will be uploaded and the underscore 
will be replaced by dash 

Whatever goes to init file , it would be called under the name of package 

INTERESTING : when we import from a module , under the hood , the python run the module and put every function and class 
into a  Dicttionary and then just called whatever you wat and ut them into the cash 
SCENARIO 1 : 
    the module has some error like indention or something else but the function or class
    we want to import is OK , it fails to import because python runs it first all of it 
SCENARIO 2 :
    If the module contains something like print ('') or any action , nut just function or class definition 
    they woule be rin as well
    

echo PYTHONPATH = $PYTHONPATH : route/ to /dir



Package /
--------project /sub_1
----------------__init__.py ==> 
                                from sub_1.helpertool import helper 
                                from sub_1.mod_1 import func_1                                                     
                helpertool.py ; def helper()
                mod_1.py 
                        we can either say from helpertool import helper OR from sub1 import its in the __init__ or from helpertool import helper because they are neighbor
                        def fun_1()
                        
--------project /sub_2
---------------------__init__.py ==> from sub_2.mod_2 import func_2
                     mod_2.py 
                             from sub_1 import helper 
                             def func_2():
                                        helper 
                                        ...
                                        return 
                                        
--------__init__.py from sub1 import helper , func_1 
                    from sub2 import func2 
--------test.py

setup.py 

scenario 1 : we are talking when the package has not been installed yet , if we put something in __init__ , then they can be callable by their neighbor withput explicit address 
however explicit address would work as well

scenario 2 : if it is installed , then instead of explicit address we can just calle them for instance we can say from project import helper or we can say from project.sub import fun1 however in this scenario every function can be called at any level 




    
'''
    
    
    
    
    
    
    
    
    
    
    
    
    











 