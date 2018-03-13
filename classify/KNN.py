# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:00:14 2018
KNN算法
输入inX：输入向量numpy Array 一维
dataSet:训练样本集 numpy Array 二维
labels：标签向量numpy Array 一维
k:选择最邻近的数目 Integer 
输出：频率最高的标签，即k中的某个元素
@author: chocoboIsland
"""
import numpy as ny
import operator
def KNN(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=ny.tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistance=sqDiffMat.sum(axis=1)
    distances=sqDistance**0.5
    sortedDistIndices=distances.argsort() 
    classCount={}
    for i in range(k):
        voteIlabel=labels(sortedDistIndices[i])
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
        
#测试



    
