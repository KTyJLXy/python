def proteins(strand):
    #Variables
    DNAdict = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 
               'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 
               'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP', 
               'UGA': 'STOP'}
    
    proteins_list = []
    
    if isinstance(strand, str):
        for protein in cutstr(strand, 3):
            if ((protein == 'UAA') or (protein == 'UAG') or (protein == 'UGA')):
                return proteins_list
            else: proteins_list.append(DNAdict.get(protein, None))
    elif isinstance(strand, list):
        for codon in strand:
            if ((codon == 'UAA') or (codon == 'UAG') or (codon == 'UGA')):
                return proteins_list
            else: proteins_list.append(DNAdict.get(codon, None))
    else:
        return proteins_list

def cutstr(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]