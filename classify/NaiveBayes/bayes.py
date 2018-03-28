# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:30:57 2018

@author: Administrator
"""

import numpy as np
import random
'''
创建实验样本

'''
def loadDataSet():
    postingList=['my dog has  flea problems help please'.split(),
                 'maybe not take him to dog park stupid'.split(),
                 'my dalmation is so cute I love him'.split(),
                 'stop posting stupid worthless garbage'.split(),
                 'mr licks ate my steak how to stop him'.split(),
                 'quit buying worthless dog food stupid'.split()]
    classVec=[0,1,0,1,0,1]#1代表侮辱性文字，0代表正常言论
    return postingList,classVec

'''
创建包含在所有文档中出现的不重复词的列表
'''
def createVocabList(dataSet):
    vocabSet=set([])#创建一个空集
    for document in dataSet:
        vocabSet=vocabSet|set(document)#创建两个集合的并集
    return list(vocabSet)

'''
返回词汇表中各单词在输入文档中是否出现，出现为1，不出现为0
输入:vocabList词汇表
    :inputSet 输入文档
输出：returnVec 返回一个与词汇表相同长度的列表，
                标识词汇表中的单词在输入文档中是否出现，1出现，0不出现
'''
def setOfWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print("the word: %s is not in my vocabulary" %word )
    return returnVec

'''
返回词汇表中各单词在输入文档中出现次数
输入:vocabList词汇表
    :inputSet 输入文档
输出：returnVec 返回一个与词汇表相同长度的列表，
                标识词汇表中的单词在输入文档中的出现次数
'''
def bagOfWords2VecMN(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
        else:
            print("the word: %s is not in my vocabulary" %word )
    return returnVec
    

'''
输入：trainMatrix文档矩阵，表示词汇中的各词是否出现
      trainCateGory类别标签
输出：p0Vect与词汇表同长度的向量，表示在非侮辱性语句中各词出现的概率
      p1Vect与词汇表同长度的向量，表示在侮辱性语句中各词出现的概率
      pAbusive 文档属于侮辱性文档的概率
'''
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)#词条数
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)#文档属于侮辱性文档的概率
    p0Num=np.ones(numWords)#将所有单词出现次数初始化为1
    p1Num=np.ones(numWords)
    p0Denom=2.0#非侮辱性语句中总的词汇数，初始化为2
    p1Denom=2.0#侮辱性语句中总的词汇数，初始化为2
    for i in range(numTrainDocs):
        if trainCategory[i]==1:#侮辱性
            p1Num+=trainMatrix[i]#侮辱性语句中各词出现的次数
            p1Denom+=sum(trainMatrix[i])#侮辱性语句中总的词汇数
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    p1Vect=np.log(p1Num/p1Denom)#侮辱性语句中各词出现的概率,再取对数
    p0Vect=np.log(p0Num/p0Denom)#非侮辱性语句中各词出现的概率,再取对数
    return p0Vect,p1Vect,pAbusive

'''
输入：vec2Classify要分类的向量
     p0Vec#非侮辱性语句中各词出现的概率,再取对数
     p1Vec#侮辱性语句中各词出现的概率,再取对数
     pClass1#文档属于侮辱性文档的概率
'''    
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+np.log(pClass1)
    p0=sum(vec2Classify*p0Vec)+np.log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0
   
def testingNB():
    listOPosts,listClasses=loadDataSet()
    myVocabList=createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb=trainNB0(np.array(trainMat),np.array(listClasses))
    testEntry='love my dalmation'.split()
    thisDoc=setOfWords2Vec(myVocabList,testEntry)
    print("thisEntry is "+str(classifyNB(thisDoc,p0V,p1V,pAb)))
    testEntry='stupid garbage'.split()
    thisDoc=setOfWords2Vec(myVocabList,testEntry)
    print("thisEntry is "+str(classifyNB(thisDoc,p0V,p1V,pAb)))

'''
将字符串分割为单词，并过滤掉长度小于3的单词
'''
def textParse(bigString):
    import re
    listOfTokens=re.split(r'\W+',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    docList=[]
    classList=[]
    fullText=[]
    for i in range(1,26):
        wordList=textParse(open('data/email/spam/%d.txt'% i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList=textParse(open('data/email/ham/%d.txt'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList=createVocabList(docList)#创建词汇表
    trainingSet=list(range(50))
    testSet=[]
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]
    trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNB0(np.array(trainMat),np.array(trainClasses))
    errorCount=0
    for docIndex in testSet:
        wordVector=setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
            errorCount+=1
    print('the error rate is'+str(float(errorCount)/len(testSet)))
    

    
        
        

     
'''
测试
'''
#testingNB()
spamTest()




