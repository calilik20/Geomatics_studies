import math
angle = float(input("Please enter an angle(degree):"))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print("Sine of the angle {} is {}".format(angle,sine))
print("Cosine of the angle {} is {}".format(angle,cosine))
print("Tangent of the angle {} is {}".format(angle,tangent))
