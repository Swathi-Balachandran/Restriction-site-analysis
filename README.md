# FASTA and Restriction-site-analysis
This is a mini project that performs the FASTA sequence analyses the genome of Escherichia coli strain K-12 and determines the restriction sites.

# FASTA analysis:
In this project, I worked with the complete genome of E coli K-12 downloaded in FASTA format from NCBI.
- Using Python and Biopython, displayed the genome ID, sequence length and calculated the AT and GC content for the first 10,000 bp.

# Restriction enzyme analysis:
- A list of common restriction enzymes was created.
- Identified the number of restriction sites of the enzymes and their positions (first 10,000 bp).

# Visualization of the restriction site map:
- Using ApE- A plasmid editor, a restriction map of the genome (first 10,000 bp) was created along with a list of the restriction enzymes.
- NEB Cutter was also used to visualize the restriction sites of the whole genome 

*Note:* 
- .py files can be opened using Notepad
- The first 10,000 bp were selected to avoid flooding of the window and ease of use for ApE.

# Files available:
- E_coli.fasta : the fasta sequence of the whole genome of E_coli K-12
- E_coli fragment.fasta : contains the first 10,000 bp for the convinience of the project
- fasta_2.py : the python script in .txt format
- Escherichia coli str. K-12 NEBCutter : the map of restriction sites (Due to the volume of data, some of the sites were not displayed)
- E_coli fragment restriction map.pdf : the map of restriction sites of the first 10,000 bp generated using ApE
- E_coli list of enzymes ApE.txt : a list of restriction enzymes that could digest the genome

# Tools used:
- Python and biopython to parse the sequences.
- Microsoft Powershell to run the python script.
- ApE and NEB Cutter (free bioinformatics tools; ApE requires installation) to visulaize the restriction sites
