Stat679: Computing tools for data analytics, Fall 2016
======================================================

Homework 1, for detail description, see:
https://github.com/UWMadison-computingtools/coursedata/tree/master/hw1-snaqTimeTests

Update: 10/09/16'
---
1. normalizeFileName.sh: The shell script change all "timetesty_snaq.log" into timetest0y_snaq.log in the "log" directory and all "timetesty_snaq.out" to "timetest0y_snaq.out" in the "out" directory, for all y between 1 to 9, if files exist.

2. summarizeSNaQres.sh: The shell script create "summarize.csv" file, with 1 row per analysis and 3 columns: 
	rootname: the file name root ("xxx") 
	hmax: the maximum number of hybridizations allowed during the analysis
	elapsedTime: total CPU time, or "Elapsed time".
