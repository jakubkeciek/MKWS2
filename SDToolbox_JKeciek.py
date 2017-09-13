import numpy as np
import SDToolbox as sdt
import matplotlib.pyplot as plt




def contourPlot(z, x,y, xlabel, ylabel, fig_name):
    plt.figure()
    plt.imshow(z, vmin=z.min(), vmax=z.max(), origin='lower',
               extent=[x.min(), x.max(), y.min(), y.max() ], aspect='auto')
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.colorbar()
    plt.savefig(fig_name + '.png')
    

mech = 'wang_highT.cti';
resolution = 20

#arrays of initial parameters

P_init =    np.linspace(1, 8, resolution)
T_init =    np.linspace(250, 1000, resolution) 
phi_init =  np.linspace(0.8, 1.8, resolution)


#arrays of calculated parameters


CJ_vel= np.zeros([resolution,resolution])
CJ_P =  np.zeros([resolution,resolution])
CJ_T =  np.zeros([resolution,resolution])



#create phi-P plot with fixed temperature T = 297K
T = 297
i=0

for P in P_init:
    j = 0
    for phi in phi_init:
        composition = 'CH4:' + str(phi*0.5) + ' O2:1 N2:3.76'
        [cj_vel,R2] = sdt.CJspeed(P * 1e5, T, composition , mech , 1);    
        gas = sdt.PostShock_eq(cj_vel, P * 1e5 , T, composition, mech) 
        CJ_P[i,j] = gas.P * 1e-5
        CJ_T[i,j] = gas.T
        CJ_vel[i,j] =  cj_vel 
        j = j + 1
    i = i + 1
    
    
contourPlot(CJ_P, phi_init, P_init, r'$ \phi \quad [-])$', r'$ P \quad [atm])$', 'CJ_P(phi,P)')
contourPlot(CJ_T, phi_init, P_init, r'$ \phi \quad [-])$', r'$ P \quad [atm])$', 'CJ_T(phi,P)')
contourPlot(CJ_vel, phi_init, P_init, r'$ \phi \quad [-])$', r'$ P \quad [atm])$', 'CJ_V(phi,P)')
        
        
#create phi-T plot with fixed temperature p = 1 bar
P = 1
i=0

for T in T_init:
    j = 0
    for phi in phi_init:
        print T,phi
        composition = 'CH4:' + str(phi*0.5) + ' O2:1 N2:3.76'
        [cj_vel,R2] = sdt.CJspeed(P * 1e5, T, composition , mech , 1);    
        gas = sdt.PostShock_eq(cj_vel, P * 1e5 , T, composition, mech) 
        CJ_P[i,j] = gas.P * 1e-5
        CJ_T[i,j] = gas.T
        CJ_vel[i,j] =  cj_vel 
        j = j + 1
    i = i + 1
    
    
contourPlot(CJ_P, phi_init, T_init, r'$ \phi \quad [-])$', r'$ T \quad [K])$', 'CJ_P(phi,T)')
contourPlot(CJ_T, phi_init, T_init, r'$ \phi \quad [-])$', r'$ T \quad [K])$', 'CJ_T(phi,T)')
contourPlot(CJ_vel, phi_init, T_init, r'$ \phi \quad [-])$', r'$ T \quad [K])$', 'CJ_V(phi,T)')
        
        
#create phi-P plot with fixed equivalence ratio phi = 1
phi = 1
i=0

for P in P_init:
    j = 0
    for T in T_init:
        print T,P
        composition = 'CH4:' + str(phi*0.5) + ' O2:1 N2:3.76'
        [cj_vel,R2] = sdt.CJspeed(P * 1e5, T, composition , mech , 1);    
        gas = sdt.PostShock_eq(cj_vel, P * 1e5 , T, composition, mech) 
        CJ_P[i,j] = gas.P * 1e-5
        CJ_T[i,j] = gas.T
        CJ_vel[i,j] =  cj_vel 
        j = j + 1
    i = i + 1
    
    
contourPlot(CJ_P, T_init, P_init, r'$ T \quad [K])$', r'$ P \quad [atm])$', 'CJ_P(T,P)')
contourPlot(CJ_T, T_init, P_init, r'$ T \quad [K])$', r'$ P \quad [atm])$', 'CJ_T(T,P)')
contourPlot(CJ_vel, T_init, P_init, r'$ T \quad [K])$', r'$ P \quad [atm])$', 'CJ_V(T,P)')