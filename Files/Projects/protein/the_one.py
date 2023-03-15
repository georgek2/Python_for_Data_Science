

def splitter(filename, mode='r'):

    with open(str(filename), str(mode)) as file:

        data = file.readlines()

        new_data = data[:24].copy()

    sq_starts = []
    ss_starts = []
    for index, line in enumerate(new_data):
        # the_index = index
        if line.startswith('>') and 'sequence' in line:
            # print(line)
            sq_starts.append(index)
        elif line.startswith('>') and 'secstr' in line:
            # print(line)
            ss_starts.append(index)

    # print(sq_starts)
    # print(ss_starts)
    for i, j in zip(sq_starts, ss_starts):
        
        sq_lines = new_data[i:j]
        with open('pdb_protein.fasta', 'a') as ss_file:

            ss_file.writelines(sq_lines)

    for j, i in zip(ss_starts, sq_starts[1:]):
        if i != sq_starts[-1]:
            ss_lines = new_data[j:i]
            with open('pdb_ss.fasta', 'a') as ss_file:

                ss_file.writelines(ss_lines)
        else:
            # pair1 = (j, i)
            # print(pair1)
            ss_lines = new_data[j:i]
            with open('pdb_ss.fasta', 'a') as ss_file:

                ss_file.writelines(ss_lines)
            # print(ss_lines)
            # pair2 = (ss_starts[-1], -1)
            # print(pair2)
            ss_lines = new_data[ss_starts[-1]:]
            with open('pdb_ss.fasta', 'a') as ss_file:

                ss_file.writelines(ss_lines)

            # print(ss_lines)
            break

    print(f'Found {len(sq_starts)} protein sequences')
    print(f'Found {len(ss_starts)} ss sequences')


print(splitter('mine.txt'))