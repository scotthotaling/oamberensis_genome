#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --mem=124G

module load anaconda3
					
<path_to_minimap> -ax map-pb \
<assembly_path> \
<input_data> \
| samtools view -hF 256 - \
| samtools sort -@ 8 -m 1G -o <output.bam> -T <temp_file>