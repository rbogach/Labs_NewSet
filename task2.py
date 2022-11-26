infile = "venv\preproinsulin-seq.txt"
outfile = "venv\sinsulin-seq-clean.txt"

delete_list = [" ", "ORIGIN", "61", "1", "//"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
            line =str(line[0:24])
        fout.write(line)
