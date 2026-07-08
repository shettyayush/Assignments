username="Admin"
password="Admin@456"

attempt=1

while [[ $attempt -le 3 ]]
do
	echo "Attempt $attempt"
	
	echo -n "Enter Username: "
	read user

	echo -n "Enter Password: "
	read pass

	if [[ "$user" == "$username" ]] && [[ "$pass" == "$password" ]]; then
		echo "Login Successful"
		exit 0
	else
		echo "Invalid Username or Password"
	fi
	attempt=$((attempt+1))
done
echo "Account Locked"
