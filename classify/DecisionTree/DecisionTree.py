# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:02:42 2018

@author: Administrator
"""
import math
import numpy as ny
import operator
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
计算给定数据集的基尼不纯度
输入二维数组，每行最后一个元素为标签，numpy array 或python 内置array都可以
'''
def calcGiniImpurity(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    giniImpurity=1
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries#频率用来代替概率
        giniImpurity-=prob*prob
    return giniImpurity


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

'''
返回信息增益最大的特征
输入：数据集，二维数组，最后一列为标签
输出：信息增益最大的特征编号
'''
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
返回列表中出现次数最高的元素
'''
       
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]

'''
创建决策树
输入：dataSet数据集二维矩阵，最后一列为标签
     labels每一列特征的含义
输出：决策树，字典表示
'''
def createTree(dataSet,labels):
    subLabels=labels[:]#拷贝一份数据而不是引用
    classList=[example[-1] for example in dataSet]#列表最后一列
    if classList.count(classList[0])==len(classList):#类别相同则停止继续划分
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)#遍历完所有特征时返回出现次数最高的类别
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=subLabels[bestFeat]
    myTree={bestFeatLabel:{}}
    del(subLabels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        #subLabels=labels[:]#拷贝一份数据而不是引用
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree
'''
计算树的叶子树
输入：决策树，字典表示
输出：叶子数量
'''
def getNumLeafs(myTree):
    numLeafs=0
    firstStr=list(myTree.keys())[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            numLeafs+=getNumLeafs(secondDict[key])
        else:
            numLeafs+=1
    return numLeafs
'''
计算树的深度,不算叶子节点，即树的深度等于最大决策次数
输入：决策树，字典表示
输出：树的深度
'''            
def getTreeDepth(myTree):
    maxDepth=0
    firstStr=list(myTree.keys())[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth=1+getTreeDepth(secondDict[key])
        else:
            thisDepth=1
        if thisDepth>maxDepth:
            maxDepth=thisDepth
    return maxDepth
    
'''
存储树
'''
def storeTree(inputTree,fileName):
    import pickle
    fw=open(fileName,'w')
    pickle.dump(inputTree,fw)
    fw.close()

'''
读取树
'''
def grabTree(fileName):
    import pickle
    fr=open(fileName)
    return pickle.load(fr)

'''
选择最好的数据集划分方式
'''
'''
dataSet=[[1,4,6,6,3,1],
         [3,4,5,8,2,9],
         [6,3,7,9,2,4],
         [8,3,4,5,7,1],
         [9,6,1,2,9,4],
         [6,4,5,1,2,7],
         [8,8,5,2,3,1]]

dataSetFish=[['Y','Y','Y'],
             ['Y','Y','Y'],
             ['Y','N','N'],
             ['N','Y','N'],
             ['N','Y','N']
             ]
labels=['surfacing','have leg']
a=createTree(dataSetFish,labels)
leafNum=getNumLeafs(a)
depth=getTreeDepth(a)
print(a)
print(leafNum)
print(depth)
#c=dict(a='aaa',b='bbb',c='ccc',d='ddd')
#print(c)
#myKeys=list(c.keys())[0]
#print(myKeys)
'''
