Stat679: Computing tools for data analytics, Fall 2016
======================================================

Homework 2, for detail description, see:
https://github.com/UWMadison-computingtools/coursedata/tree/master/hw2-datamerge

Update: 11/11/16'

---

Script	:	hw2.py
Purpose	:	merge the 2 data files of the month, where the energy value from each day is matched to the temperature value at the nearest time, with no need for any manual copy-paste operation. 
Usage	:	python hw2.py [-h] -t TEMPERATE_FILE -e ENERGY_FILE [-o OUTPUT_FILE] [-w], see python hw2.py -h for more details

File Requirements:
	1.	For temperature file:
		- it needs to have a title line : "#","Date Time, GMT-05:00","K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)"
		- after the title line, each line should has the format:
			#, MM/DD/YY HH:MM:SS AM/PM, temperature
		- the dates are consecutive increasing
	2. 	For energy file:
		- it needs to have a title line : Date/Time,Energy Produced (Wh)
		- after the title line, each line should has the format until the "Total"
			YYYY-MM-DD HH:MM:SS ZONE, energy
		- the dates are consecutive increasing
	3.	For the following cases, the script will send an warning into summary.log instead of stop the script
		- in the energy file, energy does not collect in midnight (HH:MM:SS is not equal to 00:00:00)
		- in the energy file, energy does not collect in Wisconsin time zone (ZONE is not equal to -0500 or -0600)
		- there are certain dates in temperature file that does not have a match energy in energy file
		- there are certain dates in energy file that does not have a match date in temperature file
