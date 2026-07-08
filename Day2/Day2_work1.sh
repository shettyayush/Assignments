mkdir project backup
touch file1.txt file2.txt script.sh

cp file1.txt backup/
mv file2.txt project/
mv file1.txt README.txt
find . -name "README.txt"
chmod +x script.sh
tar -czvf project.tar.gz project
backup README.txt script.sh

mkdir extract
tar -xzvf project.tar.gz -C extract

ls -R extract
