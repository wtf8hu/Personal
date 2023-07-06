#/* --------------------------------------------------------------------------------
#   Egorov Group
#   https://chemistry.as.virginia.edu/people/profile/sae6zk, University of Virginia
#   Will Ferguson, wtf8hu@virginia.edu
#
#   DFTMDComp.py
#   "This file compares DFT from Likos' paper to in-house MD simulations"
#-------------------------------------------------------------------------------- */

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing of reference data (Likos) #
DFTdata = pd.read_csv('/home/wtf8hu/lammps/grOptAnal1/Simulation1.csv', sep =',', skiprows = 0 ,header=None)
# ----------------------------------- #

fig, axs = plt.subplots(3, 3, sharex=True)
plt.subplots_adjust(wspace = 0.2, hspace = 0.2)

axs[0,2].set_xlim([0, 5])

for i in range(0,3):
    for j in range(0,3):
        axs[i,j].tick_params(bottom = True, top = True, right = True, direction = "in",length = 4,labelsize=10)

for i in range(0,3):
    axs[0,i].set_ylim([0, 1.25])
    axs[0,i].set_yticks([0, 0.25, 0.5, 0.75, 1.0, 1.25])

for k in range(0,3):
    axs[1,k].set_ylim([6, 18])
    axs[1,k].set_yticks([6.0, 9.0, 12.0, 15.0, 18.0])

for m in range(0,3):
    axs[2,m].set_ylim([40, 100])
    axs[2,m].set_yticks([40, 50, 60, 70, 80, 90, 100])

axs[0,0].set_xlim([1, 7])
plt.xticks([1, 2, 3, 4, 5, 6, 7])

axs[0,0].title.set_text(r'$\rho=5.5, x$=0.10')
axs[0,1].title.set_text(r'$\rho=5.5, x$=0.95')
axs[0,2].title.set_text(r'$\rho=7.0, x$=0.95')
axs[0,0].set_ylabel(r'$T^{*}=\frac{T k_B}{\epsilon}$',fontsize=14)
axs[1,0].set_ylabel(r'$E^{*}=\frac{E}{\epsilon}$',fontsize=14)
axs[2,0].set_ylabel(r'$p^{*}=p \frac{\sigma^{3}}{\epsilon}$',fontsize=14)

#DFTdata.iloc[0:,1:].dropna().to_numpy

r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 2].dropna().to_numpy()
print(gr)
axs[0,0].plot(r,gr,color="black")
r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 5].dropna().to_numpy()
axs[1,0].plot(r,gr,color="black")
r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 6].dropna().to_numpy()
axs[2,0].plot(r,gr,color="black")


DFTdata = pd.read_csv('/home/wtf8hu/lammps/grOptAnal1/Simulation2.csv', sep =',', skiprows = 0 ,header=None)

r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 2].dropna().to_numpy()
print(gr)
axs[0,1].plot(r,gr,color="red")
r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 5].dropna().to_numpy()
axs[1,1].plot(r,gr,color="red")
r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 6].dropna().to_numpy()
axs[2,1].plot(r,gr,color="red")


DFTdata = pd.read_csv('/home/wtf8hu/lammps/grOptAnal1/Simulation3.csv', sep =',', skiprows = 0 ,header=None)

r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 2].dropna().to_numpy()
print(gr)
axs[0,2].plot(r,gr,color="blue")
r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 5].dropna().to_numpy()
axs[1,2].plot(r,gr,color="blue")
r = DFTdata.iloc[0:, 1].dropna().to_numpy(); gr = DFTdata.iloc[0:, 6].dropna().to_numpy()
axs[2,2].plot(r,gr,color="blue")


axs[2,0].set_xlabel(r'$log_{10}(iter)$',fontsize=14)
axs[2,1].set_xlabel(r'$log_{10}(iter)$',fontsize=14)
axs[2,2].set_xlabel(r'$log_{10}(iter)$',fontsize=14)

plt.show()