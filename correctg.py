import shutil
import os
from os import listdir
import numpy as np

def correct():
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes/Andromeda/V/")
    star=os.listdir()

    avarray=np.zeros(4)
    with open('stacked29-09-21.txt','r') as f:
        lines=f.readlines()
    avarray[0]=lines[0]
    avarray[1]=lines[1]
    avarray[2]=lines[2]
    avarray[3]=lines[3]
    f.close()

    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/gband corrected/")
    starlist=os.listdir()
    array=np.zeros(5)
    correct=np.zeros(4)
    for i in starlist:
        with open(i,'r') as f:
            lines=f.readlines()
        array[1]=lines[1]
        array[2]=lines[2]
        array[3]=lines[3]
        array[4]=lines[4]

        correct[0]=avarray[0]-array[1]
        correct[1]=avarray[1]-array[2]
        correct[2]=avarray[2]-array[3]
        correct[3]=avarray[3]-array[4]

        mean=np.mean(correct)
        std=np.std(correct)

        cepheid=array[0]+mean

        write=open("{} ave".format(i),"w")

        write.write(str(cepheid))
        write.write("\n")
        write.write(str(std))

        write.close()

        original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/gband corrected/{} ave".format(i)
        target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/magnitudes/Andromeda/LT/{} ave".format(i)

        shutil.move(original,target)


correct()
