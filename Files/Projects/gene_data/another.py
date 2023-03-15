import argparse


"""
    Just get the command line options using argparse
    @return: Instance of argparse arguments
"""
parser = argparse.ArgumentParser(description='Open chr21_genes.txt, \
and ask user for a gene name')

parser.add_argument('-i', '--infile', dest='infile',
    type=str, help='Path to the file to open',
    required=False, default='./chr21_genes.txt')

print(parser.parse_args()['infile'])


