#!/bin/bash
byr = `grep -oE "\d\d\d\d$" $1`
cyr = `date +%Y`

age = $(($cyr - $byr))
 sed 's/\d{2}.\d{2}.\d{4}/$age' $1 
