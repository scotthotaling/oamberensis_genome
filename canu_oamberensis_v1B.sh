#!/bin/bash
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G
#SBATCH --mail-type=END,FAIL

<path_to_canu_program> \
-s <path_to_parameters_file (see below)> \
-p oamberensis -d <output_path> genomeSize=700m \
-pacbio-raw <input_data>

## Canu parameter file contents (move to a new file)
correctedErrorRate=0.040 cnsErrorRate=0.2500 