#Parses repeatmasker output tables and writes files formatted for plotting in R with the RepeatBarPlots.R script
#run in the same directory as repeatmasker .tbl files with the accession_key_custom.txt file also present
#in accession_key_custom.txt, first column is sample name that will appear in plot. Second column is assembly name that is listed at the top the .tbl files
import sys

table_filename = sys.argv[1]
outfilename = sys.argv[2]
tandem_repeats = [0, 0.0]
other_repeats = [0,0.0]
accession_key = {}

#the file opened below needs to be in the same directory as tables being parsed by this script
with open("accession_key_custom.txt") as key:
    for line in key:
        new_line = line.split()
        #print(new_line)
        accession_key[new_line[1]] = new_line[0]

repeat_dict = {}
with open(table_filename) as table_file:
    for line in table_file:
        if "total length:" in line:
            new_line = line.split()
            total_bps = new_line[2]
            tot_length = int(total_bps)
        elif "bases masked:" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[2])
            bases_masked = [total_bps, percent]
        elif "file" in line:
            taxon_accession = line.split()[2]
            taxon = accession_key[taxon_accession]
        elif "LINEs:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            lines = [total_bps, percent]
        elif "SINEs:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            sines = [total_bps, percent]
        elif "LTR elements:" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[3])
            ltrs = [total_bps, percent]
        elif "DNA elements" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[3])
            transposons = [total_bps, percent]
        elif "Satellites:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            satellites = [total_bps, percent]
            #tandem_repeats[0] += int(new_line[2])
            #tandem_repeats[1] += float(new_line[4])/100
        elif "Simple repeats:" in line:
            new_line = line.split()
            #percent = float(new_line[5])/100
            #total_bps = int(new_line[3])
            #simple_repeats = [total_bps, percent]
            other_repeats[0] += int(new_line[3])
            other_repeats[1] += float(new_line[5])/100
        elif "Low complexity:" in line:
            new_line = line.split()
            #percent = float(new_line[5])/100
            #total_bps = int(new_line[3])
            #low_complexity = [total_bps, percent]
            other_repeats[0] += int(new_line[3])
            other_repeats[1] += float(new_line[5])/100
        elif "Penelope" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            penelope = [total_bps, percent]
            #other_repeats[0] += int(new_line[2])
            #other_repeats[1] += float(new_line[4])/100
        elif "Rolling-circles" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            rolling_circles = [total_bps, percent]
            #other_repeats[0] += int(new_line[2])
            #other_repeats[1] += float(new_line[4])/100
        elif "Small RNA:" in line:
            new_line = line.split()
            other_repeats[0] += int(new_line[3])
            other_repeats[1] += float(new_line[5])/100
        elif "Unclassified:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            unclassified = [total_bps, percent]
        elif "L2/CR1/Rex" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            l2_cr1_rex = [total_bps, percent]
        elif "R1/LOA/Jockey" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            r1_loa_jockey = [total_bps, percent]
        elif "R2/R4/NeSL" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            r2_r4_nesl = [total_bps, percent]
        elif "RTE/Bov-B" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            rte_bov_b = [total_bps, percent]
        elif "L1/CIN4" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            l1_cin4 = [total_bps, percent]
        elif "CRE/SLACS" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            cre_slacs = [total_bps, percent]
        elif "BEL/Pao" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            bel_pao = [total_bps, percent]
        elif "Ty1/Copia" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            ty1_copia = [total_bps, percent]
        elif "Gypsy/DIRS1" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            gypsy_dirs1 = [total_bps, percent]
        elif "hobo-Activator" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            hobo_activator = [total_bps, percent]
        elif "Tc1-IS630-Pogo" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            tc1_is630_pogo = [total_bps, percent]
        elif "En-Spm" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            en_spm = [total_bps, percent]
        elif "MuDR-IS905" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            mudr_is905 = [total_bps, percent]
        elif "PiggyBac" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            piggybac = [total_bps, percent]
        elif "Tourist/Harbinger" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            tourist_harbinger = [total_bps, percent]
        elif "Other (Mirage," in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[2])
            mirage_p_element_transib = [total_bps, percent]
        #added to simplify calculation of total categorized repeats (which is different than total bases masked)
        elif "Total interspersed repeats" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[3])
            total_interspersed = [total_bps, percent]

total_reps = other_repeats[0]+tandem_repeats[0]+sines[0]+lines[0]+ltrs[0]+transposons[0]+unclassified[0]
#print(total_reps)

with open(outfilename, "a") as outfile:
    outfile.write(taxon + "\t" + str(lines[0]) + "\t" + str(lines[1]) + 
            "\tz_LINEs\n" +
        taxon + "\t" + str(sines[0]) + "\t" + str(sines[1]) + "\tx_SINEs\n" +
        taxon + "\t" + str(ltrs[0]) + "\t" + str(ltrs[1]) + "\ty_LTRs\n" +
        taxon + "\t" + str(transposons[0]) + "\t" + str(transposons[1]) + 
            "\tw_DNA_transposons\n" +
        taxon + "\t" + str(satellites[0]) + "\t" + str(satellites[1]) + 
            "\tt_satellites\n" +
        taxon + "\t" + str(other_repeats[0]) + "\t" + str(other_repeats[1]) + 
            "\ts_Other_repeats\n" +
        taxon + "\t" + str(unclassified[0]) + "\t" + str(unclassified[1]) + 
            "\tr_Unclassified_repeats\n" +
        taxon + "\t" + str(tot_length - int(bases_masked[0])) + "\t" + 
            str((tot_length - int(bases_masked[0]))/float(tot_length)) + 
            "\tq_Unique_low_repeat\n")


#New block that leaves unique out and calculates a proportion of total repeats for each category and not the total bases in the whole assembly
with open("prop_repeat_families.txt", "a") as prop_outfile:
    prop_outfile.write(taxon + "\t" + str(lines[0]) + "\t" + str((lines[0])/(total_reps)) + 
            "\tLINEs\n" +
        taxon + "\t" + str(sines[0]) + "\t" + str((sines[0])/(total_reps)) + "\tSINEs\n" +
        taxon + "\t" + str(ltrs[0]) + "\t" + str((ltrs[0])/(total_reps)) + "\tLTRs\n" +
        taxon + "\t" + str(transposons[0]) + "\t" + str((transposons[0])/(total_reps)) + 
            "\tDNA_transposons\n" +
        taxon + "\t" + str(tandem_repeats[0]) + "\t" + str((tandem_repeats[0])/(total_reps)) + 
            "\ttandem_repeats\n" +
        taxon + "\t" + str(other_repeats[0]) + "\t" + str((other_repeats[0])/(total_reps)) + 
            "\tOther_repeats\n" +
        taxon + "\t" + str(unclassified[0]) + "\t" + str((unclassified[0])/(total_reps)) + 
            "\tUnclassified_repeats\n") #+
        #taxon + "\t" + str(tot_length - int(total_reps)) + "\t" + 
            #str((tot_length - int(bases_masked[0]))/float(tot_length)) + 
            #"\tUnique_low_repeat\n")

