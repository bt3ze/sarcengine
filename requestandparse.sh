#!/bin/bash

sh ./bashrequest.sh tmp.txt $1
python parseparagraphs.py < tmp.txt > out.txt
out.txt >> colossus.txt
newline.txt >> colossus.txt
