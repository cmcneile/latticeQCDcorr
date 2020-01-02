
import numpy as np
import math

from random import seed
from random import gauss

# my modules
import corrlib
from simulation import *

print ("Starting to create the correlators")
print("Length of time direction " , nt)

ttt = A.shape
n_smear = ttt[0]
n_state = ttt[1]

# sanity check, states and smearing functions
n_exp = len(mass) + len(mass_osc)
if n_state != n_exp  :
  print("ERROR " , n_state , "!=",  n_exp)
  sys.exit(1)

if n_smear !=  nsmear : 
  print("ERROR " , n_smear , "!=" ,   nsmear  ) 
  sys.exit(1)

print("Number of smearing functions = " , n_smear  )
print("Number of mass states = " , n_state  )


Atrans = A.transpose()

corr_mean = np.zeros( (nsmear,nsmear, nt )  )

print(A) 

print("Creation of population model")

for t in range(0,nt):
 m_exp =  corrlib.create_mass(t, mass, mass_osc)
 print("Time " , t)
## for ddd in m_exp :
##   print(ddd)

 tmp = np.matmul(A, m_exp)
 cmean = np.matmul(tmp, Atrans)

 print(cmean)
 for i in range(0,nsmear) :
   for j in range(0,nsmear) :
     corr_mean[i,j, t] = cmean[i,j]

######
##
######

print("Starting the simulations")

corr = np.zeros( (nsmear,nsmear, nt )  )

file1 = open("corr.txt","w")

for icfg in range(ncfg) :
  print("Creating correlator for configuration " , icfg)

  for t in range(0,nt): 
   for i in range(0,nsmear) :
      for j in range(0,nsmear) :
            corr[i,j, t] = corr_mean[i,j, t]  + gauss(0.0, sig)

  for i in range(0,nsmear) :
    for j in range(0,nsmear) :
       for t in range(0,nt): 
         file1.write(str(corr_mean[i,j, t]) + " ") 
       file1.write("\n") 


file1.close() 
