
import numpy as np
import math

from random import seed
from random import gauss

#
#  exp(-m_i t) + (-1)**t 
#

def create_mass(t, mass, mass_osc) :

  n = len(mass)
  n_osc = len(mass_osc)
  nT = n+n_osc
  ans = np.zeros((nT,nT) )

  for i in range(0,n):
    ans[i,i] = math.exp( - t * mass[i] )

  for i in range(0,n_osc):
    ans[n+i,n+i]  = (-1)**(t) * math.exp( - t * mass_osc[i] )

  return ans 




##
##
##

nt = 8
ncfg  = 1000

# two smearing functions
nsmear = 2

sig = 0.1 

##
##
##

print ("Starting to create the correlators")
print("Length of time direction " , nt)

mass = [ 0.4 , 0.6 , 0.9]
mass_osc = [ 0.5 , 0.65 ]

A = np.array([ [ 1.5 , 1.7 , 1.9 , 0.21 , 0.23   ] ,  [ 1.02 , 1.13 , 1.02 , 0.151 , 0.156   ] ]  )





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
 m_exp =  create_mass(t, mass, mass_osc)
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

###sss = cmean.shape
##print(sss[0], sss[1] )


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
