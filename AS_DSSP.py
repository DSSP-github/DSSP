# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
from keras.models import model_from_json

base_dir = os.path.dirname(os.path.abspath(__file__))

model = model_from_json(open(os.path.join(base_dir, 'AS_model.json')).read())
model.load_weights(os.path.join(base_dir, 'AS_model.hdf5'))

base_key = {'A':0, 'C':1, 'G':2, 'T':3, 'N': 4}

input_seq = sys.argv[1]
print (input_seq)
input_vec = np.zeros((len(input_seq), 5))
for i in range(len(input_seq)):
    input_vec[i][base_key[input_seq[i]]] = 1
input_vec = np.array(input_vec).reshape(1, 140, 5)

predict = model.predict(input_vec, batch_size = 1, verbose = 0)

print ('the probability of acceptor site: {}'.format(predict[0][0]))