import shutil
import os
from os import listdir
import numpy as np

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/")

datelist=os.listdir()

stars=['GHCyg','V438Cyg','VXCyg','VZCyg','RSCas','RYCas','FMCas','TUCas','DLCas','RWCas','SWCas']

def makedir(new_dir, parent_dir):
    #path
    path=os.path.join(parent_dir, str(new_dir))

    #Create directory
    os.makedirs(path)

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/")
"""
for i in datelist:
    makedir(i,"Final new")
"""
def correct(star):
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/2021-09-29/")
    starlist=os.listdir()

    number=0
    for j in starlist:
        if j[:4]==star[:4]:
            number+=1

    starnum=0
    avarray=np.zeros((4,number))
    a=np.zeros(4)
    for j in starlist:
        if j[:4]==star[:4]:
            with open('{},{} no. {}'.format(star,'2021-09-29',starnum),'r') as f:
                lines=f.readlines()
            avarray[0][starnum]=lines[1]
            avarray[1][starnum]=lines[2]
            avarray[2][starnum]=lines[3]
            avarray[3][starnum]=lines[4]
            f.close()
            starnum+=1

    #for j in range(4):
    #    print(avarray[j],'is avarray j')
    #    avarray[j]=10**(avarray[j]/(-2.5))

    for j in range(4):
        a[j]=np.mean(avarray[j])

    for i in datelist:
        if i!='2021-09-29':
            os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/{}/".format(i))
            starlist=os.listdir()

            number=0
            for j in starlist:
                if j[:4]==star[:4]:
                    number+=1

            starnum=0
            avarray=np.zeros((5,number))

            for j in starlist:
                if j[:4]==star[:4]:
                    with open('{},{} no. {}'.format(star,i,starnum),'r') as f:
                        lines=f.readlines()
                    avarray[0][starnum]=lines[0]
                    avarray[1][starnum]=lines[1]
                    avarray[2][starnum]=lines[2]
                    avarray[3][starnum]=lines[3]
                    avarray[4][starnum]=lines[4]
                    f.close()
                    starnum+=1

            b=np.zeros(4)
            for j in range(4):
                b[j]=np.mean(avarray[j+1])

            #print(i)
            c=a-b
            print('corrected means from standard night is')
            print(a)
            print('uncorrected means are')
            print(b)
            print('new mean values are')
            print(c)
            mean=np.mean(c)
            #print('mean is',mean)
            #print('read in values are')
            #print(avarray)
            #print('new cepheid is')
            d=[]
            for j in range(starnum):
                #print(avarray[0][j]+mean)
                d.append(avarray[0][j]+mean)

            meanceph=np.mean(d)
            stdceph=np.std(d)

            write=open("{} {}".format(star,i), "w")

            write.write(str(meanceph))
            write.write("\n")
            write.write(str(stdceph))
            write.close()

            original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/{}/{} {}".format(i,star,i)
            target = "/storage/teaching/2021-22/tgp/Cepheids2/Final new/{}/{} {}".format(i,star,i)

            shutil.move(original,target)

        if i == '2021-09-29':
            os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/{}/".format(i))

            starlist=os.listdir()

            number=0
            for j in starlist:
                if j[:4]==star[:4]:
                    number+=1

            starnum=0
            avarray=np.zeros(number)


            for j in starlist:
                if j[:4]==star[:4]:
                    with open('{},{} no. {}'.format(star,'2021-09-29',starnum),'r') as f:
                        lines=f.readlines()
                    avarray[starnum]=lines[0]
                    f.close()
                    starnum+=1

            meanceph=np.mean(avarray)
            stdceph=np.std(avarray)

            write=open("{} {}".format(star,i), "w")

            write.write(str(meanceph))
            write.write("\n")
            write.write(str(stdceph))
            write.close()

            original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes new/{}/{} {}".format(i,star,i)
            target = "/storage/teaching/2021-22/tgp/Cepheids2/Final new/{}/{} {}".format(i,star,i)

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
