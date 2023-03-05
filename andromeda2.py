import numpy as np
import math
import os
from os import listdir
import shutil

with open('andromeda1.txt','r') as f:
    lines=f.readlines()

f.close()

list=[]
for i in lines:
    list.append(i.split())

def calcy(angle,minutes,seconds):
    if float(minutes) - 18. < 0:
        no1=abs(float(angle)-29.)
        no2=abs(60.-(18-float(minutes)))
    else:
        no1=abs(float(angle)-28.)
        no2=abs(float(minutes)-18.)
    no2/=60
    no3=abs(float(seconds)-00.)
    no3/=60*60
    no4=no1+no2+no3
    return no4

xyangle=np.zeros((1,2))
xyangle[0][0]=calcy(list[0][5],list[0][6],list[0][7])

time=np.array([22,24,29])

for i in range(len(time)):
    if time[2]-43<0:
        if time[1]-53<0:
            time[0]-=1
            time[1]=60-(53-time[1])
            time[2]=60-(43-time[2])
        else:
            time[1]-=1
            time[2]=60-(43-time[2])
    elif time[1]-53<0:
        time[0]-=1
        time[1]=60-(53-time[1])
        time[2]-=43
    else:
        time[1]-=53
        time[2]-=43


#convert to degrees, and by degrees i mean get the decimal point so it all works together
def calcx(hours,minutes,seconds,hours1,minutes1,seconds1):
    if float(hours1)<5.:
        degree1=(float(hours)+float(minutes)/60.+float(seconds)/3600.)*15.
        degree2=(float(hours1)+24+float(minutes1)/60.+float(seconds1)/3600.)*15.
    else:
        degree1=(float(hours)+float(minutes)/60.+float(seconds)/3600.)*15.
        degree2=(float(hours1)+float(minutes1)/60.+float(seconds1)/3600.)*15.
    no4=degree2-degree1
    return no4

xyangle[0][1]=calcx(time[0],time[1],time[2],list[0][2],list[0][3],list[0][4])

angle=[]
angle.append(1/np.cos(math.radians(np.sqrt(xyangle[0][0]**2+xyangle[0][1]**2))))
print(angle)
ev=0.13159604333108837
eb=0.2630621547267972

zptv=21.377110325198284
zptb=21.451512566397128

corrections=np.array(['AndromedaCV1',angle[0]])

def getname(starlist):
    nlist=[]
    y=0
    #gets the list 'starlist' and slices of the first 28 characters, which is PIRATE_413415_OSL_ROE_Ceph2_, leaving just the name of the cepheid and everything after
    #then splits the name from all of the '_'
    #this means that the first value in the array is the cepheid name
    for i in starlist:
        starlist[y]=starlist[y][28:]
        starlist[y]=starlist[y].split("_")
        nlist.append(starlist[y][0])
        y+=1
    #nlist is the list of the star names
    return nlist


os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/")
#get list of dates
filtlist=os.listdir()

def correct():


    for i in filtlist:
        starnum=0
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/{}/".format(i))

        stars=os.listdir()

        for h in range(2):
            if i=='V':
                #opens one of the catalogues using the index found earlier, which we're gonna work with until the point is found
                with open("{}".format(stars[h])) as f:
                    catalogue=f.read()
                f.close()

                x=[]
                z=[]
                y=0
                for c in catalogue:
                    if c=='-':
                        if catalogue[y+1]!='1':
                            x.append(c)
                            x.append(catalogue[y+1])
                            x.append(catalogue[y+2])
                            x.append(catalogue[y+3])
                            x.append(catalogue[y+4])
                            x.append(catalogue[y+5])
                            x.append(catalogue[y+6])
                            z.append(''.join(x[0 : 7]))

                            x=[]
                        else:
                            x.append(c)
                            x.append(catalogue[y+1])
                            x.append(catalogue[y+2])
                            x.append(catalogue[y+3])
                            x.append(catalogue[y+4])
                            x.append(catalogue[y+5])
                            x.append(catalogue[y+6])
                            x.append(catalogue[y+7])
                            z.append(''.join(x[0 : 8]))
                            x=[]
                    y+=1

                for c in range(len(corrections)):
                    mag0=float(z[0])-ev*float(corrections[1])+zptv
                    mag1=float(z[1])-ev*float(corrections[1])+zptv
                    mag2=float(z[2])-ev*float(corrections[1])+zptv
                    mag3=float(z[3])-ev*float(corrections[1])+zptv

            elif i=='B':
                #opens one of the catalogues using the index found earlier, which we're gonna work with until the point is found
                with open("{}".format(stars[h])) as f:
                    catalogue=f.read()
                f.close()

                x=[]
                z=[]
                y=0
                for c in catalogue:
                    if c=='-':
                        if catalogue[y+1]!='1':
                            x.append(c)
                            x.append(catalogue[y+1])
                            x.append(catalogue[y+2])
                            x.append(catalogue[y+3])
                            x.append(catalogue[y+4])
                            x.append(catalogue[y+5])
                            x.append(catalogue[y+6])
                            z.append(''.join(x[0 : 7]))

                            x=[]
                        else:
                            x.append(c)
                            x.append(catalogue[y+1])
                            x.append(catalogue[y+2])
                            x.append(catalogue[y+3])
                            x.append(catalogue[y+4])
                            x.append(catalogue[y+5])
                            x.append(catalogue[y+6])
                            x.append(catalogue[y+7])
                            z.append(''.join(x[0 : 8]))
                            x=[]
                    y+=1

                for c in range(len(corrections)):
                    mag0=float(z[0])-eb*float(corrections[1])+zptb
                    mag1=float(z[1])-eb*float(corrections[1])+zptb
                    mag2=float(z[2])-eb*float(corrections[1])+zptb
                    mag3=float(z[3])-eb*float(corrections[1])+zptb

            write=open("{},{}".format(stars[h],i),"w")

            write.write(str(mag0))
            write.write("\n")
            write.write(str(mag1))
            write.write("\n")
            write.write(str(mag2))
            write.write("\n")
            write.write(str(mag3))

            write.close()

            original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/{}/{},{}".format(i,stars[h],i)
            target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes/Andromeda/{}/{},{}".format(i,stars[h],i)

            shutil.move(original,target)
            starnum+=1

correct()
