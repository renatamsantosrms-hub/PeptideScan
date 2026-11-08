def amino_acid_count(sequence, amino_acid):
    """Conta quantas vezes um determinado aminoácido aparece na sequência."""
    return sequence.upper().count(amino_acid.upper())

def contains_amino_acids(sequence, amino_acids):
    """Verifica se a sequência contém pelo menos um dos aminoácidos informados."""
    sequence = sequence.upper()
    return any(aa.upper() in sequence for aa in amino_acids)