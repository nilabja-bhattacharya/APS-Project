#!/bin/bash

for i in {1..149}
do
    echo file_$i.txt
    python3 krskal_fibbonacci.py < file_$i.txt >> outfile3.txt
    python3 kruskl_veb.py < file_$i.txt >> outfile2.txt
    python3 krudsu.py < file_$i.txt >> outfile1.txt
done

rm -rf file_*.txt

python3 compare.py
rm -rf outfile*.sh