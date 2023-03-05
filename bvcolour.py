import os
import numpy as np
import shutil

#finds b-v colour of comparison stars on 29th october and converts their magnitudes to g band
#then gets counts of all g comparison stars and using m=-2.5(log(C))+zpt gets zpt=m+2.5(log(C))
#corrects cepheid with zpt, then converts cepheid to v band

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes/Andromeda/B/")

with open("stacked29-09-21.txt",'r') as f:
    linesB=f.readlines()

barray=np.zeros(4)
for i in range(4):
    barray[i]=linesB[i]

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes/Andromeda/V/")

with open("stacked29-09-21.txt",'r') as f:
    linesV=f.readlines()

varray=np.zeros(4)
for i in range(4):
    varray[i]=linesV[i]

bvcolour=barray-varray

g = varray + 0.60*bvcolour - 0.12

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/LTprov/")

stars=os.listdir()

maglist=[]
datelist=[]

for i in stars:
    with open(i,'r') as f:
        lines=f.readlines()
    comparison=lines[1:5]

    print(i)
    f.close()

    x=[]
    z=[]

    for c in comparison:
        for a in c:
            if a==',':
                num=3
                while c[c.index(a)+num] !='\'':
                    x.append(c[c.index(a)+num])
                    num+=1
                z.append(''.join(x[0 : len(x)]))
                x=[]

    com=np.zeros(4)
    fake=3
    num1=0
    for c in z:
        if c != fake:
            com[num1]=c
            fake=c
            num1+=1
        if num1==4:
            break

    zpt=g+2.5*np.log10(com)

    meanzpt=np.mean(zpt)

    cepheid=lines[0]

    xcep=[]
    zcep=[]

    for c in cepheid:
        if c==',':
            num=3
            while cepheid[cepheid.index(c)+num] !='\'':
                xcep.append(cepheid[cepheid.index(c)+num])
                num+=1
            zcep.append(''.join(xcep[0 : len(xcep)]))
            xcep=[]

    magcep=zcep[0]
    mag=-2.5*np.log10(float(magcep))+meanzpt

    if np.isnan(mag)==False:
        maglist.append(mag)
        datelist.append(i[4:12])


index=np.zeros((len(datelist),3))

for i in range(3):
    for j in range(len(datelist)):
        index[j,i]=69

num1=0
for i in datelist:
    num=0
    tempnumlist=[]
    for j in datelist:
        if i==j:
            tempnumlist.append(num)
        num+=1
    for k in range(len(tempnumlist)):
        index[num1][k]=tempnumlist[k]
    num1+=1


for j in range(len(datelist)):
    listmag=[]
    listdate=[]
    for i in range(3):
        if index[j,i]!=69:
            listdate.append(datelist[int(index[j,i])])
            listmag.append(maglist[int(index[j,i])])

    meanmagnitude=np.mean(listmag)
    std=np.std(listmag)
    meandate=listdate[0]
    v = meanmagnitude - 0.60 + 0.12

    write=open("{}.txt".format(meandate),"w")
    write.write(str(v))
    write.write("\n")
    write.write(str(std))
    write.close()

    original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/LT/{}.txt".format(meandate)
    target = "/storage/teaching/2021-22/tgp/Cepheids2/Final/Andromeda/{}".format(meandate)
