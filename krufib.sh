#!/bin/bash

for i in {1..149}
do
    echo file_$i.txt
    python3 krskal_fibbonacci.py < file_$i.txt >> fib.txt
done
rm -rf file_*.txt