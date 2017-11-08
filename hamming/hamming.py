def distance(strand_a, strand_b):
    hamming_distance = 0
    if len(strand_a) == len(strand_b):
        for x in range(0, len(strand_a)):
            if strand_a[x] != strand_b[x]:
                hamming_distance += 1
        return hamming_distance
    else:
        raise ValueError("strands are not of equal length")


