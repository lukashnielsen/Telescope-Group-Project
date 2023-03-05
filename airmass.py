import numpy as np
import math
import os
from os import listdir
import shutil

ev=0.13159604333108837
eb=0.2630621547267972

zptv=21.377110325198284
zptb=21.451512566397128

#corrections=np.array([['GHCyg',angle[0]],['V438Cyg',angle[1]],['VXCyg',angle[2]],['VZCyg',angle[3]],['RSCas',angle[4]],['RYCas',angle[5]],['FMCas',angle[6]],['TUCas',angle[7]],['DLCas',angle[8]],['RWCas',angle[9]],['SWCas',angle[10]],['AndromedaCV1',angle[11]]])

corrections=np.array([['GHCyg',9.162778],['V438Cyg',16.1236111],['VXCyg',21.8002778],['VZCyg',29.1969444],['RSCas',49.0569444],['RYCas',48.3511111],['FMCas',49.6072222],['TUCas',49.0644444],['DLCas',50.28],['RWCas',50.2297222],['SWCas',34.3947222]])

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

def makedir(new_dir, parent_dir):
    #path
    path=os.path.join(parent_dir, str(new_dir))

    #Create directory
    os.makedirs(path)

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/")
#get list of dates
datelist=os.listdir()

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/")
"""
for i in datelist:
    makedir(i,"magnitudes new")
"""
def correct(star):
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/")


    for i in datelist:
        if i == '2021-09-29':
            starnum=0
            os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/".format(i))

            stars=os.listdir()

            stars1=os.listdir()

            catlist=getname(stars1)

            Number = []
            #if an element of catlist is the same as the argument of findstar(), append the index of the star to the list Number
            for r in range(len(catlist)):
                if catlist[r]==star:
                    Number.append(r)

            for h in range(len(Number)):

                #opens one of the catalogues using the index found earlier, which we're gonna work with until the point is found
                with open("{}".format(stars[Number[h]])) as f:
                    catalogue=f.read()
                f.close()

                x=[]
                z=[]
                y=0
                for a in range(len(catalogue)):

                    if catalogue[a]=='\'':
                        if catalogue[a+1] !=',' or catalogue[a+1] !=']':
                            num=1
                            while catalogue[a+num] !='\'':
                                if a+num+1==len(catalogue):
                                    break
                                x.append(catalogue[a+num])
                                num+=1
                            z.append(''.join(x[0 : len(x)]))
                            x=[]

                print(catalogue)

                fluxcep=z[2]
                flux1=z[16]
                flux2=z[30]
                flux3=z[44]
                flux4=z[58]
                print(fluxcep,flux1,flux2,flux3,flux4)

                for c in range(len(corrections)):
                    if corrections[c][0]==star:
                        mag0=-2.5*np.log10(float(fluxcep))-ev*1/math.cos(math.radians(float(corrections[c][1])))+zptv
                        mag1=-2.5*np.log10(float(flux1))-ev*1/math.cos(math.radians(float(corrections[c][1])))+zptv
                        mag2=-2.5*np.log10(float(flux2))-ev*1/math.cos(math.radians(float(corrections[c][1])))+zptv
                        mag3=-2.5*np.log10(float(flux3))-ev*1/math.cos(math.radians(float(corrections[c][1])))+zptv
                        mag4=-2.5*np.log10(float(flux4))-ev*1/math.cos(math.radians(float(corrections[c][1])))+zptv

                write=open("{},{} no. {}".format(star,i,starnum), "w")

                write.write(str(mag0))
                write.write("\n")
                write.write(str(mag1))
                write.write("\n")
                write.write(str(mag2))
                write.write("\n")
                write.write(str(mag3))
                write.write("\n")
                write.write(str(mag4))

                write.close()

                original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/{},{} no. {}".format(i,star,i,starnum)
                target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/{}/{},{} no. {}".format(i,star,i,starnum)

                shutil.move(original,target)
                starnum+=1

        if i != '2021-09-29':
            starnum=0
            os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/".format(i))

            stars=os.listdir()

            stars1=os.listdir()

            catlist=getname(stars1)

            Number = []
            #if an element of catlist is the same as the argument of findstar(), append the index of the star to the list Number
            for r in range(len(catlist)):
                if catlist[r]==star:
                    Number.append(r)

            for h in range(len(Number)):

                #opens one of the catalogues using the index found earlier, which we're gonna work with until the point is found
                with open("{}".format(stars[Number[h]])) as f:
                    catalogue=f.read()
                f.close()

                x=[]
                z=[]
                y=0
                for a in range(len(catalogue)):

                    if catalogue[a]=='\'':
                        if catalogue[a+1] !=',' or catalogue[a+1] !=']':
                            num=1
                            while catalogue[a+num] !='\'':
                                if a+num+1==len(catalogue):
                                    break
                                x.append(catalogue[a+num])
                                num+=1
                            z.append(''.join(x[0 : len(x)]))
                            x=[]

                print(catalogue)

                fluxcep=z[2]
                flux1=z[16]
                flux2=z[30]
                flux3=z[44]
                flux4=z[58]
                print(fluxcep,flux1,flux2,flux3,flux4)

                for c in range(len(corrections)):
                    if corrections[c][0]==star:
                        mag0=-2.5*np.log10(float(fluxcep))
                        mag1=-2.5*np.log10(float(flux1))
                        mag2=-2.5*np.log10(float(flux2))
                        mag3=-2.5*np.log10(float(flux3))
                        mag4=-2.5*np.log10(float(flux4))

                write=open("{},{} no. {}".format(star,i,starnum), "w")

                write.write(str(mag0))
                write.write("\n")
                write.write(str(mag1))
                write.write("\n")
                write.write(str(mag2))
                write.write("\n")
                write.write(str(mag3))
                write.write("\n")
                write.write(str(mag4))

                write.close()

                original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/{},{} no. {}".format(i,star,i,starnum)
                target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/{}/{},{} no. {}".format(i,star,i,starnum)

                shutil.move(original,target)

                starnum+=1



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
                    if corrections[c][0]==star:
                        mag0=float(z[0])-ev*float(corrections[c][1])+zptv
                        mag1=float(z[1])-ev*float(corrections[c][1])+zptv
                        mag2=float(z[2])-ev*float(corrections[c][1])+zptv
                        mag3=float(z[3])-ev*float(corrections[c][1])+zptv
                        mag4=float(z[4])-ev*float(corrections[c][1])+zptv


                write=open("{},{} no. {}".format(star,i,starnum), "w")

                write.write(str(mag0))
                write.write("\n")
                write.write(str(mag1))
                write.write("\n")
                write.write(str(mag2))
                write.write("\n")
                write.write(str(mag3))
                write.write("\n")
                write.write(str(mag4))

                write.close()

                original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/{},{} no. {}".format(i,star,i,starnum)
                target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes/{}/{},{} no. {}".format(i,star,i,starnum)

                shutil.move(original,target)

correct('GHCyg')
correct('V438Cyg')
correct('VXCyg')
correct('VZCyg')
correct('RSCas')
correct('RYCas')
correct('FMCas')
correct('TUCas')
correct('DLCas')
correct('RWCas')
correct('SWCas')
