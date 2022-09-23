#!/bin/bash
#PBS -M swapdaul@iu.edu
#PBS -l nodes=1:ppn=16,walltime=0:10:0:00
#PBS -l vmem=16gb
#PBS -m abe
#PBS -N HET-1_alignment
#PBS -j oe


module load samtools/1.9
module load hisat2/2.1.0

cd /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/3.alignment
hisat2 --rna-strandness RF --dta -q -p 16 -x /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/3.alignment/rn6_HISAT2_index/rn6/genome -1 /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/1.Data/raw_fastqs/Riken-M-HET-1-naive-brain-total-RNA-cDNA_TCCGCGAA_L003_R1_001.fastq -2 /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/1.Data/raw_fastqs/Riken-M-HET-1-naive-brain-total-RNA-cDNA_TCCGCGAA_L003_R2_001.fastq -S HET-1.sam
samtools view -S -b HET-1.sam > HET-1.bam
samtools sort HET-1.bam HET-1.sorted
samtools index HET-1.sorted.bam


