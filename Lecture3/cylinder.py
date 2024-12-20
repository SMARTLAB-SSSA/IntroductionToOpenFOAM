import numpy as np


R=1
hx=20
hy=10
hz=3

hx1=5

ver=np.zeros((32,3))

xr,yr=hx1+R,0

cir= lambda theta : [xr+R*np.cos(theta),yr+R*np.sin(theta)]

#First volume
ver[0]=[0,0,-hz/2]
ver[1]=[hx1,0,-hz/2]
ver[2]=[hx1,hy/2,-hz/2]
ver[3]=[0,hy/2,-hz/2]

ver[4]=[0,0,hz/2]
ver[5]=[hx1,0,hz/2]
ver[6]=[hx1,hy/2,hz/2]
ver[7]=[0,hy/2,hz/2]

#Second volume

ver[8]=[hx1+R,R,-hz/2]
ver[9]=[hx1+R,hy/2,-hz/2]
ver[10]=[hx1+R,R,hz/2]
ver[11]=[hx1+R,hy/2,hz/2]

#Third volume

ver[12]=[hx1+2*R,0,-hz/2]
ver[13]=[hx1+2*R,hy/2,-hz/2]
ver[14]=[hx1+2*R,0,hz/2]
ver[15]=[hx1+2*R,hy/2,hz/2]

#Forth part
ver[16]=[hx,0,-hz/2]
ver[17]=[hx,hy/2,-hz/2]

ver[18]=[hx,0,hz/2]
ver[19]=[hx,hy/2,hz/2]

#Fifth part
ver[20]=[0,-hy/2,-hz/2]
ver[21]=[hx1,-hy/2,-hz/2]

ver[22]=[0,-hy/2,hz/2]
ver[23]=[hx1,-hy/2,hz/2]

#Sixth
ver[24]=[hx1+R,-hy/2,-hz/2]
ver[25]=[hx1+R,-R,-hz/2]

ver[26]=[hx1+R,-hy/2,hz/2]
ver[27]=[hx1+R,-R,hz/2]

#Seventh + eight
ver[28]=[hx1+2*R,-hy/2,-hz/2]
ver[29]=[hx,-hy/2,-hz/2]

ver[30]=[hx1+2*R,-hy/2,hz/2]
ver[31]=[hx,-hy/2,hz/2]



with open("vertices","w") as f:
    for i in range(len(ver)):
        f.write(f"( {ver[i][0]} {ver[i][1]} {ver[i][2]}) //P{i} \n")
