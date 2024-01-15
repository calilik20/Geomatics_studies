import math
# open coordinates.txt file in read mode

f=open("points.txt","r")

#empty lists for x y z values

pid = []

x = []

y = []

z = [] #heights

for line in f.readlines():
    #split each column element into a list element
    line= line.split()
    #append point ids to pid list a string
    pid.append(line[0])
    #append x coordinates to list x as float
    x.append(float(line[1]))
    #append y coordinates to list y as float
    y.append(float(line[2]))
    #append z coordinates to list z as float
    z.append(float(line[3]))

distance = []

for i in range(len(pid)-1):
    s=math.sqrt((x[i+1]-x[i])**2+ (y[i+1]-y[i])**2)
    print("Distance between",pid[i], "and", pid[i+1], ":", format(s,".3f"),"m")
    distance.append(s)
