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
Download all files into your favorite directory.   
Select a program file according to the type of splice site (donor site: “DS_DSSP.py,” acceptor site: “AS_DSSP.py”).  
An input argument must be a text of 140 bases, of which characters 71 and 72 are “GT” for donor site prediction and characters 69 and 70 are “AG” for acceptor site prediction.  
The probability that the input sequence is a splice site will be generated.

LICENSE
===
The souce code can be modified without notice.
DSSP is freely available for non-commercial use. If you are planning on using DSSP in a commercial application, please contact us.  
No claim of suitability, guarantee, or any warranty whatever happens.
