#!/bin/sh

python parsexml.py $1 > stories.txt
while read line
do
    echo $line
    echo $line >> colossus.txt
    sh ./requestandparse.sh $line
#    cat out.txt
done < stories.txt
