# Stat 679 HW1 Q2
# Create summarize.csv, with 1 row per analysis and 3 columns
#		rootname: the file name root ("xxx")
#		hmax: the maximum number of hybridizations allowed during the analysis: hmax
#		elapsedTime: total CPU time, or "Elapsed time".

output="summarize.csv"
for logfile in log/*.log
do
	rootname=$(head -n6 $logfile | ggrep -Po "rootname for files. \K[^ ]+")
	hmax=$(head -n2 $logfile | ggrep -Po "hmax = \K\d+") 
	outfile="out/${rootname}.out"
	elapsedTime=$(ggrep -Po "Elapsed time. \K\d+\.\d+" $outfile)
	printf "%s %s %s\n" $rootname $hmax $elapsedTime >> $output
done



