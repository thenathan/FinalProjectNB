#! /usr/bin/python

import re

#open Icterid file

icterid_file = "Icteridnestshape.txt"

open_icterid = open(icterid_file)

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
        print(genus + " " + species)
open_icterid.close()
