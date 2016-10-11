Stat679: Computing tools for data analytics, Fall 2016
======================================================

Homework 1, for detail description, see:
https://github.com/UWMadison-computingtools/coursedata/tree/master/hw1-snaqTimeTests

Update: 10/11/16'
---
1. normalizeFileName.sh: The shell script change all "timetesty_snaq.log" into timetest0y_snaq.log in the "log" directory and all "timetesty_snaq.out" to "timetest0y_snaq.out" in the "out" directory, for all y between 1 to 9, if files exist.

2. summarizeSNaQres.sh: The shell script create "summarize.csv" file, with 1 row per analysis and 3 columns: 
	rootname: the file name root ("xxx") 
	hmax: the maximum number of hybridizations allowed during the analysis
	elapsedTime: total CPU time, or "Elapsed time".
3. summarizeSNaQres.sh: The shell script create "summarize.csv" file, with 1 row per analysis
		rootname: the file name root ("xxx")
		hmax: the maximum number of hybridizations allowed during the analysis
		elapsedTime: total CPU time, or "Elapsed time"
		Nruns: number of runs
		Nfail: tuning parameter, "max number of failed proposals"
		fabs: tuning parameter called "ftolAbs" in the log file (tolerated difference in the absolute value of the score function, to stop the search)
		frel: "ftolRel"
		xabs: "xtolAbs"
		xrel: "xtolRel"
		seed: main seed, i.e. seed for the first runs
		under3460: number of runs that returned a network with a score (-loglik value) better than (below) 3460
		under3450: number of runs with a network score under 3450
		under3440: number of runs with a network score under 3440