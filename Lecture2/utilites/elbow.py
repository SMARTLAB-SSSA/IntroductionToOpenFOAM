import numpy as np

h0=1.6
L0=3.2

h1=h0
L1=L0

R0=1.6
R1=R0+h0


theta=(45-39.93)*np.pi/180

P0=np.array([L0,h0+R0])


Points=np.zeros((40,3))
#Creating first block
#Points from 0 to 7
Points[0]=0,0,0
Points[1]=L0,0,0
Points[2]=L0,h0,0
Points[3]=0,h0,0

Points[4]=0,0,0.1
Points[5]=L0,0,0.1
Points[6]=L0,h0,0.1
Points[7]=0,h0,0.1

#Creating points in the esternal elbow with the small pipe

Points[8]=P0[0]+R1*np.cos(-np.pi/4 -theta),P0[1]+R1*np.sin(-np.pi/4 -theta),0
Points[9]=Points[8][0],0,0
Points[11]=P0[0]+R1*np.cos(-np.pi/4 +theta),P0[1]+R1*np.sin(-np.pi/4 +theta),0
Points[10]=Points[11][0],0,0

Points[12]=Points[8]+np.array([0,0,0.1])
Points[13]=Points[9]+np.array([0,0,0.1])
Points[14]=Points[10]+np.array([0,0,0.1])
Points[15]=Points[11]+np.array([0,0,0.1])

#Creating the internal points of the elbow
Points[16]=P0[0]+R0*np.cos(-np.pi/4 -theta),P0[1]+R0*np.sin(-np.pi/4 -theta),0 
Points[17]=P0[0]+R0*np.cos(-np.pi/4 +theta),P0[1]+R0*np.sin(-np.pi/4 +theta),0

Points[18]=P0[0]+R0*np.cos(-np.pi/4 -theta),P0[1]+R0*np.sin(-np.pi/4 -theta),0.1
Points[19]=P0[0]+R0*np.cos(-np.pi/4 +theta),P0[1]+R0*np.sin(-np.pi/4 +theta),0.1


#Top block
Points[20]=L0+R1,h0+R0,0
Points[21]=L0+R1,h0+R0+L1,0
Points[22]=L0+R0,h0+R0+L1,0
Points[23]=L0+R0,h0+R0,0

Points[24]=L0+R1,h0+R0,0.1
Points[25]=L0+R1,h0+R0+L1,0.1
Points[26]=L0+R0,h0+R0+L1,0.1
Points[27]=L0+R0,h0+R0,0.1

#Axiliary points for arcs
Points[28]=P0[0]+R0*np.cos(-np.pi/4 -2*theta),P0[1]+R0*np.sin(-np.pi/4 -2*theta),0
Points[29]=P0[0]+R1*np.cos(-np.pi/4 -2*theta),P0[1]+R1*np.sin(-np.pi/4 -2*theta),0
Points[30]=P0[0]+R1*np.cos(-np.pi/4 +2*theta),P0[1]+R1*np.sin(-np.pi/4 +2*theta),0
Points[31]=P0[0]+R0*np.cos(-np.pi/4 +2*theta),P0[1]+R0*np.sin(-np.pi/4 +2*theta),0

Points[32]=P0[0]+R0*np.cos(-np.pi/4 -2*theta),P0[1]+R0*np.sin(-np.pi/4 -2*theta),0.1
Points[33]=P0[0]+R1*np.cos(-np.pi/4 -2*theta),P0[1]+R1*np.sin(-np.pi/4 -2*theta),0.1
Points[34]=P0[0]+R1*np.cos(-np.pi/4 +2*theta),P0[1]+R1*np.sin(-np.pi/4 +2*theta),0.1
Points[35]=P0[0]+R0*np.cos(-np.pi/4 +2*theta),P0[1]+R0*np.sin(-np.pi/4 +2*theta),0.1

#Middle points
Points[36]=P0[0]+R0*np.cos(-np.pi/4),P0[1]+R0*np.sin(-np.pi/4),0
Points[37]=P0[0]+R1*np.cos(-np.pi/4),P0[1]+R1*np.sin(-np.pi/4),0

Points[38]=P0[0]+R0*np.cos(-np.pi/4 ),P0[1]+R0*np.sin(-np.pi/4 ),0.1
Points[39]=P0[0]+R1*np.cos(-np.pi/4 ),P0[1]+R1*np.sin(-np.pi/4 ),0.1



with open("Points","w") as f:
    for i,p in enumerate(Points):
        if i<28:
            f.write(f"( {p[0]} {p[1]} {p[2]}) //P{i}\n")


arcs=[[2,16,28],[6,18,32],[16,17,36],[18,19,38],[1,8,29],[5,12,33]
      ,[8,11,37],[12,15,39],[17,23,31],[19,27,35],[11,20,30],[15,24,34]]
with open("arcs","w") as f:
    for i,j,k in arcs:
        p=Points[k]
        f.write(f"arc {i} {j} ( {p[0]} {p[1]} {p[2]})\n")




