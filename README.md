README for DSSP
===
DSSP is a system for splice site prediction using deep neural networks, as described in [Naito T. *J Comput Biol*. 2018;25(8):954–61](https://www.liebertpub.com/doi/pdfplus/10.1089/cmb.2018.0041).  
  
INSTALL
===
DSSP is implemented in [Python](https://www.python.org) (3.5.2). We recommend you to install [Anaconda](https://www.continuum.io) since it contains a lot of dependencies for data processing and scientific computing.

Required
---
Keras must be installed to run our program. 
* [Keras](https://keras.io/). It is a library for deep neural networks. We recommend Keras 2.0.5 since different versions may cause unexpected errors.
* Several modules may be required for using Keras. Please read the official documentations.
  
USAGE
===
* Download all files into your favorite directory. 
* Select a program file according to the type of splice site (donor site: “DS_DSSP.py,” acceptor site: “AS_DSSP.py”).  
* The required input is a 140-mer base sequence with the consensus sequence (i.e., ‘‘GT’’ and ‘‘AG’’ for the donor and acceptor sites, respectively) in the middle. 
* It returns the probability that the input sequence is a splice site.
  
Sample
===
Donor site.
---
* An input for donor site should be a 140-mer strings with the GT at positions 71 and 72.  
```
$ python DS_DSSP.py 
CTCCTCTTTGCCTTACTCCTAGCCATGGAGCTCCCATTGGTGGCAGCCAGTGCCACCATGCGCGCTCAGTGTAAGTATCATTCCCTCTCACTG
TCCTGGAGAGGACGAGAATTCCACCTGGGGTGCTGGGGGTCACTGGG
```
* Result:
```bash
Donor site probability: 0.9999337196350098
```

Acceptor site.
---
* An input for acceptor site should be a 140-mer strings with the AG at positions 69 and 70.  
```
$ python AS_DSSP.py 
GGCCAGGGGCATAGAGCTGGCCAAGGAGCCATGGCTCACTAACGTGTTGTATGGGGCTCCTTCCCTTCAGGTCCAGGCTCCTGCGTGAAGTGA
TGCTCCTCTTTGCCTTACTCCTAGCCATGGAGCTCCCATTGGTGGCA
```
* Result:
```bash
Acceptor site probability:: 0.9931520223617554
```
  
LICENSE
===
* The souce code can be modified without notice.
* DSSP is freely available for non-commercial use. If you are planning on using DSSP in a commercial application, please contact us.  
* No claim of suitability, guarantee, or any warranty whatever happens.
