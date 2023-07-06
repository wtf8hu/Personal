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
DFTdata = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/LikosDigitizedPlot.csv', sep =',', skiprows = 3 ,header=None)
# ----------------------------------- #

fig, axs = plt.subplots(3, 3, sharex=True)
plt.subplots_adjust(wspace = 0.2, hspace = 0.2)

axs[0,2].set_xlim([0, 5])

for i in range(0,3):
    for j in range(0,3):
        axs[i,j].tick_params(bottom = True, top = True, right = True, direction = "in",length = 4,labelsize=10)

for i in range(0,3):
    axs[0,i].set_ylim([0.80,1.5])
    axs[0,i].set_yticks([0.9, 1.0,1.1,1.2,1.3,1.4,1.5])

for k in range(0,3):
    axs[1,k].set_ylim([0.80,1.7])
    axs[1,k].set_yticks([1.0,1.2,1.4,1.6])

for m in range(0,3):
    axs[2,m].set_ylim([0.50, 2.6])
    axs[2,m].set_yticks([0.5,1.0,1.5,2.0,2.5])

axs[0,0].set_xlim([0, 5])
plt.xticks([0, 1, 2, 3, 4,5])

axs[0,0].title.set_text(r'$\rho=5.5, x$=0.10')
axs[0,1].title.set_text(r'$\rho=5.5, x$=0.95')
axs[0,2].title.set_text(r'$\rho=7.0, x$=0.95')
axs[0,0].set_ylabel(r'$g_{11}$(r)',fontsize=12)
axs[1,0].set_ylabel(r'$g_{12}$(r)',fontsize=12)
axs[2,0].set_ylabel(r'$g_{22}$(r)',fontsize=12)

r = DFTdata.iloc[0:, 0].dropna().to_numpy(); gr = DFTdata.iloc[0:, 1].dropna().to_numpy()
axs[0,0].plot(r,gr,color="black")
r = DFTdata.iloc[0:, 2].dropna().to_numpy(); gr = DFTdata.iloc[0:, 3].dropna().to_numpy()
axs[0,1].plot(r,gr,color="red")
r = DFTdata.iloc[0:, 4].dropna().to_numpy(); gr = DFTdata.iloc[0:, 5].dropna().to_numpy()
axs[0,2].plot(r,gr,color="blue")
r = DFTdata.iloc[0:, 6].dropna().to_numpy(); gr = DFTdata.iloc[0:, 7].dropna().to_numpy()
axs[1,0].plot(r,gr,color="black")
r = DFTdata.iloc[0:, 8].dropna().to_numpy(); gr = DFTdata.iloc[0:, 9].dropna().to_numpy()
axs[1,1].plot(r,gr,color="red")
r = DFTdata.iloc[0:, 10].dropna().to_numpy(); gr = DFTdata.iloc[0:, 11].dropna().to_numpy()
axs[1,2].plot(r,gr,color="blue")
r = DFTdata.iloc[0:, 12].dropna().to_numpy(); gr = DFTdata.iloc[0:, 13].dropna().to_numpy()
axs[2,0].plot(r,gr,color="black")
r = DFTdata.iloc[0:, 14].dropna().to_numpy(); gr = DFTdata.iloc[0:, 15].dropna().to_numpy()
axs[2,1].plot(r,gr,color="red")
r = DFTdata.iloc[0:, 16].dropna().to_numpy(); gr = DFTdata.iloc[0:, 17].dropna().to_numpy()
axs[2,2].plot(r,gr,color="blue")

d1 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr11case1.dat', sep =' ', skiprows = 0 ,header=None)
d4 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr12case1.dat', sep =' ', skiprows = 0 ,header=None)
d7 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr22case1.dat', sep =' ', skiprows = 0 ,header=None)

d2 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr11case2.dat', sep =' ', skiprows = 0 ,header=None)
d5 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr12case2.dat', sep =' ', skiprows = 0 ,header=None)
d8 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr22case2.dat', sep =' ', skiprows = 0 ,header=None)

d3 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr11case3.dat', sep =' ', skiprows = 0 ,header=None)
d6 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr12case3.dat', sep =' ', skiprows = 0 ,header=None)
d9 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr22case3.dat', sep =' ', skiprows = 0 ,header=None)

r = d1.iloc[0:, 0].dropna().to_numpy(); gr = d1.iloc[0:, 1].dropna().to_numpy()
axs[0,0].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d4.iloc[0:, 0].dropna().to_numpy(); gr = d4.iloc[0:, 1].dropna().to_numpy()
axs[1,0].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d7.iloc[0:, 0].dropna().to_numpy(); gr = d7.iloc[0:, 1].dropna().to_numpy()
axs[2,0].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d2.iloc[0:, 0].dropna().to_numpy(); gr = d2.iloc[0:, 1].dropna().to_numpy()
axs[0,1].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d5.iloc[0:, 0].dropna().to_numpy(); gr = d5.iloc[0:, 1].dropna().to_numpy()
axs[1,1].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d8.iloc[0:, 0].dropna().to_numpy(); gr = d8.iloc[0:, 1].dropna().to_numpy()
axs[2,1].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d3.iloc[0:, 0].dropna().to_numpy(); gr = d3.iloc[0:, 1].dropna().to_numpy()
axs[0,2].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d6.iloc[0:, 0].dropna().to_numpy(); gr = d6.iloc[0:, 1].dropna().to_numpy()
axs[1,2].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

r = d9.iloc[0:, 0].dropna().to_numpy(); gr = d9.iloc[0:, 1].dropna().to_numpy()
axs[2,2].plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.25)

axs[2,0].set_xlabel(r'$r/\sigma$',fontsize=12)
axs[2,1].set_xlabel(r'$r/\sigma$',fontsize=12)
axs[2,2].set_xlabel(r'$r/\sigma$',fontsize=12)

left, bottom, width, height = [0.24, 0.76, 0.1, 0.1]
inset0 = fig.add_axes([left, bottom, width, height])
inset0.set_ylim([0.17, 1.55]); inset0.set_yticks([0.5, 1, 1.5])
inset0.set_xlim([0, 8]); inset0.set_xticks([0,1,2,3,4,5,6,7,8])
inset0.tick_params(bottom = True, top = True, right = True, direction = "in")
inset0.set_ylabel(r'$S_{11}$(k)',fontsize=8)
inset0.set_xlabel(r'$k \sigma$',fontsize=8)
inset0.tick_params(axis='x',labelsize = 7); inset0.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.5125, 0.76, 0.1, 0.1]
inset1 = fig.add_axes([left, bottom, width, height])
inset1.set_ylim([0.17, 1.55]); inset1.set_yticks([0.5, 1, 1.5])
inset1.set_xlim([0, 8]); inset1.set_xticks([0,1,2,3,4,5,6,7,8])
inset1.tick_params(bottom = True, top = True, right = True, direction = "in")
inset1.set_ylabel(r'$S_{11}$(k)',fontsize=8)
inset1.set_xlabel(r'$k \sigma$',fontsize=8)
inset1.tick_params(axis='x',labelsize = 7); inset1.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.785, 0.76, 0.1, 0.1]
inset2 = fig.add_axes([left, bottom, width, height])
inset2.set_ylim([0.17, 1.55]); inset2.set_yticks([0.5, 1, 1.5])
inset2.set_xlim([0, 8]); inset2.set_xticks([0,1,2,3,4,5,6,7,8])
inset2.tick_params(bottom = True, top = True, right = True, direction = "in")
inset2.set_ylabel(r'$S_{11}$(k)',fontsize=8)
inset2.set_xlabel(r'$k \sigma$',fontsize=8)
inset2.tick_params(axis='x',labelsize = 7); inset2.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.24, 0.49, 0.1, 0.1]
inset3 = fig.add_axes([left, bottom, width, height])
inset3.set_ylim([-0.5, 0.7]); inset3.set_yticks([-0.5, 0, 0.5])
inset3.set_xlim([0, 8]); inset3.set_xticks([0,1,2,3,4,5,6,7,8])
inset3.tick_params(bottom = True, top = True, right = True, direction = "in")
inset3.set_ylabel(r'$S_{12}$(k)',fontsize=8)
inset3.set_xlabel(r'$k \sigma$',fontsize=8)
inset3.tick_params(axis='x',labelsize = 7); inset3.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.5125, 0.49, 0.1, 0.1]
inset4 = fig.add_axes([left, bottom, width, height])
inset4.set_ylim([-0.5, 0.7]); inset4.set_yticks([-0.5, 0, 0.5])
inset4.set_xlim([0, 8]); inset4.set_xticks([0,1,2,3,4,5,6,7,8])
inset4.tick_params(bottom = True, top = True, right = True, direction = "in")
inset4.set_ylabel(r'$S_{12}$(k)',fontsize=8)
inset4.set_xlabel(r'$k \sigma$',fontsize=8)
inset4.tick_params(axis='x',labelsize = 7); inset4.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.785, 0.49, 0.1, 0.1]
inset5 = fig.add_axes([left, bottom, width, height])
inset5.set_ylim([-0.5, 0.7]); inset5.set_yticks([-0.5, 0, 0.5])
inset5.set_xlim([0, 8]); inset5.set_xticks([0,1,2,3,4,5,6,7,8])
inset5.tick_params(bottom = True, top = True, right = True, direction = "in")
inset5.set_ylabel(r'$S_{12}$(k)',fontsize=8)
inset5.set_xlabel(r'$k \sigma$',fontsize=8)
inset5.tick_params(axis='x',labelsize = 7); inset5.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.24, 0.22, 0.1, 0.1]
inset6 = fig.add_axes([left, bottom, width, height])
inset6.set_ylim([0, 6.85]); inset6.set_yticks([0, 2, 4, 6])
inset6.set_xlim([0, 8]); inset6.set_xticks([0,1,2,3,4,5,6,7,8])
inset6.tick_params(bottom = True, top = True, right = True, direction = "in")
inset6.set_ylabel(r'$S_{22}$(k)',fontsize=8)
inset6.set_xlabel(r'$k \sigma$',fontsize=8)
inset6.tick_params(axis='x',labelsize = 7); inset6.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.5125, 0.22, 0.1, 0.1]
inset7 = fig.add_axes([left, bottom, width, height])
inset7.set_ylim([0, 6.85]); inset7.set_yticks([0, 2, 4, 6])
inset7.set_xlim([0, 8]); inset7.set_xticks([0,1,2,3,4,5,6,7,8])
inset7.tick_params(bottom = True, top = True, right = True, direction = "in")
inset7.set_ylabel(r'$S_{22}$(k)',fontsize=8)
inset7.set_xlabel(r'$k \sigma$',fontsize=8)
inset7.tick_params(axis='x',labelsize = 7); inset7.tick_params(axis='y',labelsize=7)

left, bottom, width, height = [0.785, 0.22, 0.1, 0.1]
inset8 = fig.add_axes([left, bottom, width, height])
inset8.set_ylim([0, 6.85]); inset8.set_yticks([0, 2, 4, 6])
inset8.set_xlim([0, 8]); inset8.set_xticks([0,1,2,3,4,5,6,7,8])
inset8.tick_params(bottom = True, top = True, right = True, direction = "in")
inset8.set_ylabel(r'$S_{22}$(k)',fontsize=8)
inset8.set_xlabel(r'$k \sigma$',fontsize=8)
inset8.tick_params(axis='x',labelsize = 7); inset8.tick_params(axis='y',labelsize=7)


DFTdata = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/insetLiterature.csv', sep =',', skiprows = 1 ,header=None)

r = DFTdata.iloc[0:, 0].dropna().to_numpy(); gr = DFTdata.iloc[0:, 1].dropna().to_numpy()
inset0.plot(r,gr,color="black")
r = DFTdata.iloc[0:, 2].dropna().to_numpy(); gr = DFTdata.iloc[0:, 3].dropna().to_numpy()
inset1.plot(r,gr,color="red")
r = DFTdata.iloc[0:, 4].dropna().to_numpy(); gr = DFTdata.iloc[0:, 5].dropna().to_numpy()
inset2.plot(r,gr,color="blue")
r = DFTdata.iloc[0:, 6].dropna().to_numpy(); gr = DFTdata.iloc[0:, 7].dropna().to_numpy()
inset3.plot(r,gr,color="black")
r = DFTdata.iloc[0:, 8].dropna().to_numpy(); gr = DFTdata.iloc[0:, 9].dropna().to_numpy()
inset4.plot(r,gr,color="red")
r = DFTdata.iloc[0:, 10].dropna().to_numpy(); gr = DFTdata.iloc[0:, 11].dropna().to_numpy()
inset5.plot(r,gr,color="blue")
r = DFTdata.iloc[0:, 12].dropna().to_numpy(); gr = DFTdata.iloc[0:, 13].dropna().to_numpy()
inset6.plot(r,gr,color="black")
r = DFTdata.iloc[0:, 14].dropna().to_numpy(); gr = DFTdata.iloc[0:, 15].dropna().to_numpy()
inset7.plot(r,gr,color="red")
r = DFTdata.iloc[0:, 16].dropna().to_numpy(); gr = DFTdata.iloc[0:, 17].dropna().to_numpy()
inset8.plot(r,gr,color="blue")


d1 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr11case1.dat.SQ.dat', sep =' ', skiprows = 1 ,header=None)
r = d1.iloc[0:, 0].dropna().to_numpy(); gr = d1.iloc[0:, 1].dropna().to_numpy()
inset0.plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.2)

d2 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr11case2.dat.SQ.dat', sep =' ', skiprows = 1 ,header=None)
r = d2.iloc[0:, 0].dropna().to_numpy(); gr = d2.iloc[0:, 1].dropna().to_numpy()
inset1.plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.2)

d4 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr12case1.dat.SQ.dat', sep =' ', skiprows = 1 ,header=None)
r = d4.iloc[0:, 0].dropna().to_numpy(); gr = d4.iloc[0:, 1].dropna().to_numpy()
gr = gr - 1
inset3.plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.2)

d5 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr12case2.dat.SQ.dat', sep =' ', skiprows = 1 ,header=None)
r = d5.iloc[0:, 0].dropna().to_numpy(); gr = d5.iloc[0:, 1].dropna().to_numpy()
gr = gr - 1
inset4.plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.2)

d7 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr22case1.dat.SQ.dat', sep =' ', skiprows = 1 ,header=None)
r = d7.iloc[0:, 0].dropna().to_numpy(); gr = d7.iloc[0:, 1].dropna().to_numpy()
inset6.plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.2)

d8 = pd.read_csv('/home/wtf8hu/lammps_install/Personal/sk+rdfFigure/gofr22case2.dat.SQ.dat', sep =' ', skiprows = 1 ,header=None)
r = d8.iloc[0:, 0].dropna().to_numpy(); gr = d8.iloc[0:, 1].dropna().to_numpy()
inset7.plot(r,gr,color="m",linestyle = "", marker='*',markersize=1.2)


plt.show()