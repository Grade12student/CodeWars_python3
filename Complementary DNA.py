def DNA_strand(dna):
    dna = dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    return dna.upper()

    # code here