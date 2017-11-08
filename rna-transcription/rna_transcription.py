'''Given a DNA strand, its transcribed RNA strand is formed by replacing
each nucleotide with its complement:

* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`

Your function will need to be able to handle invalid inputs by raising a
`ValueError` with a meaningful message.'''

import re


def to_rna(dna_strand):
    valid_input = ['G', 'C', 'T', 'A']
    coding = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'}
    rna_strand = ''
    for x in dna_strand:
        if x not in valid_input:
            raise ValueError('Invalid dna strand')


    for char in dna_strand:
        rna_strand += coding[char]
    return rna_strand

