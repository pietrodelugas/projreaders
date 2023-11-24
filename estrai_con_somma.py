# %%
from collections import deque
import numpy as np

class MyData: 
    def __init__(self, record):
        r0 = record[0].split() 
        self.ik = int(r0[0])
        self.energy = float(r0[1]) 
        self.pdos = float(r0[2]) 
        self.sigmax = float(record[2].split()[0])
        self.sigmay = float(record[3].split()[0])
        self.sigmaz = float(record[4].split()[0]) 

    def write_flatbands(self, fw, Emax):
        fw.write(f"{self.ik}  {self.energy} {self.pdos} \n" ) 
        if self.energy == Emax:
            fw.write("\n")

    def write_atomic_sigmas(self, fw, Emax):
        fw.write(f"{self.ik} {self.energy} " +
                 f"{self.sigmax} {self.sigmay} {self.sigmaz}\n")
        if self.energy == Emax:
            fw.write("\n") 

    def __add__(self, data):
        res = object.__new__(MyData)
        res.ik = self.ik
        res.energy = self.energy
        res.pdos = self.pdos + data.pdos
        res.sigmax = self.sigmax + data.sigmax
        res.sigmay = self.sigmay + data.sigmay
        res.sigmaz = self.sigmaz + data.sigmaz
        return res

    def __mul__(self, fac):
        res = object.__new__(MyData)
        res.pdos = self.pdos * float(fac)
        res.sigmax = self.sigmax * float(fac) 
        res.sigmay = self.sigmay * float(fac) 
        res.sigmaz = self.sigmaz * float(fac) 
        return res 

class MyDataArray:
    def __init__(self, array):
        self.ik = [_.ik for _ in array]
        self.energy = np.array([_.energy for _ in array])
        self.pdos  = np.array([_.pdos for _ in array]) 
        self.sigma = np.array(list(map(lambda d:[d.sigmax, d.sigmay, d.sigmaz], array)))
 
    def __add__(self, other):
        res = MyDataArray.__new__(MyDataArray) 
        res.ik = self.ik 
        res.energy = self.energy
        if type(other) is list:
            res.pdos = self.pdos + np.array([_.pdos for _ in other]) 
            res.sigma = self.sigma + np.array (list(map(lambda d: [d.sigmax, d.sigmay, d.sigmaz], other)))
        elif type(other) is MyDataArray:
            res.pdos = self.pdos + other.pdos
            res.sigma = self.sigma + other.sigma
        else:
            raise TypeError
        return res 

    def __mul__(self, other):
        res = object.__new__(MyDataArray)
        res.ik = self.ik
        res.energy = self.energy
        res.pdos = float(other) * self.pdos
        res.sigma = float(other) * self.sigma
        return res

    def writesigma(self, fw):
        Emax = max(self.energy)
        record = ['go']
        iterator = zip(self.ik, self.energy, self.sigma)
        while record:
            record = next(iterator, None)
            if record:
                atomicsigma = " ".join([f"{record[2][i]:12.8f}" for i in range(3)])
                line = f"{record[0]:5d}   {record[1]:6.3f}  {atomicsigma}\n"
                fw.write(line)
                if record[1] == Emax:
                    fw.write("\n")
    
    def writepdos(self, fw):
        Emax = max(self.energy)
        record = ['go']
        iterator = zip(self.ik, self.energy, self.pdos)
        while record:
            record = next(iterator, None)
            if record:
                line = f"{record[0]:5d}  {record[1]:6.3f}  {record[2]:12.8f}\n"
                fw.write(line)
                if record[1] == Emax:
                    fw.write("\n")
            

        
                                
         
        

        
            
        

  
  


def get_emax(filename): 
    with open(filename, 'r') as fr:
        header = next(fr)
        pdoslen = len(header.split()) - 2
        firstentry = next(fr)
        queue = (_ for _ in fr if len(_.split()) == pdoslen)
        lastentry = deque(queue, maxlen=1)[0]
    return float(firstentry.split()[1]), float(lastentry.split()[1])


def get_record(fr, Emax):
    record = ['go']
    while record[0]:
        record = [next(fr, None) for i in range(6)]
        if record[0]:
            energy = float(record[0].split()[1])
            if energy == Emax: 
                next(fr)
            yield MyData(record)
        else:
            break  
 
       

def read_data(**kwargs):
    iat = kwargs['iat']
    iwfc = kwargs['iwfc']
    labels = kwargs['labels']
    proj_dir = kwargs['proj_dir']
    filprojroot = kwargs['filprojroot']
    symbol = kwargs['symbol']
    filename = f"{proj_dir}/{filprojroot}.pdos_atm#{iat}({symbol})_wfc#{iwfc}({labels[iwfc]})"
    Emin, Emax = get_emax(filename)
    with open(filename,'r') as fr: 
        next(fr) 
        datait = get_record(fr, Emax)
        data = [_ for _ in datait]
    return Emin, Emax, data 


#if __name__ == "__main__":
#    import numpy as np
#    read_args = {
#        'iat':  1,
#        'iwfc': 4,
#         'labels': ["","s_j0.5", 
#                    "p_j1.5",
#                    "p_j0.5",
#                    "d_j2.5",
#                    "d_j1.5",
#                    "s_j0.5"],
#         'proj_dir':"../31_XGX/",
#         'filprojroot':"pdos31_XGX"}
  
#    
  
  
#    def weight(iat):
#       return exp(-n * 2.6254 / 10.0) 
  
#    zfac = sum([weight(i) for i in range(10)])  
#     
#    emin, emax, data = read_data(**read_args) 
#    sigmas = np.array([[_.sigmax, _.sigmay, _.sigmaz] for _ in data])/zfac
#        for iat in range(1,10):
#            read_args.update{"iat":iat}
#            _,_,data = read_data(**read_args)
#        
#        
#    with open('prova_pdos', 'w') as fw:
#        with open('prova_sigma', 'w') as fsw: 
#            deque(((_.write_flatbands(fw, emax),_.write_atomic_sigmas(fsw,emax)) for _ in data),maxlen=0) 
  
# %%
