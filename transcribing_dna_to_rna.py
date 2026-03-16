sample = "GATGGAACTTGACTACGTAAATT"

rnaSample = ""

for i in sample:
    if i == "T":
        rnaSample = rnaSample + "U"
    else:
        rnaSample = rnaSample + i

