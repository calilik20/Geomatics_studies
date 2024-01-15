import math

def horizontal_distance(X1,Y1,X2,Y2):
    distance = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
    print("distance(m):",format(distance,".2f"))
