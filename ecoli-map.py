from Bio import SeqIO
import re
import matplotlib.pyplot as plt

fasta_file = "Ecoli_fragment.fasta"
record = next(SeqIO.parse(fasta_file,"fasta"))

seq_str = str(record.seq[:10000]).upper()

restriction_sites = {
"EcoRI": "GAATTC",
"BamHI": "GGATCC",
"PstI": "AAGCTT",
"XhoI": "CTCGAG",
}

enzyme_positions = {}
for enzyme, site in restriction_sites.items():
    positions = [m.start()+1 for m in re.finditer(site,seq_str)]
    if positions:
        enzyme_positions[enzyme] = positions
    print (f"{enzyme}: found {len(positions)} sites")

plt.figure(figsize=(10,3))
plt.axhline(y=0, color='black', linewidth=1)
colors = ['red', 'blue', 'green', 'orange', 'purple']
y_offset = 0.2 

y=1
plt.plot([0,len(seq_str)],[y,y],color="black",linewidth = 2)
colors = ["red","blue","green","orange","purple"]

for (enzyme,positions), color in zip(enzyme_positions.items(),colors):
    y=0
    for pos in positions:      
        plt.plot(pos,y,marker="|",color=color,markersize=12)
    if positions:
        plt.text(positions[0],y+y_offset,enzyme,color=color,fontsize=8,rotation=45)
plt.title("Restriction enzyme Map (first 10000 bp of E.coli K12)")
plt.xlabel("Genome position(bp)")
plt.yticks ([])
plt.xlim(0,10000)
plt.tight_layout()
plt.show()