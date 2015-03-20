#! /usr/bin/python

#Import from Biopython
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "thenathanburroughs@gmail.com"

#puts Icteridae and CYTB into a variable
search_string = "Icteridae AND CYTB"

#Search and Read
handle = Entrez.esearch(db="nucleotide", term=search_string, usehistory="y")
record = Entrez.read(handle)
handle.close()

webenv = record["WebEnv"]
query_key = record["QueryKey"]

#Save ID list in gi_list and put number of IDs in count

gi_list = record["IdList"]
count = int(record["Count"])

print ("Count: ", count)

# Cached search, three genomes returned at a time in fasta format
# Write the three into the file "icterid.fasta"

batch_size = 3
out_handle = open("icterid.fasta", "w")
for start in range(0, count, batch_size):
    end = min(count, start+batch_size)
    fetch_handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", retstart=start, retmax=batch_size, webenv=webenv, query_key=query_key)
    data = fetch_handle.read()
    print(data)
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()
