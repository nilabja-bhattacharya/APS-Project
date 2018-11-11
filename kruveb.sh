#!/bin/bash

for i in {1..149}
do
    echo file_$i.txt
    python3 kruskl_veb.py < file_$i.txt >> veb.txt
done
rm -rf file_*.txt