import scipy as sp
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import scipy.optimize as optimization
import mpl_toolkits.mplot3d.axes3d as p3
p=2
Debyek=0.985
N1=4
N2=4
def discrete_func1(q,kappa,MinPath):
  ans=[]
  for q0 in q: 
    sum=0.0  
    i=0
    N3=6
    if (abs(q0)>10e-10):
      N3=round(2*sp.pi/q0,0)
      N3=int(N3)
    first1=-N1+1
    last1=N1+1
    first2=-N2+1
    last2=N2+1
    first3=-N3+1
    last3=N3+1
    result=0.0
    for n1 in range(first1,last1):
      for n2 in range(first2,last2):
        for n3 in range(first3,last3):
          if ((-2*N2*N3*n1+2*N1*N3*n2+2*N1*N2*n3>-3*N1*N2*N3)and(-2*N2*N3*n1+2*N1*N3*n2+2*N1*N2*n3<3*N1*N2*N3+1)and(+2*N2*N3*n1-2*N1*N3*n2+2*N1*N2*n3>-3*N1*N2*N3)and(+2*N2*N3*n1-2*N1*N3*n2+2*N1*N2*n3<3*N1*N2*N3+1)and(+2*N2*N3*n1+2*N1*N3*n2-2*N1*N2*n3>-3*N1*N2*N3)and(+2*N2*N3*n1+2*N1*N3*n2-2*N1*N2*n3<3*N1*N2*N3+1)and(+2*N2*N3*n1+2*N1*N3*n2+2*N1*N2*n3>-3*N1*N2*N3)and(+2*N2*N3*n1+2*N1*N3*n2+2*N1*N2*n3<3*N1*N2*N3+1)):
             x1=n1/float(N1)
             x2=n2/float(N2)
             x3=n3/float(N3)             
             sq=x1**2+x2**2+x3**2
             if (0!=sq):
               i+=1
               v=(n1/float(N1)+n2/float(N2)-n3/float(N3))/np.sqrt(3.0)
               k=np.sqrt(x1**2+x2**2+x3**2)
#               if (v>k):
#                  print v,k
               result=result+((v**2)/sq)*((Debyek/k)**p)/(1+4*((np.sin(q0/2))**2)*(MinPath*(v/k)*((Debyek/k)**p)+(MinPath*(v/k)*((Debyek/k)**p))**2))
    result=result/(N3*N1*N2*4)*(3-p)*((np.cos(q0/2))**2)
    ans.append(result*kappa)
    print i,'==',N1*N2*4*N3,'(N=',N3,')'
  return ans
File=open('cross2.dat','w')
q=list(np.arange(10,99+1,1))
for i in range(4,11,1):
  #y=discrete_func1([2*sp.pi/q0],1,0.615140781881)
  N1=i
  N2=i
  y=discrete_func1([2*sp.pi/q[0]],1,10)
  print >>File,i,y[0]
File.close()
