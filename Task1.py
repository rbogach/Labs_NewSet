infile = "venv\preproinsulin-seq.txt"
outfile = "venv\preproinsulin-seq-clean.txt"

delete_list = ["ORIGIN", "61", "1", "//"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
