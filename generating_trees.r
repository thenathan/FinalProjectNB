#Generates a tree
library(ape)
icterid.nexus.phylo <-
  read.nexus("test5.nex.con.tre")
plot(icterid.nexus.phylo, cex = 0.2)
#Saved tree as Icteridtree1.pdf


#Generates a tree, removes Agelaius phoeniceus which extends really far for some reason
icterid.nexus.phylo.drop <- drop.tip(icterid.nexus.phylo, c("Agelaius_phoeniceus"))
plot(icterid.nexus.phylo.drop, cex = 0.2)
#Saved tree as Icteridtree2.pdf

#Generates a fan shaped tree
library(ape)
icterid.nexus.phylo.drop <- drop.tip(icterid.nexus.phylo, c("Agelaius_phoeniceus"))
plot(icterid.nexus.phylo.drop, cex = 0.2, type = "fan")
#Saved tree as Icteridtree3.pdf


#Generates a tree with smaller font
icterid.nexus.phylo.drop <- drop.tip(icterid.nexus.phylo, c("Agelaius_phoeniceus"))
plot(icterid.nexus.phylo.drop, cex = 0.15)
#Saved tree as Icteridtree4.pdf