# Telescope-Group-Project
I worked on a group project with 4 other people to image Cepheid variable stars and use the luminosity-period
relation of the stars to calculate the distance to a cephied in the Andromeda galaxy.

Short Overview of the Code- 

This project required the use of large datasets of stars, using the code Source Extractor (SExtractor) 
to extract information off of several telescope images taken with 
the open university telescope in Tenerife,
find the cepheid variable stars, calibrate the measured flux for extinction of the atmosphere to get the real flux of the stars and finally
convert the magnitudes to the g colour band, as we used images from the liverpool telescope of a cepheid variable star in the Andromeda galaxy,
which were taken in the g band.

Code - 

sextract.py - Runs the software SExtractor on the CCD images taken with the telescope to extract a catalogue for each image containing
the thousands of stars in the CCD
image, with the catalogue recording the x and y coordinates on the CCD image, and the observed magnitude of each star. Standard candle stars were also 
imaged on the first night, and these were SExtracted too. They are used later to correct magnitudes of cepheids on the consecutive nights based on
the first night.

At this point, an excel spreadsheet was made containing the coordinates of each of the cepheids in one of the images, and 4 standard stars whose positions
and luminosity don't change over time, used to help make vectors between the cepheid and the standard stars so that these unique set of vectors could be
looped over all of the thousands of stars in the catalogues and eventually a match is found, containing the cepheid variable star and the other 4 standard
stars.

findstar.py - Reads in the excel spreadsheet containing the coordinates, makes the vectors, loops over all of the catalogues and returns the
coordinates and the magnitude of the cepheid variable star and standard star.
Sometimes the images are flipped 180 degrees, however for some reason flipping the vectors 180
degrees didn't work, so the same process had to be repeated a second time to get the flipped images data (get coords, record in excel, get vectors, loop
until star was found).

andromeda1.py - Finds the cepheid in the Andromeda SExtracted data in the same manner as above.
Only this time, the liverpool telescope had images flipped 0, 90, 180 and 270 degrees
annoyingly, so the same process had to be repeated 4 times.

airmass.txt - Right ascension and declination of stars on the first night.

airmass.py - Corrects the standard stars, cepheid variable stars and standard candle stars' magnitudes for airmass extinction using the magnitudes of
the standard stars.

andromeda2.py - Corrects Andromeda magnitude for atmospheric extinction, depending on how much atmosphere the telescope was looking through at the time
of observation to image the cepheid star.

correct.py - Corrects the stars on every other night with respect to the stars on the first night. On the first night, standard candles were measured,
which are greatly studied stars whose magnitude are known extremely precisely, and so the standard stars selected on the first night can be corrected
using the values measured on the first night, and now since we have these standard stars corrected and we know that their magnitude won't change between
nights, we can correct every other standard star every other night. Then, using this difference, the cepheid variable magnitudes can be found for 
every other night too.

The cepheid variable stars period luminosity relation can now be calculated by plotting the magnitudes and using curve fitting to make a sin/sawtooth graph
(the difference in graphs comes down to stellar physics of these stars)

bvcolour.py - Andromeda data was observed the second night of observations, so by used the corrected standard stars taken on that night, the B-V colour
had to be calculated to get the colour in the G band of the standard stars.

gband.py - The standard stars g band magnitude was then used to correct the Andromeda data for atmospheric extinction, as the 
Andromeda data was taken in the G band, while our data was taken in the V and B band.

Now the Andromeda data can be analysed in the same way as the cepheid stars we measured were. The period - luminosity relation can be found, and therefore
a distance can be found using the observed magnitudes.

correctg.py - I can't remember but feel its important so I've included it here as well
