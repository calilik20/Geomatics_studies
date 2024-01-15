# LAB 9 work 2

pidFile = open("pid.txt","w")
xFile = open("xcoordinates.txt","w")
yFile = open("ycoordinates.txt","w")
hFile = open("heights.txt","w")
sFile = open("distances.txt","w")

for i in range(len(pid)):
    pidFile.write(pid[i] +"\n")
    xFile.write(str(x[i]) +"\n")
    yFile.write(str(y[i]) +"\n")
    hFile.write(str(z[i]) +"\n")
    if i< len(distance):
        sFile.write(str(distance[i])+"\n")

        
pidFile.close()
xFile.close()
yFile.close()
hFile.close()
sFile.close()
