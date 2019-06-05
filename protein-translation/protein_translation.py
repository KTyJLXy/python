dnadict = {'AUG': 'Methionine', 
               'UUU': 'Phenylalanine', 
               'UUC': 'Phenylalanine', 
               'UUA': 'Leucine', 
               'UUG': 'Leucine', 
               'UCU': 'Serine', 
               'UCC': 'Serine', 
               'UCA': 'Serine', 
               'UCG': 'Serine', 
               'UAU': 'Tyrosine', 
               'UAC': 'Tyrosine', 
               'UGU': 'Cysteine', 
               'UGC': 'Cysteine', 
               'UGG': 'Tryptophan', 
               'UAA': 'STOP', 
               'UAG': 'STOP', 
               'UGA': 'STOP'
              }

def of_codon(codon):
    return dnadict.get(codon, None)

def proteins(strand):
    
    proteins_list = []
    
    l = len(strand)

    for x in range(0, l, 3):
        rna = strand[x: x + 3]
        codon = of_codon(rna)
        if codon:
            if codon == "STOP":
                break
            proteins_list.append(codon)
        else:
            raise ValueError("Invalid protein")
    
    return proteins_list
