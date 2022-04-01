#!/bin/bash

#run this script in the same folder as accession_key_custom.txt, RM_output_parser.py, and
#the .tbl files for each species to generate input files for plotting in R

for i in *tbl 
do 
	python RM_table_parser_families_mod4.py $i repeatmasker_results_custom.txt 
done