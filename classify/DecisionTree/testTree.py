# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:14:32 2018

@author: Administrator
"""

import DecisionTree
import drawDecisionTree
def classify(inputTree,featLabels,testVec):
    firstStr=list(inputTree.keys())[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)#将标签字符串转化为索引
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=="dict":
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel

fr=open('datas/lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age','prescript','astigmatic','tearRate']
lensesTree=DecisionTree.createTree(lenses,lensesLabels)
#drawDecisionTree.createPlot(lensesTree)

            
