#利用python仿真双缝实验
import numpy as np
import matplotlib.pyplot as plt
import math

#表示长度的物理量单位m
#波长
wavelengthR=float(7e-6)
wavelengthG=float(5.5e-6)
wavelengthB=float(4.7e-6)
#双缝间距
d_slit=float(0.002)
#缝到屏幕的距离
d_screen=float(1.0)

ym=50.0*wavelengthR*d_screen/d_slit
#xs=ym
distance=ym/500.0
ys=np.arange(-ym,ym,distance)
len_dis=len(ys)
B = [([0.0] * len_dis) for i in range(len_dis)]
Br = [([0.0] * len_dis) for i in range(len_dis)]
N=255.0
for i in range(0,len_dis):
    r1=math.sqrt((ys[i]-d_slit/2)**2+d_screen**2)
    r2=math.sqrt((ys[i]+d_slit/2)**2+d_screen**2)
    phiR=2.0*math.pi*(r2-r1)/wavelengthR
    phiG=2.0*math.pi*(r2-r1)/wavelengthG
    phiB=2.0*math.pi*(r2-r1)/wavelengthB
    tempR=4.0*math.cos(phiR/2)**2
    tempG=4.0*math.cos(phiG/2)**2
    tempB=4.0*math.cos(phiB/2)**2
    for j in range(0,len_dis):
        #B[j][i]=np.array([temp,0,0])
        #Br[j][i]=B[j][i]/4.0*N
        #print(temp/4.0*N)
        Br[j][i]=[tempR/4,tempG/4,tempB/4]

plt.title("double_slit_experiment")
plt.imshow(Br)
plt.show()
