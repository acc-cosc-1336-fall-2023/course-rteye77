#
def get_hamming_distance(dna1,dna2):
    dist = 0
    for i in range(0, len(dna1)):
        if dna1[i] != dna2[i]:
            dist = dist + 1
    return dist

def get_dna_complement(dna):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    dna_reverse = dna[::-1]
    complement = ""
    for strand in dna_reverse:
        complement += complements[strand]
    return complement
