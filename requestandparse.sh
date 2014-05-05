#!/bin/bash

sh ./bashrequest.sh tmp.txt $1
python parseparagraphs.py < tmp.txt > out.txt
cat out.txt >> colossus.txt
cat newline.txt >> colossus.txt
