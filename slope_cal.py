import math
def calc_horizontal(slope_dist, zenith):
    # convert zenith from grads to radians
    zenith_radians = zenith*(math.pi/200)
    # calculate horizontal distance
    # using math.sin() function
    horiz_dist = slope_dist* math.sin(zenith_radians)
    print("Horizontal distance (meters):", format(horiz_dist, ".3f"))
# call the function with input parameters
calc_horizontal(127.834, 98.421)
