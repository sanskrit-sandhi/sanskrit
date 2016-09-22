#!/bin/bash

gnuplot -persist << EOF
set term png size
set output 'merge.png'
set xlabel "Chapter"
set ylabel "Goodness"
set size 1.0,1.0
plot "merge" u 1:2 w linespoints lw 3 title 'JNU Result' ,\
            "merge" using 1:3 with linespoints lw 3 title 'UOH Result' ,\
            "merge" using 1:4 with linespoints lw 3 title 'Inria Result'
EOF
