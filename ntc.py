
from pstack import  Circle

class Tire(Circle):
     'tires are circle with corrected parameters '


     def perimeter(self):
         return  Circle.perimeter(self) *1.25




if __name__ == '__main__':

    t= Tire(22)
    print( 'a tire of radius ',t.radius)
    print( 'has an area of ',t.area())
    print(' also an odometer corrected perimieter of ',)
    print( t.perimeter())
