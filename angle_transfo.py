import math # it must be called as we are using the math library
angle_degree=float(input("Please enter an angle (degree) : "))

angle_rad=math.radians(angle_degree) #angle_rad has to be defined and converted to radians

print("Sinus of the angle",angle_degree,"is",format(math.sin(angle_rad),".2f")) #it has to be formatted
print("Cosinus of the angle",angle_degree,"is",format(math.cos(angle_rad),".2f")) #it has to be formatted
print("Tangent of the angle",angle_degree,"is",format(math.tan(angle_rad),".2f")) #it has to be formatted
