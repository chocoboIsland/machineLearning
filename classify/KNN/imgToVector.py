# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:53:57 2018
将32*32图像转化为1*1024的numpy数组
输入：图像文件字符串
输出：向量 numpy 1*1024
@author: Administrator
"""
import numpy as ny
import os
import KNN
import zipfile





def img2Vector(filename):
    returnVector=ny.zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVector[0,32*i+j]=int(lineStr[j])
    return returnVector
    
    
def handwritingClassTest():
    hwLabels=[]
    zTrainingFiles=zipfile.ZipFile("datas/trainingDigits.zip")
    trainingFileList=zTrainingFiles.namelist()
    del(trainingFileList[0])
    print(trainingFileList)
    #trainingFileList=os.listdir("datas/trainingDigits")
    m=len(trainingFileList)#文件数量
    trainingMat=ny.zeros((m,1024))
    for i  in range(m):
        fileNameStr=trainingFileList[i].split('/')[1]#文件名
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])#数字
        hwLabels.append(classNumStr)
        trainingMat[i,:]=img2Vector("datas/trainingDigits/%s" % fileNameStr)
    testFileList=os.listdir("datas/testDigits")
    errorCount=0
    mTest=len(testFileList)
    print(mTest)
    for j in range(mTest):
        fileNameStr=testFileList[j]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split("_")[0])
        vectorUnderTest=img2Vector("datas/testDigits/%s" %fileNameStr)
        classiferResult=KNN.KNN(vectorUnderTest,trainingMat,hwLabels,3)
        print("the classifier came back with: %d,the real answer is:%d " % (classiferResult,classNumStr))
        if classiferResult!=classNumStr:
            errorCount+=1
            print("error text is:"+fileNameStr)
    return float(errorCount)/float(mTest)
    
a=handwritingClassTest()
print(a)
b=[123,21,11,34]
del(b[0])
print(b)       
        
    
    

    
