# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:16:41 2018
用于提取文本，生成训练样本矩阵和标签向量,
文本格式'a1\ta2\ta3\t...\ty1\nb1\tb2\tb3\t...\ty2\n'
abc为不同的样本，y1,y2,y3为不同的样本集
输入：文本地址字符串
输出：训练样本二维数组numpy mat N*M,N为样本数，M为样本维度
     类标签向量 [] N
@author: chocoboIsland
"""
import numpy as ny
def file2Matrix(filename):
    fr=open(filename)
    arrayOfLines=fr.readlines()
    numberOfLines=len(arrayOfLines)#样本数
    dataDimension=len(arrayOfLines[0].strip().split('\t'))-1#样本维度
    print(numberOfLines)
    returnMat=ny.zeros((numberOfLines,dataDimension))
    classLabelVector=[]
    index =0
    for line in arrayOfLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:dataDimension]
        classLabelVector.append(int(listFromLine[-1]))
        index=index+1
    fr.close()
    return returnMat,classLabelVector

'''     
iMat,labels=file2Matrix('datas\datingTestSet2.txt')
print(iMat)
print(labels)
'''


    



    
