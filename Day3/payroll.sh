
input_file="employees.txt"
output_file="payroll_report.txt"

echo "EmployeeID Name Salary Tax Bonus NetSalary" > "$output_file"

while read empid name salary
do
    # Tax Calculation
    if [ "$salary" -le 30000 ]; then
        tax=$((salary * 5 / 100))
    elif [ "$salary" -le 60000 ]; then
        tax=$((salary * 10 / 100))
    else
        tax=$((salary * 15 / 100))
    fi

    # Bonus Calculation
    if [ "$salary" -le 50000 ]; then
        bonus=2000
    else
        bonus=5000
    fi

    # Net Salary
    net_salary=$((salary - tax + bonus))

    echo "$empid $name $salary $tax $bonus $net_salary" >> "$output_file"

done < "$input_file"

echo "Payroll report generated successfully."
