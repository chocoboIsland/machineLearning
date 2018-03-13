# -*- coding: utf-8 -*-
"""
归一化矩阵
输入：numpy矩阵
输入：归一化后的矩阵
"""
import numpy as ny
def normalize(iMat):
    row=iMat.shape[1]#列数
    line=iMat.shape[0]#行数
    max=[-99999999]*row#[-9999999]*row
    min=[99999999]*row
    for i in range(row):
        for j in range(line):
            if iMat[j,i]>max[i]:
                max[i]=iMat[j,i]
            if iMat[j,i]<min[i]:
                min[i]=iMat[j,i]
    lens=[0]*row
    for k in range(row):
        lens[k]=max[k]-min[k]
    for m in range(line):
        for n in range(row):
            if abs(lens[n]<0.005):
                if abs(iMat[m,n])<=0.005:
                    iMat[m,n]=0.0
                else:
                    iMat[m,n]=1.0
            else:
                iMat[m,n]=(iMat[m,n]-min[n])/lens[n]
    return iMat
    
'''
测试案例   
a=ny.mat([[7.8,2.4,3.7,0],[2.4,5.2,9,0],[0.5,8,4.4,0]])
an=normalize(a)
print(an)
#结果应该为
#[[1.         0.         0.         0.        ]
#[0.26027397 0.5        1.         0.        ]
# [0.         1.         0.13207547 0.        ]]
'''