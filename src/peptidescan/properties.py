from pyteomics import mass

def calculate_length(sequence):
    """Calcula o tamanho da sequência."""
    return len(sequence.upper())

def calculate_molecular_mass(sequence):
    """Calcula a massa monoisotópica em Da."""
    return mass.calculate_mass(sequence=sequence.upper())