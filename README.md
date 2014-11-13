SVMOneClAS
==========
1. Input data  
	In order to run a script one should have two files:  
		1. Input for train data (canonical event of alternative splicing)  
		2. Input for test data (potential new event of alternative splicing)  
	Each have consists of 4 columns:
		1. Id of transcript
		2. Number of reads mapped on this particular splice junction
		3. Average number of reads at all canonical splice junctions of this transcript
		4. Gene length
		5. Number of exons

2. Runing the script
	One can use test data in order to run script
	Example:
		python script.py ref_final.txt alt_final.txt, where ref_final - train data and alt_final - test data

3. Output
	Script outputs file results.txt with just one column, where "1" means that this particular event was described as a potential novel and "-1" means that this event was not described as novel

4. In order to run a scdript one should have:
	1. Python ver 2.7
	2. Numpy library
	3. Scikit-learn library 
