# %%
import numpy as np 
from sys import argv 
iat = int(argv[1])
iwfc= int(argv[2])
Emin = 0.000
Emax = 27.350
labels=["","s_j0.5", "p_j1.5", "p_j0.5", "d_j2.5", "d_j1.5", "s_j0.5"]
proj_dir = "../31_XGX/"
filprojroot = "pdos31_XGX"
filename = f"{proj_dir}/{filprojroot}.pdos_atm#{iat}(Cu)_wfc#{iwfc}({labels[iwfc]})"
with open(filename, 'r') as fr:
    next(fr)
    record = ['go']
    flatbands=open(f"./31_XGX/flatband_{iat}_{iwfc}",'w') 
    atomicsigmas = open(f"./31_XGX/sigma_at_{iat}_{iwfc}",'w')  
    while(record[0]):
        record_last = record
        record = [next(fr,None) for i in range(6)] 
        if record[0]:
            r0 = record[0].split() 
            ik = int(r0[0]) 
            energy = float(r0[1])
            pdos  = float(r0[2]) 
            if energy == Emax:
                next(fr)
            sigmax = float(record[2].split()[0])
            sigmay = float(record[3].split()[0])
            sigmaz = float(record[4].split()[0]) 
            flatbands.write(f"{ik}  {energy} {pdos}\n")                 
            atomicsigmas.write(f"{ik}  {energy} {sigmax}  {sigmay}  {sigmaz}\n") 
            if energy == Emax:
                flatbands.write("\n")
                atomicsigmas.write("\n")


                           
    
    


# %%


# %%
#record

# %%

#vals = lambda  ll: (int(ll[0]), float (ll[1]), float(ll[2]), float(ll[3]), float(ll[4]))
#def sumpari(sp1, sp2): 
#    try:
#      val = [sp1[0], sp1[1],]+[0.5 * (float(_[0])+float(_[1])) for _ in zip (sp1[2:],sp2[2:])]
#      return f"{val[0]}  {val[1]} {val[2]}  {val[3]}  {val[4]}\n"
#    except IndexError:
#        return "\n"
#
#
#def sumdispari(sp1, sp2): 
#    try:
#      val = [sp1[0], sp1[1],]+[0.5 * (float(_[0])-float(_[1])) for _ in zip (sp1[2:],sp2[2:])]
#      return f"{val[0]}  {val[1]} {val[2]}  {val[3]}  {val[4]}\n"
#    except IndexError:
#        return "\n"
#    
#def vals(sp1):
#    try:
#      val = [sp1[0], sp1[1],]+[ (float(_)) for _ in sp1[2:]]
#      return f"{val[0]}  {val[1]} {val[2]}  {val[3]}  {val[4]}\n"
#    except IndexError:
#        return "\n"
#
#
#
#
## %%
#
#
#with open("./YGY_degauss0025/sigma_at_1_4") as f1:
#    with open("./YGY_degauss0025/sigma_at_21_4") as f2:
#        a = [(_[0].split(), _[1].split()) for _ in zip(f1,f2)] 
#
#        
#
## %%
#from collections import deque 
#with open("somma_dispari_1_21_4","w") as fw:
#    queue = (fw.write(sumdispari(*_)) for _ in iter(a))
#    deque(queue, maxlen=0)
#
## %%
#from collections import deque 
#ik = 59
#ik0 = 51 
#ky = (ik-ik0)/50.0*0.7 
#print (ky)
#with open(f"plot_sigma_k_1_4_{ky:6.3f}", "w") as fw:
#    with open('./YGY_degauss0025/sigma_at_1_4', 'r') as fr: 
#        queue = (fw.write(vals(_.split())) for _ in filter(lambda _: _[:2] == "52" in _,fr ))
#        deque(queue) 
#        
#
## %%
#prova="1  3.445 1.03e-16  2.85e-24  -2.62e-20"
#
#
## %%
#prova.split()
#
#
#
#
## %%
#vals(prova.split())
#
## %%
#
#
#
