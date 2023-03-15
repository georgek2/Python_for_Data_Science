import argparse
# from assign import my_io

def create_dic(fh_in):
    """
    Create a dictionary to store gene categories + descriptions
    """
    desc = {}
    with open(fh_in, 'r') as file:
        lines = file.readlines()[1:]
    for line in lines:
        gene = line.strip().split("\t")[0].lower()
        description = line.strip().split("\t")[1].lower()
        desc[gene] = description
    return desc

# print(create_dic('chr21_genes.txt'))

def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, \
    and ask user for a gene name')

    parser.add_argument('-i', '--infile', dest='infile',
        type=str, help='Path to the file to open',
        required=False, default='./chr21_genes.txt')

    return parser.parse_args()


def main():
    args = get_cli_args()
    fh_in = args.infile
    desc = create_dic(fh_in)

    while True:
        gene = input('Enter the gene symbol or quit to exit: ')

        if gene in desc:
            print('Gene found...')
            print('Desc: ', desc[gene])
            break
        elif gene == 'quit':
            print('Exited...')
            break
        else:
            print('Not found...')


main()



