#!/bin/sh

while read line
do
    echo $line
    sh ./parsefeed.sh $line
done < $1

