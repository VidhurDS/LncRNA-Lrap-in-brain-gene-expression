array = ["KO_WT", "KO_HET", "WT_HET"]
file_names = {"KO": "KO_bams.txt",
              "WT": "WT_bams.txt",
              "HET": "HET_bams.txt"}

key_arr =[]
for hour in [6,12,24]:
    for combo in array:
        key_str = combo + "_" + str(hour)
        b1, b2 = combo.split("_")
        key_arr.append(key_str)
        with open("scripts/" + str(key_str) + "_rmats.sh", "w") as f:
            print>> f, """#!/bin/bash
#PBS -M swapdaul@iu.edu
#PBS -l nodes=1:ppn=16,walltime=0:%s:0:00
#PBS -l vmem=128gb
#PBS -m abe
#PBS -N %s
#PBS -j oe

module load rmats/4.0.2

cd /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/4.rmats_analysis
python /geode2/soft/hps/rhel7/rmats/4.0.2/rMATS-turbo-Linux-UCS2/rmats.py --b1 %s --b2 %s --gtf /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/3.alignment/lncKO_merged_wEnsembl.annotated.gtf --od %s -t paired --nthread 1 --readLength 101

""" % (str(hour), key_str, file_names[b1], file_names[b2], key_str)

key_arr = set(key_arr)
k = open("qsub_rMATS_code.txt", "w")

for i in key_arr:
    i = i.strip()
    k.write("dos2unix %s_rmats.sh\n" % (str(i)))

for i in key_arr:
    i = i.strip()
    k.write("qsub %s_rmats.sh\n" % (str(i)))

