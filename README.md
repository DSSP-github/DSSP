README for DSSP
===
DSSP is a system for splice site prediction using deep neural networks.

INSTALL
===
DSSP is implemented in [Python] (https://www.python.org) (3.5.2). We recommend you to install [Anaconda] (https://www.continuum.io) since it contains a lot of dependencies for data processing and scientific computing.

Required
---
Keras must be installed to run our program. 
* [Keras] (https://keras.io). It is a library for deep neural networks. We recommend Keras 2.0.5 since different versions may cause unexpected errors.
* Several modules may be required for using Keras. Please read the official documentations.

USAGE
===
Download all into your favorite directory. 
Select a program file in accordance with the type of splice sites (donor site: 'DS_DSSP.py', acceptor site: 'AS_DSSP.py').
An input argument must be a text of 140 bases of which 69-70th characters are 'GT' for donor site prediction and 71-72th characters are 'AG' for acceptor site prediction.
It returns the probability that the input sequence is a splice site.

LICENSE
===
The souce code can be modified without notice.
DSSP is freely available for non-commercial use. If you are planning on using DSSP in a commercial application, please contact us.  
No claim of suitability, guarantee, or any warranty whatever happens.
