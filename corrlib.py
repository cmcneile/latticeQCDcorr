#  Collection of rouines to create correlators
#
#

import numpy as np
import math

from numpy import linalg as LA

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



#
#  Create covariance matrix
#

def create_covar_time(nt, decay) :

  ans = np.zeros((nt,nt) )

  for t1 in range(0,nt):
    for t2 in range(0,nt):
      dd = math.fabs(t1 - t2) 
      ans[t1,t2] = math.exp(-dd*decay) 

  #  compute the eigenvalues 
  if 1 :
    w, v = LA.eig(ans)
    for eig in w:
      print("Eigenvalue_covar " , eig)


  return ans 



def create_diag_covar_time(nt) :

  ans = np.zeros((nt,nt) )

  for t1 in range(0,nt):
      ans[t1,t1] = 1.0


  return ans 


