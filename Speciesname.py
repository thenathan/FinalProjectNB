#open Icterid file

icterid_file = "Icteridnestshape.txt"

open_icterid = open(icterid_file)

#read everything from Icterids file, put in content variable

icterid_contents = open_icterid.read()

import re
