README
===
DSSP is a system for splice site prediction using deep neural networks, as described in [Human Splice-Site Prediction with Deep Neural Networks. Naito T. *J Comput Biol*. 2018;25(8):954–61](https://www.liebertpub.com/doi/pdfplus/10.1089/cmb.2018.0041).  
  
Required
===
* DSSP is implemented in [Python](https://www.python.org) (3.5.2).  
* [Keras](https://keras.io/) must be installed to run our program. We recommend Keras 2.0.5 since different versions may cause unexpected errors. Several modules may be required for using Keras. Please read the official documentations.
  
Usage
===
* Download all files into your favorite directory. 
* Select a program file according to the type of splice site (donor site: “DS_DSSP.py,” acceptor site: “AS_DSSP.py”).  
* The required input is a 140-mer base sequence with the consensus sequence (i.e., ‘‘GT’’ and ‘‘AG’’ for the donor and acceptor sites, respectively) in the middle. 
* DSSP can take a base sequence string or FASTA file (see Examples).
* It returns the probability that the input sequence is a splice site.  
Options:  
  * -I, INPUT : 140-mer base sequece string, or FASTA file.
  * -O, OUTPUT: path to the output file.
  
Examples
===
Donor site
---
An input for donor site should be a 140-mer string with the GT at positions 71 and 72.  
```
$ python DS_DSSP.py -I CTCCTCTTTGCCTTACTCCTAGCCATGGAGCTCCCATTGGTGGCAGCCAGTGCCACCATGCGCGCTCAGTGTAAGTATCATTCCCTCTCACTG
TCCTGGAGAGGACGAGAATTCCACCTGGGGTGCTGGGGGTCACTGGG
```
Result
```bash
Donor site probability: 0.9999337196350098
```

Alternatively, DSSP can receive a FASTA file.  
You can specify an output filename optionally. If you do not specify an output filename, the results are saved as "{input filename}_result.txt" in the same directory as the input file.
```bash
$ python DS_DSSP.py -I input.fasta -O output.txt 
```


Acceptor site
---
An input for acceptor site should be a 140-mer string with the AG at positions 69 and 70.  
```
$ python AS_DSSP.py -I GGCCAGGGGCATAGAGCTGGCCAAGGAGCCATGGCTCACTAACGTGTTGTATGGGGCTCCTTCCCTTCAGGTCCAGGCTCCTGCGTGAAGTGA
TGCTCCTCTTTGCCTTACTCCTAGCCATGGAGCTCCCATTGGTGGCA
```
Result
```bash
Acceptor site probability:: 0.9931520223617554
```
You can input a FASTA file, and specify an output filename in the same way as the DS_DSSP example.
  
License
===
* The souce code can be modified without notice.
* DSSP is freely available for non-commercial use. If you are planning on using DSSP in a commercial application, please contact us.  
* No claim of suitability, guarantee, or any warranty whatever happens.
