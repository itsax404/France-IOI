from math import *

def distance(x1, y1, x2, y2):
    distances = sqrt((x2-x1)**2 + (y2-y1)**2 )
    print(distances)
   
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance(x1, y1, x2, y2)