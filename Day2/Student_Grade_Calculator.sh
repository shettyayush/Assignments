echo "Enter Marks for 5 subjects: "

echo -n "Subject 1: "
read s1

echo -n "Subject 2: "
read s2

echo -n "Subject 3: "
read s3

echo -n "Subject 4: "
read s4

echo -n "Subject 5: "
read s5

total=$((s1+s2+s3+s4+s5))
average=$((total / 5))

echo "---------------------------"

echo "Total Marks =  $total"

echo "Average Marks = $average"

if [[ $average -ge 90 && $average -le 100 ]]; then
	grade="A"
elif [[ $average -ge 75 && $average -le 89 ]]; then
	grade="B"
elif [[ $average -ge 60 && $average -le 74 ]]; then
	grade="C"
elif [[ $average -ge 50 && $average -le 59 ]]; then
	grade="D"
elif [[ $average -lt 50 ]]; then
	grade="Fail"
else
	echo "Invalid Score Entered"
fi

echo "Grade=$grade"
