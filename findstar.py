import os
from os import listdir
import pandas as pd
import numpy as np
import shutil

#make the directory function
def makedir(new_dir, parent_dir):
    #path
    path=os.path.join(parent_dir, str(new_dir))

    #Create directory
    os.makedirs(path)

#navigate to Cepheids 2 folder
os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/")
#get list of dates
datelist=os.listdir()

#change directory to source-extracted data
os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/")

#makes directories for all the dates, with a parent directory "shortened data" in source-extracted data
"""
for i in datelist:
    makedir(i,"Shortened Data")
"""
#excel data for rough positions of cepheids and stars
data = pd.read_excel (r'/storage/teaching/2021-22/tgp/Cepheids2/comparison stars/Comparison Stars - GAIA coordinates.xlsx',sheet_name=0)

#excel data for rough positions of stars and cepheids that have the image flipped 180 degrees
data180 = pd.read_excel (r'/storage/teaching/2021-22/tgp/Cepheids2/comparison stars/Comparison Stars - GAIA coordinates.xlsx',sheet_name=1)

#function to call on the specific catalogue which the x and y coordinates of the cepheids and comparison stars were taken from and put into the excel file
#the function takes the argument , which is the cepheid, and returns the catalogue used

def return_sdata(star):
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/2021-09-29/")
        if star == 'GHCyg':
            return "PIRATE_413327_OSL_ROE_Ceph2_GHCyg_00_GHCyg_00_Filter_V_00_2021_09_29_19_48_20.cat"
        if star == 'V438Cyg':
            return "PIRATE_413333_OSL_ROE_Ceph2_V438Cyg_00_V438Cyg_00_Filter_V_00_2021_09_29_19_55_52.cat"
        if star == 'VXCyg':
            return "PIRATE_413338_OSL_ROE_Ceph1_VXCyg_00_VXCyg_00_Filter_V_00_2021_09_29_19_59_51.cat"
        if star == 'VZCyg':
            return "PIRATE_413354_OSL_ROE_Ceph2_VZCyg_00_VZCyg_00_Filter_V_00_2021_09_29_20_18_02.cat"
        if star == 'RSCas':
            return "PIRATE_413361_OSL_ROE_Ceph2_RSCas_00_RSCas_00_Filter_V_00_2021_09_29_20_30_02.cat"
        if star == 'RYCas':
            return "PIRATE_413368_OSL_ROE_Ceph2_RYCas_00_RYCas_00_Filter_V_00_2021_09_29_20_42_14.cat"
        if star == 'FMCas':
            return "PIRATE_413376_OSL_ROE_Ceph2_FMCas_00_FMCas_00_Filter_V_00_2021_09_29_20_51_24.cat"
        if star == 'TUCas':
            return "PIRATE_413385_OSL_ROE_Ceph2_TUCas_00_TUCas_00_Filter_V_00_2021_09_29_21_02_58.cat"
        if star == 'DLCas':
            return "PIRATE_413391_OSL_ROE_Ceph2_DLCas_00_DLCas_00_Filter_V_00_2021_09_29_21_07_14.cat"
        if star == 'SWCas':
            return "PIRATE_413414_OSL_ROE_Ceph2_SWCas_00_SWCas_00_Filter_V_00_2021_09_29_22_04_51.cat"
        if star == 'RWCas':
            return "PIRATE_413415_OSL_ROE_Ceph2_RWCas_00_RWCas_00_Filter_V_00_2021_09_29_22_05_55.cat"

#same function as above except calls catalogues which the stars have been flipped
#only exception is RWCas, which never had any images flipped

def return_sdata180(star):
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/2021-10-16/")
        if star == 'GHCyg':
            return "PIRATE_418379_OSL_ROE_Ceph2_GHCyg_00_GHCyg_00_Filter_V_00_2021_10_16_23_39_33.cat"
        if star == 'V438Cyg':
            return "PIRATE_418409_OSL_ROE_Ceph2_V438Cyg_00_V438Cyg_00_Filter_V_00_2021_10_17_00_07_14.cat"
        if star == 'VXCyg':
            return "PIRATE_418424_OSL_ROE_Ceph2_VXCyg_00_VXCyg_00_Filter_V_00_2021_10_17_00_11_58.cat"
        if star == 'VZCyg':
            return "PIRATE_418434_OSL_ROE_Ceph2_VZCyg_00_VZCyg_00_Filter_V_00_2021_10_17_00_14_50.cat"
        if star == 'RSCas':
            return "PIRATE_418464_OSL_ROE_Ceph2_RSCas_00_RSCas_00_Filter_V_00_2021_10_17_00_23_35.cat"
        if star == 'RYCas':
            return "PIRATE_418470_OSL_ROE_Ceph2_RYCas_00_RYCas_00_Filter_V_01_2021_10_17_00_25_21.cat"
        if star == 'FMCas':
            return "PIRATE_418474_OSL_ROE_Ceph2_FMCas_00_FMCas_00_Filter_V_00_2021_10_17_00_26_42.cat"
        if star == 'TUCas':
            return "PIRATE_418484_OSL_ROE_Ceph2_TUCas_00_ObjectName_00_Filter_V_00_2021_10_17_00_28_52.cat"
        if star == 'DLCas':
            return "PIRATE_418494_OSL_ROE_Ceph2_DLCas_00_DLCas_00_Filter_V_00_2021_10_17_00_30_51.cat"
        if star == 'SWCas':
            return "PIRATE_418459_OSL_ROE_Ceph2_SWCas_00_SWCas_00_Filter_V_00_2021_10_17_00_21_59.cat"
        if star == 'RWCas':
            os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/2021-09-29/")
            return "PIRATE_413415_OSL_ROE_Ceph2_RWCas_00_RWCas_00_Filter_V_00_2021_09_29_22_05_55.cat"

#function to get the coordinates of the stars
def coords(star):
        #the loop checks over all of the rows in the excel document in the Cepheid column for the 'star' inputted into the function
        #this helps to get the number of the row in which the star is, which is called simply 'number'
        for i in range(len(data)):
            starcheck = data['Cepheid'][i]
            if str(starcheck)==star:
                number = i

        #'number' is used here to find the x and y coordinates of the Cepheid listed in the excel document
        X=data['X1'][number]
        Y=data['Y1'][number]

        #these coordinates are for the comparison stars associated with the Cepheid
        x1=data['X2'][number]
        y1=data['Y2'][number]

        x2=data['X2'][number+1]
        y2=data['Y2'][number+1]

        x3=data['X2'][number+2]
        y3=data['Y2'][number+2]

        x4=data['X2'][number+3]
        y4=data['Y2'][number+3]

        """now we have the coordinates read from the excel document, we can find the similar values in the source extracted data to correctly identify which are the source extracted x and y coordinates
        we do this by performing abs((x excel)-x(sextracted)+y(excel)-y(sextracted)) and finding the smallest value"""

        #sdata_star calls back to the function return_sdata
        #it is the name of the catalogue
        sdata_star=return_sdata("{}".format(star))

        #opens source extracted data
        with open("{}".format(sdata_star)) as f:
            sdata=f.readlines()

        #splits all of the spaces in the source extracted data past line 7, as before line 7 is the guide to interpret the different columns in the data, and the data starts from line 7
        #this gives 7 different columns, which are the differemt data types from the source extracted data.
        x=0
        for i in sdata:
            sdata[x+7]=sdata[x+7].split()
            x+=1
            if x+7==len(sdata):
                break

        def getcoords(chosenstar):

            #to differentiate between the different star inputs, Standard Stars are named 1 to 4 on the excel sheet,
            #and if any of those numbers are inputted then the corresponding Standard Star coordinates are used
            #for simplicity, anything else is assumed to be the Cepheid
            if chosenstar==1:
                coordinatesx=x1
                coordinatesy=y1
            elif chosenstar==2:
                coordinatesx=x2
                coordinatesy=y2
            elif chosenstar==3:
                coordinatesx=x3
                coordinatesy=y3
            elif chosenstar==4:
                coordinatesx=x4
                coordinatesy=y4
            else:
                coordinatesx=X
                coordinatesy=Y

            #to get a list of the x coordinates
            #we only need column 5 for the x coordinates, but all of the rows past 6, which is why it is looped over sdata[x+7][5]
            x=0
            xcoords=[]
            for i in sdata:
                #subtracts the excel value from source extracted value and finds the absolute value
                xcoord=abs(float(sdata[x+7][5])-coordinatesx)
                #adds to the list xcoords
                xcoords.append(xcoord)
                x+=1
                #breaks when the final value of the data is reached
                if x+7==len(sdata):
                    break

            #exact same as above except its for the y coordinates, so it uses column 6 instead of 5
            y=0
            ycoords=[]
            for i in sdata:
                ycoord=abs(float(sdata[y+7][6])-coordinatesy)
                ycoords.append(ycoord)
                y+=1
                if y+7==len(sdata):
                    break

            #adds the two lists of coordinates together (not to be confused with the individual coordinates) and appends them to sumlist
            sumlist = []
            for (item1, item2) in zip(xcoords, ycoords):
                sumlist.append(item1+item2)

            #finds the minimum value of sumlist
            minval=min(sumlist)
            #finds where the value is in sumlist (the index) which should be the Cepheid
            minindex=sumlist.index(minval)
            #finally, the cepheids values are taken from the source extracted data and attributed to 'cepheid'
            coordsofstar=sdata[minindex+7]

            return coordsofstar

        star1=getcoords(1)
        star2=getcoords(2)
        star3=getcoords(3)
        star4=getcoords(4)
        cepheid=getcoords(star)

        return cepheid, star1, star2, star3, star4

#same function as above except perfoms it for the flipped data
def coords180(star):
        #the loop checks over all of the rows in the excel document in the Cepheid column for the 'star' inputted into the function
        #this helps to get the number of the row in which the star is, which is called simply 'number'
        for i in range(len(data180)):
            starcheck = data180['Cepheid'][i]
            if str(starcheck)==star:
                number = i

        #'number' is used here to find the x and y coordinates of the Cepheid listed in the excel document
        X=data180['X1'][number]
        Y=data180['Y1'][number]

        #these coordinates are for the comparison stars associated with the Cepheid
        x1=data180['X2'][number]
        y1=data180['Y2'][number]

        x2=data180['X2'][number+1]
        y2=data180['Y2'][number+1]

        x3=data180['X2'][number+2]
        y3=data180['Y2'][number+2]

        x4=data180['X2'][number+3]
        y4=data180['Y2'][number+3]


        """now we have the coordinates read from the excel document, we can find the similar values in the source extracted data to correctly identify which are the source extracted x and y coordinates
        we do this by performing abs((x excel)-x(sextracted)+y(excel)-y(sextracted)) and finding the smallest value"""

        #sdata_star calls back to the function return_sdata
        #it is the name of the catalogue
        sdata_star180=return_sdata180("{}".format(star))

        #opens source extracted data
        with open("{}".format(sdata_star180)) as f180:
            sdata180=f180.readlines()

        #splits all of the spaces in the source extracted data past line 7, as before line 7 is the guide to interpret the different columns in the data, and the data starts from line 7
        #this gives 7 different columns, which are the differemt data types from the source extracted data.
        x=0
        for i in sdata180:
            sdata180[x+7]=sdata180[x+7].split()
            x+=1
            if x+7==len(sdata180):
                break

        def getcoords(chosenstar):

            #to differentiate between the different star inputs, Standard Stars are named 1 to 4 on the excel sheet,
            #and if any of those numbers are inputted then the corresponding Standard Star coordinates are used
            #for simplicity, anything else is assumed to be the Cepheid
            if chosenstar==1:
                coordinatesx=x1
                coordinatesy=y1
            elif chosenstar==2:
                coordinatesx=x2
                coordinatesy=y2
            elif chosenstar==3:
                coordinatesx=x3
                coordinatesy=y3
            elif chosenstar==4:
                coordinatesx=x4
                coordinatesy=y4
            else:
                coordinatesx=X
                coordinatesy=Y

            #to get a list of the x coordinates
            #we only need column 5 for the x coordinates, but all of the rows past 6, which is why it is looped over sdata[x+7][5]
            x=0
            xcoords=[]
            for i in sdata180:
                #subtracts the excel value from source extracted value and finds the absolute value
                xcoord=abs(float(sdata180[x+7][5])-coordinatesx)
                #adds to the list xcoords
                xcoords.append(xcoord)
                x+=1
                #breaks when the final value of the data is reached
                if x+7==len(sdata180):
                    break

            #exact same as above except its for the y coordinates, so it uses column 6 instead of 5
            y=0
            ycoords=[]
            for i in sdata180:
                ycoord=abs(float(sdata180[y+7][6])-coordinatesy)
                ycoords.append(ycoord)
                y+=1
                if y+7==len(sdata180):
                    break

            #adds the two lists of coordinates together (not to be confused with the individual coordinates) and appends them to sumlist
            sumlist = []
            for (item1, item2) in zip(xcoords, ycoords):
                sumlist.append(item1+item2)

            #finds the minimum value of sumlist
            minval=min(sumlist)
            #finds where the value is in sumlist (the index) which should be the Cepheid
            minindex=sumlist.index(minval)
            #finally, the cepheids values are taken from the source extracted data and attributed to 'cepheid'
            coordsofstar=sdata180[minindex+7]

            return coordsofstar

        star1=getcoords(1)
        star2=getcoords(2)
        star3=getcoords(3)
        star4=getcoords(4)
        cepheid=getcoords(star)

        return cepheid, star1, star2, star3, star4

#function to find the vector from the cepheid to the star
def getdistance(star):
        #returns the 5 values
        cepheid, star1, star2, star3, star4=coords(star)

        #takes the x and y coordinates of the 2 inputted stars and takes star1 away from star2: in essence, point B - point A = vectorAB, so gets the vector12
        def distance(star1,star2):
            xcoord1=star1[5]
            ycoord1=star1[6]
            xcoord2=star2[5]
            ycoord2=star2[6]
            xcoord=float(xcoord2)-float(xcoord1)
            ycoord=float(ycoord2)-float(ycoord1)
            return xcoord, ycoord

        #-> vector 1
        xcoord1, ycoord1=distance(cepheid, star1)
        #-> vector 2
        xcoord2, ycoord2=distance(cepheid, star2)
        #-> vector 3
        xcoord3, ycoord3=distance(cepheid, star3)
        #-> vector 4
        xcoord4, ycoord4=distance(cepheid, star4)

        #vector from cepheid to star 1
        vector1=[xcoord1,ycoord1]
        #vector from cepheid to star 2
        vector2=[xcoord2,ycoord2]
        #vector from cepheid to star 3
        vector3=[xcoord3,ycoord3]
        #vector from cepheid to star 4
        vector4=[xcoord4,ycoord4]

        return vector1, vector2, vector3, vector4

def getdistance180(star):
        #returns the 5 values
        cepheid, star1, star2, star3, star4=coords180(star)

        #takes the x and y coordinates of the 2 inputted stars and takes star1 away from star2: in essence, point B - point A = vectorAB, so gets the vector12
        def distance(star1,star2):
            xcoord1=star1[5]
            ycoord1=star1[6]
            xcoord2=star2[5]
            ycoord2=star2[6]
            xcoord=float(xcoord2)-float(xcoord1)
            ycoord=float(ycoord2)-float(ycoord1)
            return xcoord, ycoord

        #-> vector 1
        xcoord1, ycoord1=distance(cepheid, star1)
        #-> vector 2
        xcoord2, ycoord2=distance(cepheid, star2)
        #-> vector 3
        xcoord3, ycoord3=distance(cepheid, star3)
        #-> vector 4
        xcoord4, ycoord4=distance(cepheid, star4)

        #vector from cepheid to star 1
        vector1=[xcoord1,ycoord1]
        #vector from cepheid to star 2
        vector2=[xcoord2,ycoord2]print('2')
        #vector from cepheid to star 3
        vector3=[xcoord3,ycoord3]
        #vector from cepheid to star 4
        vector4=[xcoord4,ycoord4]

        return vector1, vector2, vector3, vector4

#function to get just the name of the star we're working with, which the point will become apparent later
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

#function to get rid of the .cat at the end of the catalogue, which is used later to add .txt at the end to make the shortened files with the
#same names as the catalogues a different file
def finaltxtname(slist):
    slist=slist.split(".cat")
    return slist[0]

#function which finds the stars, writes their coordinates into a txt file and moves the file from the original position to the shortened data folder
def findstar(star):
        #gets the 4 vectors from getdistance()
        vector1, vector2, vector3, vector4 = getdistance(star)

        #4 flipped vectors. For some reason, taking the negative of the normal vectors didn't work, so that's why the coordinates had to be remeasured
        #after this step, all the coordinates worked
        vector1180, vector2180, vector3180, vector4180 = getdistance180(star)

        #navigate to source extracted folder for cepheids
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/")

        #first loop loops over all of the different dates in the directory
        #these values will be explained later
        p=0
        q=0
        for i in datelist:
            print(i)
            #enters the date directory
            os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/{}/".format(i))
            #lists all of the catalogues in that date directory entered
            cataloguelist=os.listdir()
            #we make another variable to act on the getname() function so that we still have the original cataloguelist unchanged
            cataloguelistdifferent=os.listdir()

            #even though os.listdir() lists the directories seemingly randomly, the way that the directories are listed are the same every time
            #for example, in datelist, 2021-09-29 always came first, 2021-10-18 always came second etc no matter how many times os.listdir() was acted upon the directories
            #therefore, catlist, which is a list just the names of the cepheids, has the names in the same indexes as the cepheids in cataloguelist
            #this means that we have an easy way to find which catalogues are the cepheid in question we want to act on, and can differentiate from those that aren't
            catlist=getname(cataloguelistdifferent)

            #small loop to get the indexes in the list of the star catalogues of the star in question which we've inputted into the function at the start
            Number = []
            #if an element of catlist is the same as the argument of findstar(), append the index of the star to the list Number
            for r in range(len(catlist)print('2')):
                if catlist[r]==star:
                    Number.append(r)

            #This is the big loop which finds the coordinates of the cepheids and Stars
            #looping over the ~5 or however many pictures we got of a star that night
            for h in range(len(Number)):

                #opens one of the catalogues using the index found earlier, which we're gonna work with until the point is found
                with open("{}".format(cataloguelist[Number[h]])) as f:
                    catalogue=f.readlines()

                x=0
                #list of all of the coordinates of all of the stars in the catalogue
                #this is made into a vector list with the origin point at the corner of the image at [0,0]
                coordlist=[]

                #we need to save catalogue for later to write all the data for Shortened Data when we find the points of the stars, therefore we make diffcatalogue
                diffcatalogue=catalogue
                #loop to find the stars coordinates in x and y
                for s in diffcatalogue:
                    #splits the catalogue up
                    diffcatalogue[x+7]=diffcatalogue[x+7].split()
                    #takes column 5 and 6 for x and y coordinates respectively
                    coordlist.append([float(diffcatalogue[x+7][5]), float(diffcatalogue[x+7][6])])
                    x+=1
                    #when the end is reached, break
                    if x+7==len(diffcatalogue):
                        break
                    #turns the coordinate list into an array to make it a vector list which vector calculations can be done on
                    vlist=np.array(coordlist)
                #This returns vlist, which is the vector list

                #adds 1 to the value p, but not q, which were made at the beggining of the loop. q only comes at the end of this loop
                p+=1
                #loops over all of the coordinates in the catalogue to find the potential position of the Cepheid
                for n in vlist:

                    #calculates the first potential point, point1 with the first vector, vector1
                    point1=n-np.array(vector1)
                    for j in vlist:

                        #if point1 reaches another point in the catalogue defined by a vector from the origin, the code can continue
                        #since the centre of the point might be a bit different in each catalogue, an uncertainty in the position is introduced
                        #an uncertainty of +- 3 was found to be the best value, through trial and error
                        #its big enough to account for the uncertainty of calculating the coordinates of the center of the star
                        #however, not too big as to find potential other coordinates which match
                        if abs(point1[0]-j[0])<=3 and abs(point1[1]-j[1])<=3:

                            for k in vlist:
                                #calculates another point which is reached by another vector, vector2
                                point2=k-np.array(vector2)
                                #if thats the same point reached by vector2 as well as vector1, the same as before repeats
                                #again, an uncertainty in the exact coordinates in point2 is introduced in between different catalogues, so we have to account for that too

                                if abs(point2[0]-j[0])<=3 and abs(point2[1]-j[1])<=3:

                                    for l in vlist:

                                        point3=l-np.array(vector3)
                                        if abs(point3[0]-j[0])<=3 and abs(point3[1]-j[1])<=3:

                                            for m in vlist:

                                                point4=m-np.array(vector4)
                                                if abs(point4[0]-j[0])<=3 and abs(point4[1]-j[1])<=3:

                                                    #if this stage is reached i.e. the cepheid and comparison stars have been found succesfully, then q=p, and we know that
                                                    #the image wasn't inverted
                                                    q=p
                                                    #if all 4 vectors can reach the same point from other points,
                                                    #then it is likely that this common point is the cepheid and all the vectors
                                                    #are connecting to the comparison star
                                                    cepheidpoint=j
                                                    cstar1=n
                                                    cstar2=k
                                                    cstar3=l
                                                    cstar4=m

                                                    break
                if q==p:

                    #makes file which is called the name of the catalogue we're working with
                    write=open("{}.txt".format(finaltxtname(cataloguelist[Number[h]])), "w")
                    #finds the index of the coordinates found. this returns a 2 by 2 array [a,b][c,d]
                    cepheidindex=np.where(vlist==cepheidpoint)

                    write.write("Cepheid {}\n".format(star))
                    #in [a,b][c,d], we want a as thats the index of the cepheid. We add 7 to account for the information lines at the start of the catalogue
                    write.write(str(catalogue[int(cepheidindex[0][0])+7]))
                    write.write("\n")

                    cstar1index=np.where(vlist==cstar1)
                    write.write("Comparison Stars\n")
                    write.write(str(catalogue[int(cstar1index[0][0])+7]))
                    write.write("\n")

                    cstar2index=np.where(vlist==cstar2)
                    write.write(str(catalogue[int(cstar2index[0][0])+7]))
                    write.write("\n")

                    cstar3index=np.where(vlist==cstar3)
                    write.write(str(catalogue[int(cstar3index[0][0])+7]))
                    write.write("\n")

                    cstar4index=np.where(vlist==cstar4)
                    write.write(str(catalogue[int(cstar4index[0][0])+7]))

                    write.close()

                    #renames the file as a txt file and moves is to the correct directory in shortened data
                    original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/{}/{}".format(i,str(finaltxtname(cataloguelist[Number[h]])+".txt"))
                    target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/{}".format(i,str(finaltxtname(cataloguelist[Number[h]])+".txt"))

                    shutil.move(original,target)

                #if q does not equal p i.e. the conditions in the previous loop were not met to get to the final point, then that means that the image was flipped
                #now, we work with the new data with all the flipped vectors
                if q != p:

                    for n in vlist:

                        point1=n-np.array(vector1180)
                        for j in vlist:

                            if abs(point1[0]-j[0])<=3 and abs(point1[1]-j[1])<=3:

                                for k in vlist:

                                    point2=k-np.array(vector2180)

                                    if abs(point2[0]-j[0])<=3 and abs(point2[1]-j[1])<=3:

                                        for l in vlist:
                                            point3=l-np.array(vector3180)
                                            if abs(point3[0]-j[0])<=3 and abs(point3[1]-j[1])<=3:

                                                for m in vlist:
                                                    point4=m-np.array(vector4180)
                                                    if abs(point4[0]-j[0])<=3 and abs(point4[1]-j[1])<=3:

                                                        cepheidpoint=j

                                                        cstar1=n
                                                        cstar2=k
                                                        cstar3=l
                                                        cstar4=m
                                                        break
                if q!=p:

                    write=open("{}.txt".format(finaltxtname(cataloguelist[Number[h]])), "w")

                    cepheidindex=np.where(vlist==cepheidpoint)

                    write.write("Cepheid {}\n".format(star))
                    write.write(str(catalogue[int(cepheidindex[0][0])+7]))
                    write.write("\n")

                    cstar1index=np.where(vlist==cstar1)
                    write.write("Comparison Stars\n")
                    write.write(str(catalogue[int(cstar1index[0][0])+7]))
                    write.write("\n")

                    cstar2index=np.where(vlist==cstar2)
                    write.write(str(catalogue[int(cstar2index[0][0])+7]))
                    write.write("\n")

                    cstar3index=np.where(vlist==cstar3)
                    write.write(str(catalogue[int(cstar3index[0][0])+7]))
                    write.write("\n")

                    cstar4index=np.where(vlist==cstar4)
                    write.write(str(catalogue[int(cstar4index[0][0])+7]))

                    write.close()

                    original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Cepheids/{}/{}".format(i,str(finaltxtname(cataloguelist[Number[h]])+".txt"))
                    target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/{}/{}".format(i,str(finaltxtname(cataloguelist[Number[h]])+".txt"))

                    shutil.move(original,target)

                    #adds 1 to q finally so that q and p are equal again
                    q+=1

#finally we call the functions for all of the cepheids and let the code do the rest of the work B)
findstar('GHCyg')
findstar('V438Cyg')
findstar('VZCyg')
findstar('VXCyg')
findstar('RSCas')
findstar('RYCas')
findstar('FMCas')
findstar('TUCas')
findstar('DLCas')
findstar('RWCas')
findstar('SWCas')
