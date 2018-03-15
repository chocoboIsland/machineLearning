# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:02:42 2018

@author: Administrator
"""
import math
import numpy as ny
'''
计算给定数据集的香农熵
输入二维数组，每行最后一个元素为标签，numpy array 或python 内置array都可以
'''
def calcShannonEntropy(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEntropy=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries#频率用来代替概率
        shannonEntropy+=(-prob*math.log(prob,2))
    return shannonEntropy

'''
按照给定特征划分数据集
输入：dataSet待划分的数据集
     axis划分数据集的特征
     value需要返回的特征的值
'''
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    bestEntropy=calcShannonEntropy(dataSet)#源数据集香农熵
    bestInfoGain=0.0
    bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]#第i列数据
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEntropy(subDataSet)
        infoGain=bestEntropy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature
        
            
        
        
        
        
'''
选择最好的数据集划分方式
'''
dataSet=[[1,4,6,6,3,1],
         [3,4,5,8,2,9],
         [6,3,7,9,2,4],
         [8,3,4,5,7,1],
         [9,6,1,2,9,4],
         [6,4,5,1,2,7],
         [8,8,5,2,3,1]]

#e=[d[1] for d in dataSet]
#c=splitDataSet(dataSet,1,3)
#print(c)
e=set("hello")
e.add('da')
#help(set)
print(e)
