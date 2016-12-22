#encoding:utf-8


_=float('inf')

def dijkstra(BandWidth, l, n):
    k=n
    bdw=[0]*l
    flag=[True]*l
    pre=[n]*l
    flag[n]=False
    for i in xrange(l):
        bdw[i]=BandWidth[k][i]
    for j in xrange(l-1):
        judge=_
        for i in xrange(l):
            if bdw[i]<judge and flag[i]:
                judge=bdw[i]
                k=i
        if k==n:
            return
        flag[k]=False
        for i in xrange(l):
            if bdw[i]>bdw[k]+BandWidth[k][i]:
                bdw[i]=bdw[k]+BandWidth[k][i]
                pre[i]=k
    return pre

def searchpath(per, d, s):
    k=d
    path=[]
    path.append(d+1)
    while per[k]!=s:
        path.insert(0, per[k]+1)
        k=per[k]
    path.insert(0, s+1)
    return path

#BandWidt里写带宽时延
BandWidth=[[  0,150,  _,  _,  _,  _,  _,  _],
           [150,  0,160,  _,155,  _,  _,200],
           [  _,160,  0,167,123,  _,  _,  _],
           [  _,  _,167,  0,  _,198,  _,  _],
           [  _,155,123,  _,  0,184,172,  _],
           [  _,  _,  _,198,184,  0,  _,  _],
           [  _,  _,  _,  _,172,  _,  0,145],
           [  _,200,  _,  _,  _,  _,145,  0]]
l=len(BandWidth)
n=4#源交换机
m=2#目的交换机
per=dijkstra(BandWidth, l, n-1)
path=searchpath(per, m-1, n-1)
print path