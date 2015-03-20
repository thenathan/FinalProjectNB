#! /usr/bin/python

import re

#open Icterid file

icterid_file = "Icteridnestshape.txt"

open_icterid = open(icterid_file)

newoutput = []

#Use regular expressions to find genus_species

for line in open_icterid:
    #print(line)
    m = re.search("[A-Za-z]+_[A-Za-z]+", line)
    #Use regular expressions to seperate genus and species
    if m:
        gs = m.group()
        #print(gs)
        mgenus = re.search("[A-Za-z]+", gs)
        mspecies = re.search(r"[A-Za-z]+$", gs)
        genus = mgenus.group()
        species = mspecies.group()

        output = open("genus_and_species.txt", "w")
        output.write(genus + " " + species)
        output.close()        
        
        #Save into a new vector
        newoutput.append(genus + " " + species)
open_icterid.close()

#save new vector as a file
f = open("gs2.txt", "w")
for element in newoutput:
    f.write(element + '\n')
f.close()
