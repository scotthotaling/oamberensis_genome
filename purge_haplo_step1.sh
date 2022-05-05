#!/bin/bash
#SBATCH --cpus-per-task=20

# organize environment
module load anaconda3
source activate purge_haplotigs_env

# run the program						
purge_haplotigs readhist -b <aligned.bam> -g <assembly_path> -t 20