# Stat 679 HW1 Q2
# Create summarize.csv, with 1 row per analysis and 3 columns
#		rootname: the file name root ("xxx")
#		hmax: the maximum number of hybridizations allowed during the analysis
#		elapsedTime: total CPU time, or "Elapsed time"
#		Nruns: number of runs
#		Nfail: tuning parameter, "max number of failed proposals"
#		fabs: tuning parameter called "ftolAbs" in the log file (tolerated 
#				difference in the absolute value of the score function, to stop 
#				the search)
#		frel: "ftolRel"
#		xabs: "xtolAbs"
#		xrel: "xtolRel"
#		seed: main seed, i.e. seed for the first runs
#		under3460: number of runs that returned a network with a score (-loglik value) better than (below) 3460
#		under3450: number of runs with a network score under 3450
#		under3440: number of runs with a network score under 3440

output="summarize.csv"
printf "" > $output
for logfile in log/*.log
do
	rootname=$(basename -s .log $logfile)
	outfile="out/${rootname}.out"
	hmax=$(head -n2 $logfile | ggrep -Po "hmax = \K\d+") 
	elapsedTime=$(ggrep -Po "Elapsed time. \K\d+[\.]?[\de\-]*" $outfile)
	Nruns=$(head -n7 $logfile | ggrep -Po "BEGIN. \K\d+")
	Nfail=$(head -n5 $logfile | ggrep -Po "max number of failed proposals \K\d+")
	fabs=$(head -n4 $logfile | ggrep -Po "ftolAbs=\K\d+[\.]?[\de\-]*")
	frel=$(head -n4 $logfile | ggrep -Po "ftolRel=\K\d+[\.]?[\de\-]*")
	xabs=$(head -n4 $logfile | ggrep -Po "xtolAbs=\K\d+[\.]?[\de\-]*")
	xrel=$(head -n4 $logfile | ggrep -Po "xtolRel=\K\d+[\.]?[\de\-]*")
	seed=$(head -n9 $logfile | ggrep -Po "main seed \K\d+")
	under3460=0
	under3450=0
	under3440=0
	for num in $(ggrep -Po "loglik of best \K\d+" $logfile)
	do
		if [ $num -lt 3460 ]
		then
			((under3460++))
			if [ $num -lt 3450 ]
			then
				((under3450++))
				if [ $num -lt 3440 ]
				then
					((under3440++))
				fi
			fi
		fi
	done
	printf "%s " $rootname >> $output
	printf "%s " $hmax >> $output
	printf "%s " $elapsedTime >> $output
	printf "%s " $Nruns >> $output
	printf "%s " $Nfail >> $output
	printf "%s " $fabs >> $output
	printf "%s " $frel >> $output
	printf "%s " $xabs >> $output
	printf "%s " $xrel >> $output
	printf "%s " $seed >> $output
	printf "%s " $under3460 >> $output
	printf "%s " $under3450 >> $output
	printf "%s\n" $under3440 >> $output
done



