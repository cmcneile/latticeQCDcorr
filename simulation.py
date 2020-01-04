##
##  parameters of the simulation
##
import numpy as np
import sys

nt = 64
ncfg  = 8000

# two smearing functions
nsmear = 2

#  parameters of the noise
sig = 0.7 
n_decay = 0.5 

##
##
##

mass = [ 1.1 , 1.4 , 1.6]
mass_osc = [ ]

##A = np.array([ [ 1.5 , 1.7 , 1.9   ] ,  [ 1.02 , 1.13 , 1.02    ] ]  )
A = np.array([ [ 1.5 , 1.7 , 1.9   ] ,  [ 1.5 , 1.7 , 1.9    ] ]  )


###

corr_name = "corr.txt"

############################################################
