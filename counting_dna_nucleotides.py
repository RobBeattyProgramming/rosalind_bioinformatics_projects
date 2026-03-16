sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
nucleotideDict = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}

for i in sample:
    if i in nucleotideDict:
        x = nucleotideDict[i]
        x = x + 1
        nucleotideDict[i] = x


for y in nucleotideDict:
    print(y)
    print(nucleotideDict[y])
       
