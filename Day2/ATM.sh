#Inital Balance

balance=10000

while true
do
echo "=============================================="
echo "1. Check Balance"
echo "2. Deposit"
echo "3. Withdraw"
echo "4. Exit"

echo "=============================================="

echo -n "Enter your Choice :"
read choice

case $choice in 
	1) 
		echo  "Current balance: $balance"
		;;
	2)
		echo -n "Enter deposit amount: "
		read amount
		if [[ $amount -gt 0 ]]; then
			balance=$((balance+amount))
			echo "Amount deposited successfully"
			echo "Updated balance: $balance"
		else
			echo "Invalid amount"
		fi
		;;
	3)
		echo "Enter amount to withdraw"
		read withdraw
		if [[ $withdraw -le 0 ]]; then
			echo "Invalid withdraw amount"
		elif [[ $withdraw -gt $balance ]]; then
			echo "Insufficent balance."
		else
			balance=$((balance - withdraw))
			echo "Withdraw successfully"
			echo "Updated balance: $balance"
		fi
		;;
	4)
		echo "Thank you for using the application."
		break
		;;
	*)
		echo "Invalid choice, please select a valid option."
		;;
	esac
done
