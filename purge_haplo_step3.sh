#!/bin/bash
#SBATCH --cpus-per-task=20

# organize environment
module load anaconda3
source activate purge_haplotigs_env
	
# run the program								
purge_haplotigs  purge -g <input_assembly> -c <*stats.csv_file> -t 20 -o <purged_assembly_output.fa>
