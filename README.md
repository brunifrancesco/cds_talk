#CDS Talk

##Requirements

- SBT (Scala build tool)
- Python 3.4 (CPython)
- PyPy


##Launch the notebook

	virtualenv --distribute -p /usr/bin/python3.4 cds
	cd cds
	source bin/activate
	git clone https://github.com/brunifrancesco/cds_talk.git
	cd cds_talk 
	pip3 install -r requirements.txt (this will take a while)
	ipython3 notebook

##Deactivate the virtualenv

	deactivate

#Exec the "performance" test
	
The output will be saved on csvs file. 
Change the out file name in the compute_charts.py script to avoid overriding previuos results.

	cd benchmarks
	rm *.csv
	sbt run (Output will be saved on scala.csv)
	/bin/to/pypy compute_charts.py
	
