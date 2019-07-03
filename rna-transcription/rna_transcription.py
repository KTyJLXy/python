def to_rna(dna_strand):
    #Vars
    Translation = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    RNA = []
    
    if len(dna_strand) == 0:
        return ""
    else:   
        for nucleotide in dna_strand:
            if nucleotide in Translation:
                RNA += Translation[nucleotide]
                
    return ''.join(RNA)
