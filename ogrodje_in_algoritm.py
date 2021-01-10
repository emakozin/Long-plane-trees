import random
import math
import numpy as np
from numpy import linalg as LA
import matplotlib
import jupyter
from shapely.geometry import Point, Polygon
import sys
sys.setrecursionlimit(10000)


class Graf:
    def __init__(self,tocke=[],n=5):
        self.n = n
        self.tocke=tocke
        if not tocke:
            for i in range(n):
                self.tocke.append(Point(random.random(),random.random()))
        self.dim =len(self.tocke)
        dim=self.dim
        self.Z= np.zeros((dim,dim))
        self.dolžine = np.zeros((dim,dim))
        for i in range(dim):
            for j in range(dim):
                    self.dolžine[i][j]= dist(self.tocke[i],self.tocke[j])

 
class kvadrat:
    def __init__(self,x=1,y=1,n=5):
        self.n = n
        self.x = x 
        self.y = y



def generiraj(kvadrat,n=1):
    ret = []
    for i in range(n):
        ret.append(Graf(kvadrat))
    return ret
    
def alisesekata(graf,a,b,p,q):
    at=graf.tocke[a]
    bt=graf.tocke[b]
    pt=graf.tocke[p]
    qt=graf.tocke[q]
    if at.x == pt.x:
        if bt.x == qt.x:
            return False
        else:
            k2 = (bt.y - qt.y) / (bt.x - qt.x)
            n2 = 1 / 2 * (bt.y + qt.y - k2 * (bt.x + qt.x))
            y = at.x * k2 + n2
            if (y >= min(bt.y, qt.y) and y <= max(bt.y, qt.y)):
                return True
            else:
                return False
    else:
        k1 = (at.y - pt.y) / (at.x - pt.x)
    if bt.x == qt.x:
        n1 = 1 / 2 * (at.y + pt.y - k1 * (at.x + pt.x))
        y = bt.x * k1 + n1
        if (y >= min(at.y, pt.y) and y <= max(at.y, pt.y)):
            return True
        else: return False
    else: k2 = (bt.y - qt.y) / (bt.x - qt.x)
    n1 = 1 / 2 * (at.y + pt.y - k1 * (at.x + pt.x))
    n2 = 1 / 2 * (bt.y + qt.y - k2 * (bt.x + qt.x))
    if (k1 == k2):
        if (n1 == n2):
            if ((max(at.x, pt.x) < min[bt.x,qt.x]) or (min(at.x, pt.x) > max[bt.x,qt.x])):
                return False
            else: return True
        else: return False
    x = (n2 - n1) / (k1 - k2)
    y = k1 * x + n1
    if (x >= min(at.x, pt.x) and x <= max(at.x, pt.x)) and (x >= min(bt.x, qt.x) and x <= max(bt.x, qt.x)) and (y >= min(at.y, pt.y) and y <= max(at.y, pt.y)) and (y >= min(bt.y, qt.y) and y <= max(bt.y, qt.y)):
            return True
    return False


def dist(tocka1,tocka2):
    x= tocka1.y-tocka2.y
    y= tocka1.x-tocka2.x
    r = math.sqrt(x*x + y*y)
    return  r

def listdist(spisek,a,graf):
    vsota=0
    for i in spisek:
        print("spisek",i)
        vsota += graf.dolžine[i][a]
    print("list,dist test",vsota)
    return vsota 

def tocka_daljica(a,b,pqk):
    return abs((pqk.x-b.x)*(b.y-a.y) - (b.x-a.x)*(pqk.y-b.y)) / np.sqrt(np.square(pqk.x-b.x) + np.square(pqk.y-b.y))

def pomožna (graf,a,b,p,q):
    if graf.Z[p][q]>0:
        return graf.Z[p][q]
    if graf.Z[p][q]<0:
        return 0
    k=0
    razdalja_od_ab=0
    trenutna_tocka = 0
    razdp = tocka_daljica(graf.tocke[a],graf.tocke[b],graf.tocke[p])
    razdq = tocka_daljica(graf.tocke[a],graf.tocke[b],graf.tocke[q])
    if razdp==razdq:
        return s
    if razdp > razdq:
        ratio = razdq/razdp
        poly = Polygon([graf.tocke[a],graf.tocke[b],graf.tocke[a]*(1-ratio) + graf.tocke[p]*ratio ,graf.tocke[q]]) 
    if razdp < razdq:
        ratio = razdp/razdq
        poly = Polygon([graf.tocke[a],graf.tocke[b], graf.tocke[p],graf.tocke[b]*(1-ratio) + graf.tocke[q]*ratio])
    else:
        poly = Polygon([graf.tocke[a],graf.tocke[b], graf.tocke[p],graf.tocke[q]])
    for i in range(graf.dim):
        if i not in [a,b,p,q]:
            if graf.tocke[i].within(poly):
                razd =  tocka_daljica(graf.tocke[a],graf.tocke[b],graf.tocke[k])
                if razdalja_od_ab < razd:
                    k=+ (i-k)
                    razdalja_od_ab += razd - razdalja_od_ab
    if k:
        razdk = LA.norm(np.cross(graf.tocke[a]-graf.tocke[b],graf.tocke[b]-graf.tocke[k]))/LA.norm(graf.tocke[a]-graf.tocke[k])
        ratio=razdk/razdp               
        levit=Polygon(([graf.tocke[a],graf.tocke[k],graf.tocke[a]*(1-ratio) + graf.tocke[p]*ratio])) 
        ratio=razdk/razdq               
        desnit=Polygon(([graf.tocke[b],graf.tocke[k],graf.tocke[b]*(1-ratio) + graf.tocke[q]*ratio]))
        levilist=[]
        desnilist=[]
        for i in range(graf.dim):
            if i not in [a,b,p,q,k]:
                if graf.tocke[i].within(levit):
                    levilist.append(i)
                if graf.tocke[i].within(desnit):
                    desnilist.append(i)
        if graf.Z[k][q]>0:
            g1= graf.Z[k][q]
        elif graf.Z[k][q]<0:
            g1= 0
        else:
            g1 = pomožna(graf,a,b,k,q)
        if graf.Z[p][k]>0:
            g2 = graf.Z[p][k]
        elif graf.Z[p][k]<0:
            g2 = 0
        else:
            g2 = pomožna(graf,a,b,p,k)
        g= max(g1+listdist(levilist,a,graf)  , g2 +listdist(desnilist,b,graf) )
        graf.Z[p][q]=g
        return g
    else:
        graf.Z[p][q]=-1
        return 0

    
def pomožna_B (graf,a,b):
    print("a======================================================!")
    if graf.dim ==2:
        print("to je maks",0)
        return 0
    if graf.dim ==3:
        print("jaja")
        return max(dist(graf.tocke[1],graf.tocke[2]),(dist(graf.tocke[0],graf.tocke[2])))
    for i in range(graf.dim):
        print("i",i)
        for j in range (i+1,graf.dim):
            print("j:",j)
            if j not in [a,b] and i not in [a,b]:
                if  (not alisesekata(graf,a,b,i,j)) :
                    print(i,j)
                    if graf.Z[i][j] == 0 :
                        print("_____________________",a,b,i,j)
                        pomožna(graf,a,b,i,j)
                if not alisesekata(graf,a,b,j,i):
                    if graf.Z[j][i] == 0:
                        print(a,b,j,i)
                        pomožna(graf,a,b,j,i)
    maks=0
    for i in graf.Z:
        for j in i:
            if j>maks:
                maks = j
    print(graf.Z)
    print("to je maks",maks)
    return maks


def algo(graf):
    maksa=0
    for a in range(graf.dim):
        for b in range (a+1,graf.dim):
            spisek1=[graf.tocke[a],graf.tocke[b]]
            spisek2=[graf.tocke[a],graf.tocke[b]]
            #razdelimo graf na del pod in nad èrto saj sta to pravzaprav loèena primera
            for i in graf.tocke:
                if 0>(i.x-graf.tocke[a].x)*(graf.tocke[b].y-graf.tocke[a].y) - (i.y-graf.tocke[a].y)*(graf.tocke[b].x-graf.tocke[a].x):
                    spisek1.append(i)
                if 0<(i.x-graf.tocke[a].x)*(graf.tocke[b].y-graf.tocke[a].y) - (i.y-graf.tocke[a].y)*(graf.tocke[b].x-graf.tocke[a].x):
                    spisek2.append(i)
            graf1=Graf(spisek1)
            graf2=Graf(spisek2)
            vred=pomožna_B(graf1,0,1)+pomožna_B(graf2,0,1)
            if dist(graf.tocke[a],graf.tocke[b])+vred > maksa:
                SH_A = a
                SH_B = b
                maksa= vred + dist(graf.tocke[a],graf.tocke[b])
    return maksa
                
                    
print(1)
grafek=Graf(n=100)
print(1)
c=algo(grafek)
print(1)
print("done" ,c)
     
    
