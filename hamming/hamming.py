def distance(strand_a, strand_b):
        if len(strand_a) != len(strand_b):
            raise ValueError('Strands are not of equal length')
        diffs = 0
        for ch1, ch2 in zip(strand_a, strand_b):
                if ch1 != ch2:
                        diffs += 1
        return diffs
