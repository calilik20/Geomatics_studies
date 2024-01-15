def calc_azimuth(ax, ay, bx, by):
    import math
    TWO_PI = math.pi * 2
    theta = math.atan2(bx - ax, ay - by)
    if (theta < 0.0):
        theta += TWO_PI
    return math.degrees(theta)*(10/9)
print(format(calc_azimuth(3660.000,1930.000,3660.000,2030.000), ".4f"))
