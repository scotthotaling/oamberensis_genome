###################################
 'O. amberensis Genome Assembly'
   Written by: Scott Hotaling
   Email: scott.hotaling@wsu.edu
###################################

Note: This is not a script. These are bioinformatic notes to aid in reproducing analyses
and/or better understanding the commands/programs used for the study.
 
Where appropriate, corresponding scripts are provided on the GitHub (see list below).

######

'Script/key file list':
	> X - canu_oamberensis_v1B.sh
	> X - busco_Oamber-Pacbio_v2A.sh
	> X - minimap2_Oamber.sh
	> X - purge_haplo_step1.sh
	> X - purge_haplo_step2.sh
	> X - purge_haplo_step3.sh
	> arrow_oamber_v3A.sh
	> maker_opts.ctl
	> maker_Oamber_denovo.sh
	
######

'More info':
1. Organizing the data.

	# A. Unpacking the data.
		tar -xvf wsu-pacbio-20181211.tar.3
		
	# B. Converting BAMs to FASTQ.
		> Use "BAM2fastx" -- https://github.com/PacificBiosciences/bam2fastx

	# C. Combining BAMs with pbmerge
		
		Basic: 
			>> pbmerge -o merged.bam 1.bam 2.bam 3.bam
				

2. Assembling genome with Canu
	'GitHub': https://github.com/marbl/canu
	'Paper': Koren et al. 2017, Genome Research, https://genome.cshlp.org/content/27/5/722
	
	'Script': canu_oamberensis_v1B.sh


3. Assemblathon:
	'Basic command': 
	./assemblathon_stats.pl [assembly path] -csv > [output path]	
		
				
4. BUSCO:							
	'Script': busco_Oamber-Pacbio_v2A.sh


5. De-tigging the duplicates w/ 'purge_haplotigs'.
	# Goal: Remove duplication from the Canu assembly.
	# Website: https://bitbucket.org/mroachawri/purge_haplotigs#markdown-header-citation

	'Scripts
		> Map reads: minimap2_Oamber.sh
		> Purge, step 1: purge_haplo_step1.sh
			'Note': see examples on https://bitbucket.org/mroachawri/purge_haplotigs#markdown-header-running-purge-haplotigs
		> Purge, step 2: purge_haplo_step2.sh
			'Note': Runs fast, does not need script.
		> Purge, step 3: purge_haplo_step3.sh
		

6. Polish assembly w/ 'arrow'.
	# GitHub: https://github.com/PacificBiosciences/GenomicConsensus

	# Basic usage:
				
		module load anaconda3
				
		variantCaller -jn --algorithm=arrow <aligned_reads> -r <reference> -o <variants.gff> -o <output_name.fasta> -o <output_name.fastq> -o <variants.gff>
			# -jn = number of CPUs (n=number i.e. j10 = 10 cpus)
			
	'Script': arrow_oamber_v3A.sh


7. Annotating the genome w/ 'Maker2'
	# Relevant links:
		https://reslp.github.io/blog/My-MAKER-Pipeline/
		http://weatherby.genetics.utah.edu/MAKER/wiki/index.php/MAKER_Tutorial_for_WGS_Assembly_and_Annotation_Winter_School_2018#Getting_Started_with_MAKER	
		https://gist.github.com/darencard/bb1001ac1532dd4225b030cf0cd61ce2
		
	# Performed multiple rounds with example control/script files:
		
		maker_opts.ctl
		maker_Oamber_denovo.sh
		
	# Merging gene models/etc.
	
		Move to output directory...
		
		> Merge all of the GFF3 models together
				
			~/maker/bin/gff3_merge -d ~Oamber_SNAP_master_datastore_index.log
									
		> Convert the GFF3 models to ZFF

			~/maker/bin/maker2zff Oamber_SNAP.all.gff
						
		> Check the new files have been created
						
			genome.ann = ZFF format
			genome.dna = FASTA coordinates for referencing
			
		
