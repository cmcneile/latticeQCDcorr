#  Collection of rouines to create correlators
#
#

import numpy as np
import math

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


