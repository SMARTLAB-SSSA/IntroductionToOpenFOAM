import numpy as np


hc=1.6 #m
hh=0.4 #m

Uh=0.2 #m/s
Uc=0.05 #m/s

Th= 40+273.15
Tc=20+273.15


mc=Uc*hc
mh=Uh*hh

To=(mc*Tc+mh*Th)/(mc+mh)

print(To-273)

