with open('mine.txt', 'r') as file:

    data = file.readlines()

    new_data = data[:48].copy()

    sq_starts = []
    ss_starts = []
    for index, line in enumerate(new_data):
        the_index = index
        if line.startswith('>') and 'sequence' in line:
            # print(line)
            sq_starts.append(index)
        elif line.startswith('>') and 'secstr' in line:
            # print(line)
            ss_starts.append(index)

    print(sq_starts)
    print(ss_starts)
    for i, j in zip(sq_starts, ss_starts):
        
        sq_lines = new_data[i:j]
        with open('pdb_protein.fasta', 'a') as ss_file:

            ss_file.writelines(sq_lines)

    for j, i in zip(ss_starts, sq_starts[1:]):
        if i == sq_starts[-1]:
            ss_lines = new_data[j:]
            with open('pdb_ss.fasta', 'a') as ss_file:

                ss_file.writelines(ss_lines)
        else:
            ss_lines = new_data[j:i]
            with open('pdb_ss.fasta', 'a') as ss_file:

                ss_file.writelines(ss_lines)










