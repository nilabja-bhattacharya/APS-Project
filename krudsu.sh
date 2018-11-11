#!/bin/bash

for i in {1..149}
do
    echo file_$i.txt
    python3 krudsu.py < file_$i.txt >> dsu.txt
done
rm -rf file_*.txt