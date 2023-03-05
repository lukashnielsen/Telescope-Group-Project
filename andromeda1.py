import os
from os import listdir
import pandas as pd
import numpy as np
import shutil


#excel data for rough positions of cepheids and stars
data = pd.read_excel (r'/storage/teaching/2021-22/tgp/Cepheids2/comparison stars/Comparison Stars - GAIA coordinates.xlsx',sheet_name=2)
data90 = pd.read_excel (r'/storage/teaching/2021-22/tgp/Cepheids2/comparison stars/Comparison Stars - GAIA coordinates.xlsx',sheet_name=3)
data180=pd.read_excel (r'/storage/teaching/2021-22/tgp/Cepheids2/comparison stars/Comparison Stars - GAIA coordinates.xlsx',sheet_name=4)
data270=pd.read_excel (r'/storage/teaching/2021-22/tgp/Cepheids2/comparison stars/Comparison Stars - GAIA coordinates.xlsx',sheet_name=5)
#function to call on the specific catalogue which the x and y coordinates of the cepheids and comparison stars were taken from and put into the excel file
#the function takes the argument , which is the cepheid, and returns the catalogue used

def return_sdata():
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/LT/")
    return "h_e_20170608_101_1_1_1.fits.cat"

def return_sdata90():
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/LT/")
    return "h_e_20170613_127_1_1_1.fits.cat"

def return_sdata180():
    os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/LT/")
    return "h_e_20170912_128_1_1_1.fits.cat"

def return_sdata270():
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/LT/")
        return "h_e_20170818_81_1_1_1.fits.cat"

#same function as above except calls catalogues which the stars have been flipped
#only exception is RWCas, which never had any images flipped
#function to get the coordinates of the stars
def coords():
        #these coordinates are for the comparison stars associated with the Cepheid
        X=data['X1'][0]
        Y=data['Y1'][0]

        x1=data['X2'][0]
        y1=data['Y2'][0]

        x2=data['X2'][1]
        y2=data['Y2'][1]

        x3=data['X2'][2]
        y3=data['Y2'][2]

        x4=data['X2'][3]
        y4=data['Y2'][3]

        """now we have the coordinates read from the excel document, we can find the similar values in the source extracted data to correctly identify which are the source extracted x and y coordinates
        we do this by performing abs((x excel)-x(sextracted)+y(excel)-y(sextracted)) and finding the smallest value"""

        #sdata_star calls back to the function return_sdata
        #it is the name of the catalogue
        sdata_star=return_sdata()

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
        cepheid=getcoords('Andromeda')

        return cepheid, star1, star2, star3, star4

def coords90():
        #the loop checks over all of the rows in the excel document in the Cepheid column for the 'star' inputted into the function
        #this helps to get the number of the row in which the star is, which is called simply 'number'
        X=data90['X1'][0]
        Y=data90['Y1'][0]

        x1=data90['X2'][0]
        y1=data90['Y2'][0]

        x2=data90['X2'][1]
        y2=data90['Y2'][1]

        x3=data90['X2'][2]
        y3=data90['Y2'][2]

        x4=data90['X2'][3]
        y4=data90['Y2'][3]


        """now we have the coordinates read from the excel document, we can find the similar values in the source extracted data to correctly identify which are the source extracted x and y coordinates
        we do this by performing abs((x excel)-x(sextracted)+y(excel)-y(sextracted)) and finding the smallest value"""

        #sdata_star calls back to the function return_sdata
        #it is the name of the catalogue
        sdata_star90=return_sdata90()

        #opens source extracted data
        with open("{}".format(sdata_star90)) as f90:
            sdata90=f90.readlines()

        #splits all of the spaces in the source extracted data past line 7, as before line 7 is the guide to interpret the different columns in the data, and the data starts from line 7
        #this gives 7 different columns, which are the differemt data types from the source extracted data.
        x=0
        for i in sdata90:
            sdata90[x+7]=sdata90[x+7].split()
            x+=1
            if x+7==len(sdata90):
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
            for i in sdata90:
                #subtracts the excel value from source extracted value and finds the absolute value
                xcoord=abs(float(sdata90[x+7][5])-coordinatesx)
                #adds to the list xcoords
                xcoords.append(xcoord)
                x+=1
                #breaks when the final value of the data is reached
                if x+7==len(sdata90):
                    break

            #exact same as above except its for the y coordinates, so it uses column 6 instead of 5
            y=0
            ycoords=[]
            for i in sdata90:
                ycoord=abs(float(sdata90[y+7][6])-coordinatesy)
                ycoords.append(ycoord)
                y+=1
                if y+7==len(sdata90):
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
            coordsofstar=sdata90[minindex+7]

            return coordsofstar

        star1=getcoords(1)
        star2=getcoords(2)
        star3=getcoords(3)
        star4=getcoords(4)
        cepheid=getcoords('Andromeda')

        return cepheid, star1, star2, star3, star4

def coords180():
        #the loop checks over all of the rows in the excel document in the Cepheid column for the 'star' inputted into the function
        #this helps to get the number of the row in which the star is, which is called simply 'number'
        X=data180['X1'][0]
        Y=data180['Y1'][0]

        x1=data180['X2'][0]
        y1=data180['Y2'][0]

        x2=data180['X2'][1]
        y2=data180['Y2'][1]

        x3=data180['X2'][2]
        y3=data180['Y2'][2]

        x4=data180['X2'][3]
        y4=data180['Y2'][3]


        """now we have the coordinates read from the excel document, we can find the similar values in the source extracted data to correctly identify which are the source extracted x and y coordinates
        we do this by performing abs((x excel)-x(sextracted)+y(excel)-y(sextracted)) and finding the smallest value"""

        #sdata_star calls back to the function return_sdata
        #it is the name of the catalogue
        sdata_star180=return_sdata180()

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
        cepheid=getcoords('Andromeda')

        return cepheid, star1, star2, star3, star4

def coords270():
        #the loop checks over all of the rows in the excel document in the Cepheid column for the 'star' inputted into the function
        #this helps to get the number of the row in which the star is, which is called simply 'number'
        X=data270['X1'][0]
        Y=data270['Y1'][0]

        x1=data270['X2'][0]
        y1=data270['Y2'][0]

        x2=data270['X2'][1]
        y2=data270['Y2'][1]

        x3=data270['X2'][2]
        y3=data270['Y2'][2]

        x4=data270['X2'][3]
        y4=data270['Y2'][3]


        """now we have the coordinates read from the excel document, we can find the similar values in the source extracted data to correctly identify which are the source extracted x and y coordinates
        we do this by performing abs((x excel)-x(sextracted)+y(excel)-y(sextracted)) and finding the smallest value"""

        #sdata_star calls back to the function return_sdata
        #it is the name of the catalogue
        sdata_star270=return_sdata270()

        #opens source extracted data
        with open("{}".format(sdata_star270)) as f270:
            sdata270=f270.readlines()

        #splits all of the spaces in the source extracted data past line 7, as before line 7 is the guide to interpret the different columns in the data, and the data starts from line 7
        #this gives 7 different columns, which are the differemt data types from the source extracted data.
        x=0
        for i in sdata270:
            sdata270[x+7]=sdata270[x+7].split()
            x+=1
            if x+7==len(sdata270):
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
            for i in sdata270:
                #subtracts the excel value from source extracted value and finds the absolute value
                xcoord=abs(float(sdata270[x+7][5])-coordinatesx)
                #adds to the list xcoords
                xcoords.append(xcoord)
                x+=1
                #breaks when the final value of the data is reached
                if x+7==len(sdata270):
                    break

            #exact same as above except its for the y coordinates, so it uses column 6 instead of 5
            y=0
            ycoords=[]
            for i in sdata270:
                ycoord=abs(float(sdata270[y+7][6])-coordinatesy)
                ycoords.append(ycoord)
                y+=1
                if y+7==len(sdata270):
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
            coordsofstar=sdata270[minindex+7]

            return coordsofstar

        star1=getcoords(1)
        star2=getcoords(2)
        star3=getcoords(3)
        star4=getcoords(4)
        cepheid=getcoords('Andromeda')

        return cepheid, star1, star2, star3, star4

#function to find vectors that go to each of the stars from the other stars
def getdistance():
        #returns the 5 values
        cepheid, star1, star2, star3, star4=coords()

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

def getdistance90():
        #returns the 5 values
        cepheid, star1, star2, star3, star4=coords90()

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

def getdistance180():
        #returns the 5 values
        cepheid, star1, star2, star3, star4=coords180()

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

def getdistance270():
        #returns the 5 values
        cepheid, star1, star2, star3, star4=coords270()

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
    slist=slist.split(".fits.cat")
    return slist[0]

#function which finds the stars, writes their coordinates into a txt file and moves the file from the original position to the shortened data folder
def findstar():
        #gets the 4 vectors from getdistance()
        vector1, vector2, vector3, vector4 = getdistance()

        vector190, vector290, vector390, vector490 = getdistance90()

        vector1180, vector2180, vector3180, vector4180 = getdistance180()

        vector1270, vector2270, vector3270, vector4270 = getdistance270()

        #navigate to source extracted folder for cepheids
        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/")

        filtlist=os.listdir()
        #first loop loops over all of the different dates in the directory
        #these values will be explained later
        p=0
        q=0

        os.chdir("/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/LT/")
        #lists all of the catalogues in that date directory entered
        cataloguelist=os.listdir()


        #This is the big loop which finds the coordinates of the cepheids and Stars
        #loping over the ~5 or however many pictures we got of a star that night
        for h in range(len(cataloguelist)):

            #opens one of the catalogues using the index found earlier, which we're gonna work with until the point is found
            with open("{}".format(cataloguelist[h])) as f:
                catalogue=f.readlines()

            print(cataloguelist[h])
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

            #if q does not equal p i.e. the conditions in the previous loop were not met to get to the final point, then that means that the image was flipped
            #now, we work with the new data with all the flipped vectors
            if q != p:

                for n in vlist:

                    point1=n-np.array(vector190)
                    for j in vlist:

                        if abs(point1[0]-j[0])<=3 and abs(point1[1]-j[1])<=3:

                            for k in vlist:

                                point2=k-np.array(vector290)

                                if abs(point2[0]-j[0])<=3 and abs(point2[1]-j[1])<=3:

                                    for l in vlist:
                                        point3=l-np.array(vector390)
                                        if abs(point3[0]-j[0])<=3 and abs(point3[1]-j[1])<=3:

                                            for m in vlist:
                                                point4=m-np.array(vector490)
                                                if abs(point4[0]-j[0])<=3 and abs(point4[1]-j[1])<=3:

                                                    cepheidpoint=j
                                                    q=p
                                                    cstar1=n
                                                    cstar2=k
                                                    cstar3=l
                                                    cstar4=m
                                                    break
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
                                                    q=p
                                                    cstar1=n
                                                    cstar2=k
                                                    cstar3=l
                                                    cstar4=m
                                                    break


            if q != p:

                for n in vlist:

                    point1=n-np.array(vector1270)
                    for j in vlist:

                        if abs(point1[0]-j[0])<=3 and abs(point1[1]-j[1])<=3:

                            for k in vlist:

                                point2=k-np.array(vector2270)

                                if abs(point2[0]-j[0])<=3 and abs(point2[1]-j[1])<=3:

                                    for l in vlist:
                                        point3=l-np.array(vector3270)
                                        if abs(point3[0]-j[0])<=3 and abs(point3[1]-j[1])<=3:

                                            for m in vlist:
                                                point4=m-np.array(vector4270)
                                                if abs(point4[0]-j[0])<=3 and abs(point4[1]-j[1])<=3:

                                                    cepheidpoint=j
                                                    q=p
                                                    cstar1=n
                                                    cstar2=k
                                                    cstar3=l
                                                    cstar4=m
                                                    break


            #makes file which is called the name of the catalogue we're working with
            write=open("{}.txt".format(finaltxtname(cataloguelist[h])), "w")
            #finds the index of the coordinates found. this returns a 2 by 2 array [a,b][c,d]
            cepheidindex=np.where(vlist==cepheidpoint)
            if len(cepheidindex[0])>0:
                #in [a,b][c,d], we want a as thats the index of the cepheid. We add 7 to account for the information lines at the start of the catalogue
                write.write(str(catalogue[int(cepheidindex[0][0])+7]))
                write.write("\n")

                cstar1index=np.where(vlist==cstar1)
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
                original = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Andromeda/LT/{}".format(str(finaltxtname(cataloguelist[h])+".txt"))
                target = "/storage/teaching/2021-22/tgp/Cepheids2/source-extracted data/Shortened Data/Andromeda/LT/{}".format(str(finaltxtname(cataloguelist[h])+".txt"))
                shutil.move(original,target)


            #adds 1 to q finally so that q and p are equal again



findstar()
