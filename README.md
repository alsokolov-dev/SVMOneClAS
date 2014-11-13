SVMOneClAS
==========
1. Input data <br/>  
	In order to run a script one should have two files:<br/>  
		1. Input for train data (canonical event of alternative splicing)<br/>  
		2. Input for test data (potential new event of alternative splicing)<br/>  
	Each have consists of 4 columns:<br/>
		1. Id of transcript<br/>
		2. Number of reads mapped on this particular splice junction<br/>
		3. Average number of reads at all canonical splice junctions of this transcript<br/>
		4. Gene length<br/>
		5. Number of exons<br/>
<br/>
2. Runing the script:<br/>
	One can use test data in order to run script<br/>
	Example:<br/>
		python script.py ref_final.txt alt_final.txt, where ref_final - train data and alt_final - test data<br/>
<br/>
3. Output:<br/>
	Script outputs file results.txt with just one column, where "1" means that this particular event was described as a potential novel and "-1" means that this event was not described as novel<br/>
<br/>
4. In order to run a scdript one should have:<br/>
	1. Python ver 2.7<br/>
	2. Numpy library<br/>
	3. Scikit-learn library<br/> 
