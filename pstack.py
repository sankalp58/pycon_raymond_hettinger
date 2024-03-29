'''
This is example docstring 
'''

import  math

class Circle(object):
    '''
    An adavanced circle analytic toolkit
    
    '''

    version ='0.2a' #class variable

    def  __init__(self,radius):

        self.radius =radius

    def area(self):

        'Performa quadrature on a shape of uniform radius '
        return  math.pi *self.radius**2.0

    #for rubber sheet comapny
    def perimeter(self):
        'perform bprder length of curve for any given radius '
        return  math.pi * self.radius * 2.0

    @classmethod
    def from_bbd(cls,bbd):      #alternative construcotr
        'Construct a circle from bounding box diagnal '
        radius = bbd/2.0/math.sqrt(2.0)
        return  cls(radius)  # to know from which class the method was called

    @staticmethod #attach function to classes
    def angle2grade(angle):
        return   math.tan(math.radians(angle)) * 100.0




if __name__ == '__main__':

    print( 'circuitous version ' , Circle.version)
    c= Circle(10)
    print( 'a circle of radius ', c.radius)
    print('has an area of ',c.area())

