import random
import math
import numpy as np
from numpy import linalg as LA
import matplotlib
import jupyter
from shapely.geometry import Point, Polygon
import sys
sys.setrecursionlimit(1000)
cifre=[0,1,2,3,4,5,6,7,8,9]
#razred kjer bomo generirali točke beleži tudi vrednosti Z(p,q) da se izognemo rekurziji
class Graf:
    def __init__(self,tocke=[],n=5):
        self.n = n
        self.tocke=tocke
        if not tocke:
            i = n
            while i != 0:
                a = random.choice(cifre)
                b = random.choice(cifre)
                c = random.choice(cifre)
                d = random.choice(cifre)
                e = random.choice(cifre)
                f = random.choice(cifre)
                x = a*1/10 + b * 1/100 + c*1/1000
                y = d*1/10 + e * 1/100 + f*1/1000
                tocka = Point(x,y)
                if tocka not in self.tocke:
                    self.tocke.append(tocka)
                    i = i - 1
        self.dim =len(self.tocke)
        dim=self.dim
        self.Z= np.zeros((dim,dim))
        self.dolžine = np.zeros((dim,dim))
        for i in range(dim):
            for j in range(dim):
                    self.dolžine[i][j]= dist(self.tocke[i],self.tocke[j])



#class kvadrat:
#    def __init__(self,x=1,y=1,n=5):
#        self.n = n
#        self.x = x 
#        self.y = y



#def generiraj(kvadrat,n=1):
 #   ret = []
 #   for i in range(n):
 #       ret.append(Graf(kvadrat))
 #   return ret
    
#funkcija ki preveri ali se daljici sekata
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

# evklidska razdalja
def dist(tocka1,tocka2):
    x= tocka1.y-tocka2.y
    y= tocka1.x-tocka2.x
    r = math.sqrt(x*x + y*y)
    return  r

# razdalja poti med točkami iz spiska in točko a
def listdist(spisek,a,graf):
    vsota=0
    for i in spisek:
        vsota += graf.dolžine[i][a]
    return vsota 

#razdalja med  točko in daljico
def tocka_daljica(a,b,pqk):
    grr=abs((pqk.x-b.x)*(b.y-a.y) - (b.x-a.x)*(pqk.y-b.y)) / np.sqrt(np.square(pqk.x-b.x) + np.square(pqk.y-b.y))
    return grr


#osnova algoritma 
def pomožna (graf,a,b,p,q,ne=0):
    razdne=10
    #preverimo če smo iskano vrednost že poračunali
    if p==q:
        return error
    if graf.Z[p][q]>0:
        return graf.Z[p][q]
    if graf.Z[p][q]<0:
        return 0
    k=0
    razdalja_od_ab=0
    trenutna_tocka = 0
    #Izračunamo odaljenost p in q od daljice a-b da lahko poiščemo štirikotnik Q(p,q)
    if ne:
        razdne=tocka_daljica(graf.tocke[a],graf.tocke[ne],graf.tocke[b])
    razdp = tocka_daljica(graf.tocke[a],graf.tocke[p],graf.tocke[b])
    razdq = tocka_daljica(graf.tocke[a],graf.tocke[q],graf.tocke[b])
    if razdp==razdq:
        return error
    if razdp > razdq:
        ratio = razdq/razdp
        tocka = Point(graf.tocke[a].x*(1-ratio)+graf.tocke[p].x*ratio,graf.tocke[a].y*(1-ratio)+graf.tocke[p].y*ratio)
        poly = Polygon([graf.tocke[a],graf.tocke[b],tocka,graf.tocke[q]]) 
    elif razdp < razdq:
        ratio = razdp/razdq
        tocka= Point(graf.tocke[b].x*(1-ratio) + graf.tocke[q].x*ratio,graf.tocke[b].y*(1-ratio) + graf.tocke[q].y*ratio)
        poly = Polygon([graf.tocke[a],graf.tocke[b], graf.tocke[p],tocka])
    else:
        poly = Polygon([graf.tocke[a],graf.tocke[b], graf.tocke[p],graf.tocke[q]])
    #za vse točke preverimo če se nahajajo v štirikotniku
    for i in range(graf.dim):
        if i not in [a,b,p,q,ne]:
            if graf.tocke[i].within(poly):
                #vzamemo najbolj odaljeno
                razd =  tocka_daljica(graf.tocke[a],graf.tocke[i],graf.tocke[b])
                if razdalja_od_ab < razd:
                    if razd <  razdp:
                         if razd< razdq:
                            if razd<razdne:
                                k= i
                                razdalja_od_ab = razd
    #če smo našli kako točko v pravokotniku zažanemo krog rekurzije z najbolj odaljeno med njimi
    if k:
        #pogledamo če je v levem in desnem trikotniku kakšna točka, ki povežemo z ustrezno točko (a ali b)
        razdk = tocka_daljica(graf.tocke[a],graf.tocke[k],graf.tocke[b])
        bočka= Point(graf.tocke[a].x*(1-ratio) + graf.tocke[p].x*ratio,graf.tocke[a].y*(1-ratio) + graf.tocke[p].y*ratio)             
        levit=Polygon(([graf.tocke[a],graf.tocke[k],bočka])) 
        ratio=razdk/razdq 
        nočka=Point(graf.tocke[b].x*(1-ratio) + graf.tocke[q].x*ratio, graf.tocke[b].y*(1-ratio) + graf.tocke[q].y*ratio)           
        desnit=Polygon(([graf.tocke[b],graf.tocke[k],nočka]))
        levilist=[]
        desnilist=[k]
        for i in range(graf.dim):
            if i not in [a,b,p,q,k,ne]:
                if graf.tocke[i].within(levit):
                    levilist.append(i)
                if graf.tocke[i].within(desnit):
                    desnilist.append(i)
        if graf.Z[k][q]>0:
            g1= graf.Z[k][q]
        elif graf.Z[k][q]<0:
            g1= 0
        else:
            g1 = pomožna(graf,a,b,k,q,ne=p)
        if graf.Z[p][k]>0:
            g2 = graf.Z[p][k]
        elif graf.Z[p][k]<0:
            g2 = 0
        else:
            g2 = pomožna(graf,a,b,p,k,ne=q)
        #po algoritmu poiščemo maksimum
        g= max(g1+listdist(levilist,a,graf),g2 +listdist(desnilist,b,graf) )
        g += listdist([p],a,graf)
        g += listdist([q],b,graf)
        graf.Z[p][q]=g
        return g
    #če v pravokotniku ni točk se veriga konča
    else:
        graf.Z[p][q]=listdist([q],b,graf) + listdist([p],a,graf)
        return listdist([q],b,graf) + listdist([p],a,graf)

    
def pomožna_B (graf,a,b):
    #po izreku poiščemo za fiksen a,b največji dvozvezdni graf kjer tečemo po vseh p in q
    if graf.dim ==2:
        return 0
    if graf.dim ==3:
        return max(dist(graf.tocke[1],graf.tocke[2]),(dist(graf.tocke[0],graf.tocke[2])))
    for i in range(graf.dim):
        for j in range (graf.dim):
            if j not in [a,b] and i not in [a,b] and i!=j:
                if  (not alisesekata(graf,a,b,i,j)) :
                    if graf.Z[i][j] == 0 :
                        graf.Z[i][j]=pomožna(graf,a,b,i,j)
                if not alisesekata(graf,a,b,j,i):
                    if graf.Z[j][i] == 0:
                        graf.Z[j][i]=pomožna(graf,a,b,j,i)
    maks=0
    for i in graf.Z:
        for j in i:
            if j>maks:
                maks = j
    return maks

#sedaj tečemo še po vseh možnih a in b 
def algo(graf):
    maksa=0
    for a in range(graf.dim):
        for b in range (a+1,graf.dim):
            spisek1=[graf.tocke[a],graf.tocke[b]]
            spisek2=[graf.tocke[a],graf.tocke[b]]
            #razdelimo graf na del pod in nad črto saj sta to pravzaprav ločena primera
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

#še algoritem za eno zvezdo 
def algo1(graf):
    maksa=0
    for a in range(graf.dim):
        spisek=[]
        for ou in range(graf.dim):
            if a != ou:
                spisek.append(ou)
        if maksa < listdist(spisek,a,graf):
            maksa=listdist(spisek,a,graf)
    return maksa


grafek=Graf(n=10)
c=algo(grafek)
d=algo1(grafek)

print("rešeno",c,d)
