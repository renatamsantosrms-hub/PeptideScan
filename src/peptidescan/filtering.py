from .properties import calculate_length, calculate_molecular_mass

def filter_peptides(sequences, min_length=None, max_length=None, min_mass=None, max_mass=None):
    """Filtra peptídeos com base em limites de comprimento e massa molecular."""
    results = []
    for item in sequences:
        seq = item["sequence"] if isinstance(item, dict) else item
        length = calculate_length(seq)
        mass_val = calculate_molecular_mass(seq)
        
        if min_length is not None and length < min_length:
            continue
        if max_length is not None and length > max_length:
            continue
        if min_mass is not None and mass_val < min_mass:
            continue
        if max_mass is not None and mass_val > max_mass:
            continue
            
        results.append({
            "sequence": seq,
            "length": length,
            "mass": mass_val
        })
    return results