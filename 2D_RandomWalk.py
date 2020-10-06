# Jake Geiser
# Initial September 10, 2018
# Updated October 6, 2020

import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit
from matplotlib.animation import FuncAnimation

def func(t,D):
    return 4*D*t #=<x^2> - mean-squared displacement for diffusion in 2D 

# Do the walk, provide number of walks(nwalks) and number of steps each walk(nsteps)
nsteps = 1000 ; nwalks = 500
diff = np.zeros(nwalks) # coefficent of diffusion D
finalR = np.zeros(nwalks)
for j in range(0,nwalks):
    # if j == 0: # For the purpose of making a gif of a random walk
    #     Sx = [0]
    #     Sy = [0]
    #     r2 = [0]
    #     for i in range(nsteps): # choose next step
    #         d = np.random.randint(1,4+1)
    #         if d == 1: 
    #             Sx.append(Sx[i-1]+1)
    #             Sy.append(Sy[i-1])
    #         if d == 2:
    #             Sx.append(Sx[i-1]-1)
    #             Sy.append(Sy[i-1])
    #         if d == 3: 
    #             Sy.append(Sy[i-1]+1)
    #             Sx.append(Sx[i-1])
    #         if d == 4: 
    #             Sy.append(Sy[i-1]-1)
    #             Sx.append(Sx[i-1])
    #         # print(i, Sx[i])
    #         r2.append(Sx[i]**2.+Sy[i]**2.)
    #     # Make animation
    #     fig, ax = plt.subplots(figsize=(6,6))
    #     ax.set_ylim(np.min(Sy)-1,np.max(Sy)+1)
    #     ax.set_xlim(np.min(Sx)-1,np.max(Sx)+1)
    #     ax.set_xlabel("X position")
    #     ax.set_ylabel("Y position")
    #     def animate(i):
    #         ax.plot(Sx[i],Sy[i],'ro')
    #         # if i>0:
    #         #     ax.plot(Sx[i-1:i],Sy[i-2:i], 'r-')
    #         ax.set_title(f"Step {i} of {nsteps}",fontsize=18)
    #         ax.grid(True)
    #     anim = FuncAnimation(fig, animate, frames=len(Sx), interval = 20)
    #     anim.save("images/2D_RW2.gif",dpi=80, writer='imagemagick')
    # else:
    Sx = 0
    Sy = 0
    r2 = np.zeros(nsteps+1)
    r2[0] = 0
    for i in range(nsteps): # choose next step
        d = np.random.randint(1,4+1)
        if d == 1: Sx+=1
        if d == 2: Sx-=1
        if d == 3: Sy+=1
        if d == 4: Sy-=1
        r2[i+1] = Sx**2.+Sy**2.
        # if r[i] == 0: # if statement to prevent log(0)
        #     r[i] = 0.00001
         
        
    # rl = np.log(r)
    # nl = np.log(range(1,nsteps+1))
    T = range(0,nsteps+1)
    r2_mean = np.zeros(len(r2))
    r2_mean[0] = 0
    for i in range(1,len(r2)):
        r2_mean[i] = np.mean(r2[0:i])
    par, con = curve_fit(func,T,r2_mean)
    diff[j] = par[0]
    finalR[j] = (np.sqrt(r2[-1]))

plt.figure(4)
plt.hist(diff, bins='auto')
plt.xlabel("Diffusion const (length^2/s)")
plt.ylabel("Count")
plt.title(f"Diffusion Constant Distribution for {nwalks} Discret Random Walks")
Dmean = np.mean(diff)
Dstd = np.std(diff)
plt.savefig("images/2D_hist_Diff.png")

print ('The average diffusion constant is ', Dmean)
print ('and the standard deviation is ', Dstd)
print("")

plt.figure(5)
plt.hist(finalR, bins='auto')
plt.xlabel("Displacement (length)")
plt.ylabel("Count")
plt.title(f"Final Displacement Distribution for {nwalks} Discret Random Walks")
Rmean = np.mean(finalR)
Rstd = np.std(finalR)
plt.savefig("images/2D_hist_r.png")

print ('The average final displacement is ', Rmean)
print ('and the standard deviation is ', Rstd)
