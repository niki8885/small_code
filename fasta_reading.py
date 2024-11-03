try:
    f = open("sequence.fasta")
except IOError:
    print("File not found")
    exit(1)


seqs = {}
name = None

for line in f:
    line = line.rstrip()
    if not line:
        continue
    if line[0] == '>':
        words = line.split()
        name = words[0][1:]
        seqs[name] = ''
    else:
        seqs[name] += line

print(seqs)