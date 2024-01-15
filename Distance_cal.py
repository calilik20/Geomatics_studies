import math # it must be called as we are using the math library for

X1 = float(input("Please enter the x value of first point :")) # there was no float
Y1 = float(input("Please enter the y value of first point :"))
X2 = float(input("Please enter the x value of second point :"))
Y2 = float(input("Please enter the y value of second point :")) # there was no float

S = math.sqrt((X1-X2)**2 + (Y1-Y2)**2) # we need to utilize sqrt for accuracy
print("The distance between given points is",format(S,".2f"),"m") # it has to be formatted
