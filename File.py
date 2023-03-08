from json import tool
from random import randint


def tootajad(toolised:list,sunniaasta:list):
    end=""
    while True:
        end=input("end?: ")
        if end=="end":
            break
        else:
            nimi=input("sisestage tootaja nimi: ")
            toolised.append(nimi)
            aeg=int(input("tootaja sunniaasta: "))
            sunniaasta.append(aeg)
    return toolised,sunniaasta

def pension(toolised:list,sunniaasta:list):
    pen=[]
    x=len(sunniaasta)
    for ind in range(1,x):
        r=sunniaasta[ind]
        if r >= 1958:
            nik=toolised[ind]
            pen.append(nik)
        else:
            pass
    return pen

def avg(sunniaasta:list):
    sred = sum(sunniaasta) / len(sunniaasta)
    sred=round(sred)
    return sred 

def sort(toolised:list,sunniaasta:list):
    s=int(input("top X. X = "))
    s+=1
    v=int(input("1-kahaneb; 2-kasvab: "))
    if v == 1:
        aeg=[]
        n=len(sunniaasta)
        for j in range(0, n-1):
            for k in range(j+1, n):
                if sunniaasta[j] < sunniaasta[k]:
                    a=sunniaasta[j]
                    sunniaasta[j]=sunniaasta[k]
                    sunniaasta[k]=a

                    a=toolised[j]
                    toolised[j]=toolised[k]
                    toolised[k]=a
        for i in range(1, s):
            s=toolised[i]
            aeg.append(s)
    elif v == 2:
        aeg=[]
        n=len(sunniaasta)
        for j in range(0, n-1):
            for k in range(j+1, n):
                if sunniaasta[j] > sunniaasta[k]:
                    a=sunniaasta[j]
                    sunniaasta[j]=sunniaasta[k]
                    sunniaasta[k]=a

                    a=toolised[j]
                    toolised[j]=toolised[k]
                    toolised[k]=a
        for i in range(1, s):
            s=toolised[i]
            aeg.append(s)
    return aeg 

def nimi(toolised:list,sunniaasta:list):
    sss=[]
    aaa=int(input("tootaja sunniaasta: "))
    x=len(sunniaasta)
    for i in range(1,x):
        if sunniaasta[i]==aaa:
            sss.append(toolised[i])
    return sss

def random(toolised:list,sunniaasta:list):
    l=len(toolised)
    r=randint(0,l-1)
    t=toolised[r]
    s=sunniaasta[r]
    return t,s