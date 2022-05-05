#!/bin/bash
#SBATCH --cpus-per-task=18

module load boost
module load python3/3.5.0

python3 /data/kelley/projects/programs/busco/scripts/run_BUSCO.py \
-i <assembly_path> \
-o <output_title> \
-l /data/kelley/projects/programs/busco/actinopterygii_odb9 \
-m genome