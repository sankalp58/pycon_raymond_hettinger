from random import random,seed

from pstack import  Circle

seed(8675309)

print( 'Suing cirtuitous(tmn) version ',Circle.version)
n=10
circles= [ Circle(random()) for i in  range(n)]
print( 'the average area of ',n,'   random circles  ')
avg =  sum([ c.area()  for c in circles])/n
print ('is %.3f ' % avg)
