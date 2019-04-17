# -*- coding: utf-8 -*-

import os
import sys
import argparse
import numpy as np
from keras.models import model_from_json

BASE_KEY = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'N': 4}


def check_input(input_seq):
    print(type(input_seq))
    if not type(input_seq) == str:
        print('The input must be a string.')
        sys.exit(1)
    if not len(input_seq) == 140:
        print('The sequence should be 140-mer.')
    if not input_seq[68:70] == 'AG':
        print('The position of 69 and 70 should be "AG".')


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description='Receive a single 140-mer base sequence, and return the acceptor site probability.')
    if len(argv) != 2:
        parser.parse_args(['-h'])
    parser.add_argument('sequence')
    args = parser.parse_args()
    input_seq = args.sequence
    check_input(input_seq)
    input_vec = np.zeros((1, 140, 5))
    for i in range(len(input_seq)):
        try:
            input_vec[0][i][BASE_KEY[input_seq[i]]] = 1
        except KeyError:
            print('Each base must be "A", "C", "G", "T", or "N"')
            sys.exit(1)
    model = model_from_json(open(os.path.join(os.path.dirname(__file__), 'AS_model.json')).read())
    model.load_weights(os.path.join(os.path.dirname(__file__), 'AS_model.hdf5'))
    predict = model.predict(input_vec, batch_size=1, verbose=0)
    print ('Acceptor site probability: {}'.format(predict[0][0]))


if __name__ == '__main__':
    main()
