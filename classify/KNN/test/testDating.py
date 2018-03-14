# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:53:30 2018

@author: Administrator
"""
import sys
sys.path.append('../')
sys.path.append('../../../prepare')
import getData
import KNN
import normalization

'''
检测算法的错误率
'''
def datingClassTest():
    hoRatio=0.10#测试样本占总样本的比例
    k=7#
    datingDataMat,datingLabels=getData.file2Matrix('../datas/datingTestSet2.txt')
    normMat=normalization.normalize(datingDataMat)
    m=normMat.shape[0]#行数
    numTestVecs=int(m*hoRatio)#测试样本数
    errorCount=0#错误样本数
    for i in range(numTestVecs):
        classifierResult=KNN.KNN(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],k)
        if(classifierResult!=datingLabels[i]):
            errorCount+=1
    return float(errorCount)/float(numTestVecs)
    