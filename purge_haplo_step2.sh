#!/bin/bash
#SBATCH --cpus-per-task=20

# organize environment
module load anaconda3
source activate purge_haplotigs_env

# run the program						
purge_haplotigs contigcov -i <*.gencov_file_from_step_1> -l 10 -m 140 -h 195 -o <output_stats_file> -j 80 -s 80