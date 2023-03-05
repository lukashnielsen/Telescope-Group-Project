import os
import shutil

os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/LT/")

list=os.listdir()

B=25.55125007
V=25.51350669


z=[]
for i in list:
    with open(i,'r') as f:
        catalogue=f.readlines()
        print(catalogue)
    x=[]
    z=[]
    #get a index in c, if c[index(a)+1]!=1
    for c in catalogue:
        for a in c:
            print(a)
            if a=='-':
                if c[c.index(a)+1]!='1':
                    x.append(a)
                    x.append(c[c.index(a)+1])
                    x.append(c[c.index(a)+2])
                    x.append(c[c.index(a)+3])
                    x.append(c[c.index(a)+4])
                    x.append(c[c.index(a)+5])
                    x.append(c[c.index(a)+6])
                    z.append(''.join(x[0 : 7]))

                    x=[]
                else:
                    x.append(a)
                    x.append(c[c.index(a)+1])
                    x.append(c[c.index(a)+2])
                    x.append(c[c.index(a)+3])
                    x.append(c[c.index(a)+4])
                    x.append(c[c.index(a)+5])
                    x.append(c[c.index(a)+6])
                    x.append(c[c.index(a)+7])
                    z.append(''.join(x[0 : 8]))
                    x=[]
    for d in range(1):
        v0 = float(z[0]) + 0.12 - 0.6*(B-V)
        v1 = float(z[1]) + 0.12 - 0.6*(B-V)
        v2 = float(z[2]) + 0.12 - 0.6*(B-V)
        v3 = float(z[3]) + 0.12 - 0.6*(B-V)
        v4 = float(z[4]) + 0.12 - 0.6*(B-V)

    write=open("{} gband corrected".format(i),"w")

    write.write(str(v0))
    write.write("\n")
    write.write(str(v1))
    write.write("\n")
    write.write(str(v2))
    write.write("\n")
    write.write(str(v3))
    write.write("\n")
    write.write(str(v4))

    write.close()
