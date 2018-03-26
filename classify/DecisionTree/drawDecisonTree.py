# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:12:18 2018

@author: Administrator
"""
import numpy as np  
import matplotlib.pyplot as plt 
#增加下面三行配置信息用以显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题 

'''
添加父子节点连线中的文字
parentPt父节点坐标
nodePt此节点坐标
text文本内容
'''
def plotMidText(parentPt,nodePt,conditionText):
    #之所以除以1.5是为了让文本离父节点近一些
    xMid=nodePt[0]+(parentPt[0]-nodePt[0])/2
    yMid=nodePt[1]+(parentPt[1]-nodePt[1])/2
    plt.text(xMid, yMid,conditionText,fontdict={'size': 16, 'color': 'r'})  

'''
画树节点
text文本内容
nodePt节点坐标
'''
def drawRootAnnotate(text,nodePt):
     decisionNode=dict(boxstyle='sawtooth',fc='0.8')
     plt.annotate(s=text,xy=nodePt,fontsize=16,bbox=decisionNode)


'''
text文本内容
conditionText条件文本
parentPt父节点坐标
nodePt当前节点坐标
isLeftNode是否是叶子节点
'''
def drawAnnotate(text,conditionText,parentPt,nodePt,isLeftNode):
    decisionNode=dict(boxstyle='sawtooth',fc='0.8')
    leftNode=dict(boxstyle='round4',fc='0.8')
    if isLeftNode:
        nodeType=decisionNode
    else:
        nodeType=leftNode
    plt.annotate(s=text,xy=parentPt,xytext=(nodePt[0]-3*len(text),nodePt[1]),\
                  fontsize=16,arrowprops=dict(arrowstyle='<-'),bbox=nodeType)
    plotMidText(parentPt,nodePt,conditionText)



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
绘制树
myTree树,字典格式
parentNode 父节点坐标
textStr指引线文本
'''
def plotTree(myTree,parentNode,textStr):
    leaveNum=getNumLeafs(myTree)#叶子树
    depth=getTreeDepth(myTree)#深度
    rootStr=list(myTree.keys())[0]
    drawAnnotate(rootStr,textStr,parentNode,plotTree.currentNode,False)
    
    secondDict=myTree[rootStr]#{'Y': {'have leg': {'Y': 'Y', 'N': 'N'}}, 'N': 'N'}
    parentNode=(plotTree.currentNode[0],plotTree.currentNode[1])
    plotTree.currentNode=(plotTree.currentNode[0]-80,plotTree.currentNode[1]-40)
    i=1
    for key in secondDict.keys():  
        plotTree.currentNode=(plotTree.currentNode[0]+40,plotTree.currentNode[1])
        i+=1
        if type(secondDict[key]).__name__=='dict':
             #还是树 
             plotTree(secondDict[key],parentNode,key)
        else:
             #叶子节点
             drawAnnotate(secondDict[key],key,parentNode,plotTree.currentNode,True)
        plotTree.currentNode=(parentNode[0]+40*i,parentNode[1]-40)
           
           
           
   
def createPlot(myTree):
    plotTree.leafs=getNumLeafs(myTree)#叶子树
    plotTree.depth=getTreeDepth(myTree)#深度
    plotTree.currentNode=(0,0)#初始化节点位置
    plotTree.XoffSet=0
    plotTree.YoffSet=0
    x1=np.linspace(-40*plotTree.leafs,40*plotTree.leafs,20)
    y1=0*x1
    y2=np.linspace(-40*plotTree.depth,40,20)
    x2=0*y2
    plt.figure()  
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plotTree(myTree,(0,40),'begin')
    plt.show()
    
tree={'surfacing': {'Y': {'have leg': {'Y': 'Y', 'N': 'N'}}, 'N': 'N'}} 
createPlot(tree)
#parentNode=(0,0)
#childNode1=(-40,-30)
#childNode2=(40,-30)
#rootText="根节点"
#drawAnnotate("子节点1",'YY',parentNode,childNode1,False)
#drawAnnotate("子节点2",'NN',parentNode,childNode2,False)

 
# scatter(x, y, s=20, c='b', marker='o', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, hold=None, **kwargs)  
# x,y 画点的坐标可以是单点，也可以是x=[x0,2],y=[y0,5]表示多个点(x0,y0)和(2,5)坐标的散列点  
# s : 缩放，默认缩放20倍 也可以(50,100),表示第一个点缩放50，第二个点缩放100，一次对应设置  
# c 也可以写成 color : 点的颜色，默认是'b'蓝色,也可以写成数组cValue = ['r','y','g','b']，然后设置c=cValue  
# marker : 样式。与plt.plot()的linestyle参数一样，有‘-’、'--'、'o'、'+'等  
# cmap ：color map  
# norm : 数据亮度0.0-1.0，跟c参数有关,没看出什么效果，不太懂，  
# hold : 是否显示其他内容True显示，默认为none显示，Fales不显示，只渲染散点  
# alpha : 这个点的透明度0.0-1.0，0.0表示完全透明，1.0表示完全不透明(默认)  
# linewidths : 设置点的圆环粗细，设置值为0，则远点没有圆环外边框  
 
 
# 创建一个描述  annotate(s, xy, xytext=None, xycoords='data',textcoords='data', arrowprops=None, **kwargs)  
# s : 描述的内容  
# xy : 加描述的点  
# xytext : 标注的位置，xytext=(30,-30),表示从标注点x轴方向上增加30，y轴方向上减30的位置  
# xycoords 、textcoords :这两个参数试了好多次没弄明白，只知道 xycoords='data'给定就行，  
#  textcoords='offset points' 标注的内容从xy设置的点进行偏移xytext  
# textcoords='data' 标注内容为xytext的绝对坐标  
# fontsize : 字体大小，这个没什么好说的  
# arrowstyle : 箭头样式'->'指向标注点 '<-'指向标注内容 还有很多'-'  
            # '->'   head_length=0.4,head_width=0.2  
            # '-['  widthB=1.0,lengthB=0.2,angleB=None  
            # '|-|'     widthA=1.0,widthB=1.0  
            # '-|>'  head_length=0.4,head_width=0.2  
            # '<-'   head_length=0.4,head_width=0.2  
            # '<->'   head_length=0.4,head_width=0.2  
            # '<|-'  head_length=0.4,head_width=0.2  
            # '<|-|>'     head_length=0.4,head_width=0.2  
            # 'fancy'   head_length=0.4,head_width=0.4,tail_width=0.4  
            # 'simple'  head_length=0.5,head_width=0.5,tail_width=0.2  
            # 'wedge'   tail_width=0.3,shrink_factor=0.5  
#plt.annotate(s = r'$2x+1=%s$' % y0, xy=(x0, y0),xytext=(+30,-30), xycoords='data',textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle='<-', connectionstyle="arc3,rad=.2"))  
#drawAnnotate("这个文本",(1,3),(+30,-30),False)
# 直接在图片上添加文字做标注，实际是添加文字  
# (-4,3)坐标处开始输入，输入的内容空格要用\转义，
