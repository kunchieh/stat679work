# Stat 679 HW1 Q1
# Change timetesty_snaq.log to timetest0y_snaq.log 
#        timetesty_snaq.out to timetest0y_snaq.out for y between 1 to 9

for i in {1..9}
do
	if [ -f "log/timetest${i}_snaq.log" ]; then
		mv "log/timetest${i}_snaq.log" "log/timetest0${i}_snaq.log"
	fi
	if [ -f "out/timetest${i}_snaq.out" ]; then
		mv "out/timetest${i}_snaq.out" "out/timetest0${i}_snaq.out"
	fi
done

