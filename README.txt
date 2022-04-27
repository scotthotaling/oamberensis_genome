##### README #####

Hotaling et al. (2022) Pathways to polar adaptation in fishes revealed by long-read sequencing

# Files
"GFF" - hosted on Zenodo at: 10.5281/zenodo.6494764

“RM_output_parser.py" - Python script that parses RepeatMasker output .tbl files. Requires accession_key_custom.txt and .tbl files to be present in the same directory

“accession_key_custom.txt" - List with each assembly named required by RM_output_parser.py

"loop2.sh" - Bash script used to run RM_output_parser.py in a loop through all .tbl files in the directory

“RepeatBarPlots.R" - R script that takes output from RM_output_parser.py and generates stacked bar plots in Fig. 2a and 2b.

*.tbl [multiple files] - RepeatMasker output table files summarizing repeat content of ten study species that are parsed by RM_ouptut_parser.py
