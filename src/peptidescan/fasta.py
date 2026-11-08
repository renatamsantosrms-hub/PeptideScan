from Bio import SeqIO

def read_fasta(file_path):
    """Lê um arquivo FASTA e retorna ID, descrição e sequência."""
    records = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = str(record.seq).upper()
        records.append({
            "id": record.id,
            "description": record.description,
            "sequence": sequence
        })
    return records
