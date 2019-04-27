# -*- coding: utf-8 -*-

import os
import sys
import argparse
import numpy as np
from keras.models import model_from_json

BASE_KEY = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'N': 4}


def check_input(input_seq):

    if not type(input_seq) == str:
        print('The input must be a string.')
        sys.exit(1)

    if not len(input_seq) == 140:
        print('The sequence should be 140-mer.')

    if not input_seq[70:72] == 'GT':
        print('The position of 71 and 72 should be "AG".')


def DS_DSSP(input_seq):
    
    check_input(input_seq)
    
    input_vec = np.zeros((1, 140, 5))
    for i in range(len(input_seq)):
        try:
            input_vec[0][i][BASE_KEY[input_seq[i]]] = 1
        except KeyError:
            print('Each base must be "A", "C", "G", "T", or "N"')
            sys.exit(1)
            
    model = model_from_json(open(os.path.join(os.path.dirname(__file__), 'DS_model.json')).read())
    model.load_weights(os.path.join(os.path.dirname(__file__), 'DS_model.hdf5'))

    predict = model.predict(input_vec, batch_size=1, verbose=0)[0, 0]
    
    print ('Donor site probability: {}'.format(predict))

    return predict


def main(argv=sys.argv):

    parser = argparse.ArgumentParser(description='Receive a single 140-mer base sequence string or FASTA file.')

    if len(argv) == 1:
        parser.parse_args(['-h'])

    parser.add_argument('-I', '--input', required=True, help='140-mer base sequece string, or FASTA file')
    parser.add_argument('-O', '--output', required=False, help='path to the output file')

    args = parser.parse_args()

    if os.path.isfile(args.input):
        input_file = args.input
        print(input_file)
        print(os.path.split(input_file)[1])
        if args.output:
            fn_o = args.output
        else:
            fn_o = 'result_' + os.path.splitext(input_file)[0] + '.txt'

        f_i = open(input_file, mode='r')
        f_o = open(fn_o, mode='w')
        line = f_i.readline()
        while line:
            if line[0] == '>':
                f_o.write(line)
                input_seq = f_i.readline().rstrip()
                predict = DS_DSSP(input_seq)
                f_o.write(str(predict)+'\n')
            else:
                f_i.close()
                f_o.close()
                sys.exit(1)
            line = f_i.readline()
        f_i.close()
        f_o.close()
    
    else:
        input_seq = args.input       
        predict = DS_DSSP(input_seq)
        if args.output:
            with open(args.output, mode='w') as f_o:
                f_o.write(str(predict))


if __name__ == '__main__':
    main()
