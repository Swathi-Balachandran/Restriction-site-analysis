from Bio import SeqIO
import re

fasta_file = "E_coli.fasta"
sequences = list(SeqIO.parse(fasta_file, "fasta"))

for record in sequences:
    print("=" * 120)
    print("ID:", record.id)
    print("Length:", len(record.seq))
    print("Sequence (first 10000 bp):", record.seq[:10000])
    print("=" * 120)

    # GC and AT content
    gc_content = 100 * float(record.seq.count("G") + record.seq.count("C")) / len(record.seq)
    print("GC_content (%):", round(gc_content, 2))
    at_content = 100 * float(record.seq.count("A") + record.seq.count("T")) / len(record.seq)
    print("AT_content (%):", round(at_content, 2))

    # Reverse complement
    print("Reverse complement (first 10 bp):", record.seq.reverse_complement()[:10])

    # Restriction sites
    restriction_sites = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "XhoI": "CTCGAG",
        "PstI": "CTGCAG",
    }

    print("\nRestriction enzyme recognition sites:")
    seq_str = str(record.seq).upper()

    for enzyme, site in restriction_sites.items():
        positions = [m.start() + 1 for m in re.finditer(site, seq_str)]
        print(f"{enzyme} ({site}) → found {len(positions)} sites")

        if positions:
            print(f"First few positions: {positions[:5]} {'...' if len(positions) > 5 else ''}")
        else:
            print(f"{enzyme} ({site}) not found.")

    print("=" * 120)
