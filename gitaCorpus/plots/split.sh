#!/bin/bash

gnuplot -persist << EOF
set term png size
set output 'split.png'
set xlabel "Chapter"
set ylabel "Goodness"
set size 1.0,1.0
plot "split" u 1:2 w linespoints lw 3 title 'JNU Result' ,\
            "split" using 1:3 with linespoints lw 3 title 'UOH Result' ,\
            "split" using 1:4 with linespoints lw 3 title 'Inria Result'
EOF
