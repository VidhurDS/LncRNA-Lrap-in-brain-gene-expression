out_file = open("JC_FDR_all_Combo_events.txt", "a")
out_file_2 = open("JCEC_FDR_all_Combo_events.txt", "a")
AS_events = ["SE", "RI", "MXE", "A5SS","A3SS"]
out_file.write("JC_events_FDR_0.05\t"+"\t".join(AS_events)+ "\n")
out_file_2.write("JCEC_events_FDR_0.05\t"+"\t".join(AS_events)+ "\n")
# take in folder name
fn_list = ["KO_WT", "KO_HET", "WT_HET"]

# function to take in an array and filter by p-val (18)/FDR (19) (argument), return number of events


def filter_lines(in_arr, val, MXE):
    if val == 1:
        index = 19
    else:
        index = 18

    if MXE : index += 1

    e_count = 0
    for line in in_arr:
        line = line.strip()
        ele = line.split("\t")
        if float(ele[index]) <= 0.05:
            e_count += 1
    return e_count


# loop over all types of files

for fn in fn_list:
    jc_dict = {}
    jcec_dict = {}
    # A3SS.MATS.JC.txt
    out_str = fn
    out_str_2 = fn

    for ase in AS_events:
        if ase == "MXE": m = 1
        else: m = 0

        for out_type in ["JC", "JCEC"]:
            file_name = ase + ".MATS." + out_type + ".txt"
            file_path = fn + "/" + file_name
            f = open(file_path, 'r')
            x = f.readlines()[1:] #skipping header
            f.close()
            num = filter_lines(x, 1, m)

            if out_type == "JC":
                jc_dict[ase] = num
            else:
                jcec_dict[ase] = num
        out_str = out_str + "\t" + str(jc_dict[ase])
        out_str_2 = out_str_2 + "\t" + str(jcec_dict[ase])

    out_file.write(out_str + "\n")
    out_file_2.write(out_str_2 + "\n")

# send each file to function and feed into dictionary
# use 1 for FDR filter, 0 for pval filter of less than equal to 0.05
# print dictionary as matrix

# each comparison two matrices
