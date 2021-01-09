import random
import math
import numpy as np
import matplotlib
import jupyter

class mreža:
    def __init__(self,kvadrat):
        self.tocke=[]
        for i in range(kvadrat.n):
            self.tocke.append([random.random()*kvadrat.x,random.random()*kvadrat.y])
        
 
class kvadrat:
    def __init__(self,x=1,y=1,n=5):
        self.n=n
        self.x=x
        self.y=y



def generiraj(kvadrat,n=1):
    ret = []
    for i in range(n):
        ret.append(mreža(kvadrat))
    return ret
    



def dist(tocka1,tocka2):
    x= tocka1[1]-tocka2[1]
    y= tocka1[0]-tocka2[0]
    r = math.sqrt(x*x + y*y)
    return  r

class graf:
    def __init__(self,mreza):
        self.dim =len(mreza.tocke)
        dim=self.dim
        self.graf= np.zeros((dim,dim))
        print(self.graf)
        self.dolzine = np.zeros((dim,dim))
        for i in range(len(mreza.tocke)):
            for j in range(len(mreza.tocke)):
                if i < j:
                    self.dolzine[i][j]= dist(mreza.tocke[i],mreza.tocke[j])
                    print(i,j)
    def razpon(self)
        ret = 0
        for i in range(self.dim):
            for j in range(i,self.dim):
                if  self.graf[i][j]:
                    ret += self.dolzine[i][j]
        return ret
    
kvadrat=kvadrat()
mreža=mreža(kvadrat)
graf=graf(mreža)
graf.dolzine
    
