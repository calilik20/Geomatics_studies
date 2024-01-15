import math

# Taking Inputs

print("This program calculates the coordinates in open traverse serie")
print("-"*64)
print("Enter the point ID of first known point  :", end=" ")
a_0624 = input()

print("Enter the Y coordinates of first known point (m) :",end=" ")
b_0624=float(input())

print("Enter the X coordinates of first known point (m)  :",end=" ")
c_0624=float(input())

print("Enter the point ID of second known point  :", end=" ")
d_0624 = input()

print("Enter the Y coordinates of second known point (m)  :", end=" ")
e_0624 = float(input())

print("Enter the X coordinates of second known point (m)  :", end=" ")
f_0624 = float(input())

print("Enter the number of unknown traverse points  :", end=" ")
g_0624 = int(input())

# Adding the First known points ID's to the list 10
list10=[]
list10.append(a_0624)
list10.append(d_0624)

list1 = [] # unknown points ID's

# Adding the unknown points ID's to the list 1
for i in range(1, g_0624 + 1):
    print("Enter the point ID of unknown point ", i, ":", end=" ")
    i = int(input())
    list1.append(i)

# Inputting the first traverse angle
print("Enter the traverse angle of", d_0624, "(grad)  :", end=" ")
h_0624 = float(input())

list2 = [] # traverse angles
list2.append(h_0624)

# Inputting the unknown point's traverse angles
for j in range(list1[0], len(list1)):
    print("Enter the traverse angle of ", j, "(grad)  :", end=" ")
    j = float(input())
    list2.append(j)

# Inputting the first horizontal distance
print("Enter the horizontal distance between", d_0624, "and", list1[0], "(m)  :", end=" ")
i_0624 = float(input())

list3 = [] # horizontal distances
list3.append(i_0624)

# Inputting the horizontal distances between unknown points
for k in range(list1[0], len(list1)):
    print("Enter the horizontal distance between", k, "and", k + 1, "(m)  :", end=" ")
    k = float(input())
    list3.append(k)

list4 = []  # Azimuth angles

# Defining function for first azimuth angle between known points
def first_azimuth(y1, x1, y2, x2):
    dy = y2 - y1
    dx = x2 - x1
    if x1 == x2 and y1 > y2:
        azimuth = 300
    elif x1 == x2 and y1 < y2:
        azimuth = 100
    elif y1 == y2 and x1 > x2:
        azimuth = 200
    elif y1 == y2 and x1 < x2:
        azimuth = 0
    else:
        azimuth = math.atan(abs(dy / dx)) * 200 / math.pi
    if dy > 0 and dx > 0:
        azimuth = azimuth
    elif dy > 0 and dx < 0:
        azimuth = 200 - azimuth
    elif dy < 0 and dx < 0:
        azimuth = 200 + azimuth
    else:
        azimuth = 400 - azimuth
    return azimuth

# Defining function for next azimuth angle between unknown points
def next_azimuth(azimut, traverse):
    K_0624 = float(azimut + traverse)
    if K_0624 < 200:
        K_0624 += 200
    elif K_0624 > 200 and K_0624 < 600:
        K_0624 -= 200
    elif K_0624 > 600:
        K_0624 -= 600
    return K_0624

# Finding first azimuth angle between known points
first_azimuth(b_0624, c_0624, e_0624, f_0624)
tab=first_azimuth(b_0624, c_0624, e_0624, f_0624)
list4.append(tab)

# Finding and appending first azimuth angle between unknown points
for i in range(len(list2)):
        az = float(next_azimuth(list4[i], list2[i]))
        list4.append(az)

# Defining function for delta Y between points
def delta_y(dist,azimuth):
    deltay_0624 = float(dist * math.sin(azimuth*math.pi/200))
    return deltay_0624

# Defining function for delta X between points
def delta_x(dist,azimuth):
    deltax_0624 = float(dist * math.cos(azimuth*math.pi/200))
    return deltax_0624

list5 = []  # delta Y

# Finding and appending for delta Y between points
for i in range(len(list1)):
    deltay=delta_y(list3[i],list4[i+1])
    list5.append(deltay)

list6=[] # delta X

# Finding and appending for delta X between points
for i in range(len(list1)):
    deltax=delta_x(list3[i],list4[i+1])
    list6.append(deltax)

list7=[] # Y coordinates
list7.append(e_0624)

# Finding and appending for Y coordinates
for i in range(len(list1)):
    coordy = list7[i]+ list5[i] 
    list7.append(coordy)

list8=[] # X coordinates
list8.append(f_0624)

# Finding and appending for X coordinates
for i in range(len(list1)):
    coordx = list8[i]+ list6[i] 
    list8.append(coordx)

# Proper Format
list4 = ["%.4f" % member for member in list4]
list5 = ["%.2f" % member for member in list5]
list6 = ["%.2f" % member for member in list6]
list7 = ["%.2f" % member for member in list7]
list8 = ["%.2f" % member for member in list8]

# Printing and making table
print("-"*73)
print("%-15s %-15s %-15s %-15s  %s" %("Point ID", "Point ID", "Azimuth","Delta Y","Delta X"))
print("-"*73)
print("%-15s %-15s  %s" %(a_0624, d_0624,list4[0]))
print("%-15s %-15s %-15s %-15s %s" % (list10[1], list1[0], list4[1],list5[0],list6[0]))

for i in range(len(list1)-1):
    print("%-15s %-15s %-15s %-15s %s" % (list1[i], list1[i+1], list4[i+2],list5[i+1],list6[i+1]))
print("-" * 73)

print("%-15s %-15s %s" %("Point ID","Coordinate(Y)","Coordinate(X)"))
print("-" * 45)
for i in range(len(list1)):
    print("%-15s %-15s %s" % (list1[i],list7[i+1], list8[i+1]))
print("-" * 45)
