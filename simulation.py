##
##  parameters of the simulation
##
import numpy as np

nt = 8
ncfg  = 1000

# two smearing functions
nsmear = 2

#  parameters of the noise
sig = 0.1 
n_decay = 0.5 

##
##
##

mass = [ 0.4 , 0.6 , 0.9]
mass_osc = [ 0.5 , 0.65 ]

A = np.array([ [ 1.5 , 1.7 , 1.9 , 0.21 , 0.23   ] ,  [ 1.02 , 1.13 , 1.02 , 0.151 , 0.156   ] ]  )

############################################################
