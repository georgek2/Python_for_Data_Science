

with open('mine.txt', 'r') as file:

    data = file.readlines()

# print(data[:10])

sq_start = []
ss_start = []

new_data = data[:40].copy()

for i, line in enumerate(new_data):

    if line.startswith('>') and 'sequence' in line:
        # print(line)
        sq_start.append(i)

    elif line.startswith('>') and 'secstr' in line:
        # print('>>', line)
        ss_start.append(i)
    
    else:
        continue

print(sq_start)
print(ss_start)

# print(data[sq_start[0]:ss_start[0]])
# print(data[ss_start[0]:sq_start[1]])

for i, j in zip(sq_start, ss_start):
    print(i, j)
    sq_lines = new_data[i:j] 
    print(sq_lines)
    with open('protein.txt', 'a') as file:
        file.writelines(sq_lines)
    print('*'*30)
    
print('------------------------------------')

for i, j in zip(ss_start, sq_start[1:]):
    print(i, j)

    if j != sq_start[-1]:
        ss_lines = new_data[i:j]
        print(ss_lines)
        with open('ss.txt', 'a') as file:
            file.writelines(ss_lines)

    else:
        ss_lines = new_data[i:j]
        print(ss_lines)
        with open('ss.txt', 'a') as file:
            file.writelines(ss_lines)
        print('The last seq_s-string-----')
        print(ss_start[-1], ': rem...' )
        ss_lines = new_data[ss_start[-1]:]
        print(ss_lines)
        with open('ss.txt', 'a') as file:
            file.writelines(ss_lines)
    print('*'*30)

