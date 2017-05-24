'''
This is example docstring 
'''

import  math

class Circle(object):
    '''
    An adavanced circle analytic toolkit
    
    '''

    version ='0.1' #class variable

    def  __init__(self,radius):

        self.radius =radius

    def area(self):

        'Performa quadrature on a shape of uniform radius '
        return  math.pi *self.radius**2.0


    def perimeter(self):
        'perform bprder length of curve for any given radius '
        return  math.pi * self.radius * 2.0



if __name__ == '__main__':

    print( 'circuitous version ' , Circle.version)
    c= Circle(10)
    print( 'a circle of radius ', c.radius)
    print('has an area of ',c.area())
