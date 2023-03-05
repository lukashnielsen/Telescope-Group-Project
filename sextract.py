import os
from os import listdir
from os.path import isfile, join
import shutil

"""first we define some useful functions and make some directories"""


#function to make a directory with a parent directory
def makedir(new_dir, parent_dir):
    #path
    path=os.path.join(parent_dir, str(new_dir))

    #Create directory
    os.makedirs(path)

#navigate to Cepheids 2 folder
os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/")

#make source extracted directory, with 3 new directories - Andromeda, Cepheids and Standard Stars
makedir("Andromeda","source-extracted data")
makedir("Cepheids","source-extracted data")
makedir("Standard Stars","source-extracted data")


"""next we make a function to source extract the data from the images and move the data to the appropriate folder in the Source Extracted Data directory"""
def sextract(startype):
    #navigate to folder with all of the reduced data for cepheids
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/ReducedData/{}/".format(startype))

    #list of dates that the measurements were taken to make directories for the source extracted data
    directorylist=os.listdir()
    y=0
    for i in directorylist:
        #navigates first to source extracted data directory to make the different sub directories for each of the stars
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/")
        #makes directory
        makedir(directorylist[y], str(startype))
        #navigates to the ReducedData directory
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/ReducedData/{}/{}/".format(startype, directorylist[y]))
        #lists everything in the reduced data directory
        dirlist=os.listdir()

        x=0
        for i in dirlist:
            if dirlist[x].startswith("PIRATE"):
                #source extractor command line
                cmd='source-extractor ' + str(dirlist[x]) + ' -c default.sex'
                #executes the command in command prompt
                os.system(cmd)

                namelist = dirlist
                namelist[x] = namelist[x].split('.fits')
                #renames test.cat to the star name to help tell apart what the different catalogues are
                fd="test.cat"
                os.rename(fd,str(namelist[x][0])+".cat")

                #moves the data to the directory made previously for the sextracted data
                original = "/storage/teaching/2021-22/tgp/Cepheids2/ReducedData/{}/{}/{}".format(startype, directorylist[y], str(namelist[x][0]+".cat"))
                target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/{}/{}/{}".format(startype, directorylist[y], str(namelist[x][0]+".cat"))

                shutil.move(original,target)

            x+=1
        y+=1
sextract("Andromeda")
sextract("Cepheids")
sextract("Standard Stars")
