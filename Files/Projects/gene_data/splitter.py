import csv
import argparse

from assign import my_io

def create_data(filename, mode = 'r'):
    with open(filename, mode, newline='') as file:

        genes = csv.reader(file, delimiter = '\t')
        # gene_data = {
        #     'Gene_Symbol' : [],
        #     'Gene_Description' : [],
        #     'Gene_Category' : []
        # }

        # '''
        #     Wrong...Just grabbing the key as symbol and desc as value
        # '''

        # Works
        gene_data = {}
        next(genes)

        for gene in genes:
            symbol = gene[0].lower()
            desc = gene[1].lower()
            gene_data[symbol] = desc 

            # print(symbol)
            # print(desc)

    return gene_data

create_data('chr21_genes.txt')

# print(gene_data['Gene_Symbol'][:10])
# print(type(gene_data['Gene_Symbol']))

def main():

    parser = argparse.ArgumentParser(description='The tin..')

    parser.add_argument('--infile', required=False, default='./chr21_genes.txt')
    args = parser.parse_args()

    filename = args.infile
    print(filename)

    gene_data = create_data(filename)

    while True:
        print('Enter gene symbol or exit to quit....')
        gene = input('Enter the gene: ').lower()

        if gene in gene_data:

            print('Gene found: ', gene)
            print('Desc: ', gene_data[gene])
            break

        elif gene == 'quit':
            break

        else:
            print('No such gene found!!!')


main()

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and ask user for a gene name')

#     # parser.add_argument('filename', )
#     parser.add_argument('-i', '--infile',  help='Path to File to Open',
#         required=False, default='./chr21_genes.txt' #..
#     )

#     args = parser.parse_args()

#     get_file(args.infile)








