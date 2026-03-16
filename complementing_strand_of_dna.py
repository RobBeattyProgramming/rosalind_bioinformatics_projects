def complementStrand(strand):
    reversedString = strand[::-1]
    complementString = ""
    for i in reversedString:
        if i == "A":
            complementString = complementString + "T"
        elif i == "T":
            complementString = complementString + "A"
        elif i == "G":
            complementString = complementString + "C"
        elif i == "C":
            complementString = complementString + "G"
    
    return complementString


print(complementStrand("AAAACCCGGT"))