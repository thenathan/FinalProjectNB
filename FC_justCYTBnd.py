#! /usr/bin/python
import re

allSpecies = {

	'Agelaius cyanopus' : 0,
	'Agelaius flavus' : 0,
	'Agelaius humeralis' : 0,
	'Agelaius icterocephalus' : 0,
	'Agelaius phoeniceus' : 0,
	'Agelaius phoeniceus arctolegus' : 0,
	'Agelaius phoeniceus assimilis' : 0,
	'Agelaius phoeniceus grinnelli' : 0,
	'Agelaius phoeniceus gubernator' : 0,
	'Agelaius phoeniceus mearnsi' : 0,
	'Agelaius phoeniceus phoeniceus' : 0,
	'Agelaius ruficapillus' : 0,
	'Agelaius tricolor' : 0,
	'Agelaius xanthomus' : 0,
	'Agelaius xanthophthalmus' : 0,
	'Amblycercus holosericeus' : 0,
	'Amblycercus holosericeus australis' : 0,
	'Amblycercus holosericeus holosericeus' : 0,
	'Amblyramphus holosericeus' : 0,
	'Cacicus cela' : 0,
	'Cacicus cela cela' : 0,
	'Cacicus cela vitellinus' : 0,
	'Cacicus chrysonotus chrysonotus' : 0,
	'Cacicus chrysonotus leucoramphus' : 0,
	'Cacicus chrysonotus peruvianus' : 0,
	'Cacicus chrysopterus' : 0,
	'Cacicus haemorrhous haemorrhous' : 0,
	'Cacicus koepckeae' : 0,
	'Cacicus leucoramphus' : 0,
	'Cacicus melanicterus' : 0,
	'Cacicus sclateri' : 0,
	'Cacicus solitarius' : 0,
	'Cacicus uropygialis' : 0,
	'Cacicus uropygialis microrhynchus' : 0,
	'Cacicus uropygialis pacificus' : 0,
	'Cacicus uropygialis uropygialis' : 0,
	'Chrysomus cyanopus' : 0,
	'Chrysomus thilius' : 0,
	'Curaeus curaeus' : 0,
	'Curaeus forbesi' : 0,
	'Dives atroviolaceus' : 0,
	'Dives bonariensis' : 0,
	'Dives dives' : 0,
	'Dives warszwewiczi' : 0,
	'Dolichonyx oryzivorus' : 0,
	'Euphagus carolinus' : 0,
	'Euphagus cyanocephalus' : 0,
	'Gnorimopsar chopi' : 0,
	'Gymnomystax mexicanus' : 0,
	'Gymnostinops bifasciatus neivae' : 0,
	'Gymnostinops bifasciatus yuracares' : 0,
	'Gymnostinops montezuma' : 0,
	'Gymnostinops yuracares' : 0,
	'Hypopyrrhus pyrohypogaster' : 0,
	'Icterus abeillei' : 0,
	'Icterus auratus' : 0,
	'Icterus auricapillus' : 0,
	'Icterus bonana' : 0,
	'Icterus bullockii' : 0,
	'Icterus bullockii parvus' : 0,
	'Icterus cayanensis' : 0,
	'Icterus cayanensis cayanensis' : 0,
	'Icterus cayanensis chrysocephalus' : 0,
	'Icterus cayanensis periporphyrus' : 0,
	'Icterus cayanensis pyrrhopterus' : 0,
	'Icterus cayanensis tibialis' : 0,
	'Icterus chrysater chrysater' : 0,
	'Icterus chrysater hondae' : 0,
	'Icterus cucullatus igneus' : 0,
	'Icterus cucullatus nelsoni' : 0,
	'Icterus dominicensis' : 0,
	'Icterus dominicensis dominicensis' : 0,
	'Icterus dominicensis melanopsis' : 0,
	'Icterus dominicensis northropi' : 0,
	'Icterus dominicensis portoricensis' : 0,
	'Icterus dominicensis prosthemelas' : 0,
	'Icterus galbula' : 0,
	'Icterus galbula galbula' : 0,
	'Icterus graceannae' : 0,
	'Icterus graduacauda audubonii' : 0,
	'Icterus graduacauda graduacauda' : 0,
	'Icterus gularis gularis' : 0,
	'Icterus gularis tamaulipensis' : 0,
	'Icterus gularis yucatanensis' : 0,
	'Icterus icterus' : 0,
	'Icterus icterus ridgewayi' : 0,
	'Icterus jamacaii strictifrons' : 0,
	'Icterus laudabilis' : 0,
	'Icterus leucopteryx' : 0,
	'Icterus maculialatus' : 0,
	'Icterus mesomelas' : 0,
	'Icterus mesomelas mesomelas' : 0,
	'Icterus mesomelas salvinii' : 0,
	'Icterus nigrogularis' : 0,
	'Icterus nigrogularis trinitatis' : 0,
	'Icterus oberi' : 0,
	'Icterus parisorum' : 0,
	'Icterus pectoralis' : 0,
	'Icterus prosthemelas' : 0,
	'Icterus pustulatus' : 0,
	'Icterus pustulatus formosus' : 0,
	'Icterus pustulatus sclateri' : 0,
	'Icterus spurius' : 0,
	'Icterus spurius fuertesi' : 0,
	'Icterus spurius spurius' : 0,
	'Icterus wagleri wagleri' : 0,
	'Lampropsar tanagrinus' : 0,
	'Leistes militaris' : 0,
	'Macroagelaius imthurni' : 0,
	'Macroagelaius subalaris' : 0,
	'Melospiza melodia' : 0,
	'Molothrus aeneus' : 0,
	'Molothrus ater' : 0,
	'Molothrus badius' : 0,
	'Molothrus bonariensis' : 0,
	'Molothrus rufoaxillaris' : 0,
	'Nesopsar nigerrimus' : 0,
	'Ocyalus latirostris' : 0,
	'Oreopsar bolivianus' : 0,
	'Passerina cyanea' : 0,
	'Psarocolius angustifrons' : 0,
	'Psarocolius angustifrons alfredi' : 0,
	'Psarocolius angustifrons angustifrons' : 0,
	'Psarocolius angustifrons atrocastaneus' : 0,
	'Psarocolius atrovirens' : 0,
	'Psarocolius bifasciatus yuracares' : 0,
	'Psarocolius cassini' : 0,
	'Psarocolius decumanus' : 0,
	'Psarocolius decumanus decumanus' : 0,
	'Psarocolius decumanus insularis' : 0,
	'Psarocolius decumanus maculosus' : 0,
	'Psarocolius decumanus melanterus' : 0,
	'Psarocolius guatimozinus' : 0,
	'Psarocolius oseryi' : 0,
	'Psarocolius viridis' : 0,
	'Psarocolius wagleri ridgwayi' : 0,
	'Psarocolius wagleri wagleri' : 0,
	'Pseudoleistes guirahuro' : 0,
	'Pseudoleistes virescens' : 0,
	'Quiscalus lugubris' : 0,
	'Quiscalus lugubris lugubris' : 0,
	'Quiscalus major' : 0,
	'Quiscalus mexicanus' : 0,
	'Quiscalus nicaraguensis nicaraguensis' : 0,
	'Quiscalus niger' : 0,
	'Quiscalus niger niger' : 0,
	'Quiscalus quiscula' : 0,
	'Saltator coerulescens' : 0,
	'Scaphidura oryzivora' : 0,
	'Spiza americana' : 0,
	'Sturnella bellicosa' : 0,
	'Sturnella defilippii' : 0,
	'Sturnella loyca' : 0,
	'Sturnella magna' : 0,
	'Sturnella magna paralios' : 0,
	'Sturnella militaris' : 0,
	'Sturnella neglecta' : 0,
	'Sturnella superciliaris' : 0,
	'Thraupis episcopus' : 0,
	'Xanthocephalus xanthocephalus' : 0

}

##  >gi|564813697|gb|KF810932.1| Sturnella defilippii voucher AMNH 816591 cytochrome b (CYTB) gene, partial cds; mitochondrial

#
#  Use Regex to get candidate sub species from a gi line
#  .  get the first three words separated by spaces.
#  .  Example "Sturnella defilippii voucher" in above line
#
def getSubspecies (line):
	gnarly = line [4:]
	m = re.search(r"[A-Za-z]+ [A-Za-z]+ [A-Za-z]+", gnarly)
	gnarly = m.group()
	return (gnarly)

#  Use Regex to get candidate species from a gi line
#  .  get the first two words separated by spaces.
#  .  Example "Sturnella defilippii"

def getSpecies (line):
	gnarly = line [4:]
	m = re.search(r"[A-Za-z]+ [A-Za-z]+", gnarly)
	gnarly = m.group()
	return (gnarly)

#  Check if speciesName is in the dictionary of species names

def hasDictEntry (speciesName):
	result = False
	hasEntry = allSpecies.get(speciesName, -1)
	if (hasEntry > -1):
		result = True
	return result


#  For a "gi" line
#  .  Check if the line has a sub species:
#  .  Pull out the first three words
#  .  Are they in the species dictionary?
#  .  If so, does the subspecies still need to be printed?
#  .  If so, mark that the subspecies is being printed, return True
#  .  Else if there is no subspecies, repeat the same check for a species (first two words)

def checkIfShouldPrint (line):
	result = False

	speciesName = getSubspecies(line)
	lookUp = hasDictEntry (speciesName)
	if (lookUp):
		gnarly = int(allSpecies [speciesName])
		if (0 == gnarly):
			allSpecies [speciesName] = 1
			result = True

	else:
		speciesName = getSpecies(line)
		lookUp = hasDictEntry (speciesName)
		if (lookUp):
			gnarly = int(allSpecies [speciesName])
			if (0 == gnarly):
				allSpecies [speciesName] = 1
				result = True

	return result


file = open ("icterid.fasta")
out_handle = open("icteridcytnd.fasta", "w")
printLines = False
for line in file:
	#line = line.rstrip("\n")

	
	#  If "gi" line, check for 
	#  .  cytochrome B (not full genome)
	#  .  then check if this bird has not been printed,  if not, set the flag to print it
	#  .  else clear the flag to skip printing this bird
	
	if re.search("gi", line):
		if re.search("cytochrome", line):
			printLines = checkIfShouldPrint (line)

		else:
			printLines = False

	if (printLines):
		#print (line.rstrip("\n"))
                #instead, save to new file
                out_handle.write(line)

out_handle.close()
