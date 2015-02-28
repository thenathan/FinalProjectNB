#! /usr/bin/python

#Check how many records there are

from Bio import Entrez
Entrez.email = "thenathanburroughs@gmail.com"     # Always tell NCBI who you are
handle = Entrez.egquery(term="Icteridae AND cytochrome b")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"]=="nuccore":
        print(row["Count"])

#download the list of GenBank identifiers:

handle = Entrez.esearch(db="nuccore", term="Icteridae AND cytochrome b")
record = Entrez.read(handle)
gi_list = record["IdList"]
gi_list

#Using GenBank identifiers, download GenBank records

gi_str = ",".join(gi_list)
handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb", retmode="text")

#look ar raw GenBank files

text = handle.read()
print(text)

#get records in python friendly form

from Bio import SeqIO
handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb", retmode="text")
records = SeqIO.parse(handle, "gb")
