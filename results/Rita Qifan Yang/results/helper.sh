#!/bin/bash


awk '
 BEGIN {FS=",";count=0}
 {if ($1 != "") {print $0; count+=1}}
 ' < p2.csv > p3.csv

