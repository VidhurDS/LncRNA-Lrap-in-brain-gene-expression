#!/bin/bash
#PBS -M swapdaul@iu.edu
#PBS -l nodes=1:ppn=16,walltime=0:24:0:00
#PBS -l vmem=128gb
#PBS -m abe
#PBS -N KO_HET_24
#PBS -j oe

module load rmats/4.0.2

cd /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/4.rmats_analysis
python /geode2/soft/hps/rhel7/rmats/4.0.2/rMATS-turbo-Linux-UCS2/rmats.py --b1 KO_bams.txt --b2 HET_bams.txt --gtf /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/3.alignment/lncKO_merged_wEnsembl.annotated.gtf --od KO_HET_24 -t paired --nthread 1 --readLength 101


