#!/bin/bash

gnuplot -persist << EOF
set term png size
set xtics  norangelimit
set xtics   ()
set output 'vowel.png'
set xlabel "Corpus"
set ylabel "Goodness"
set size 1.0,1.0
plot "vowel" u 1:3:xtic(2) w linespoints lw 3 title 'JNU Result' ,\
                "vowel" using 1:4:xtic(2) with linespoints lw 3 title 'UOH Result' ,\
                            "vowel" using 1:5:xtic(2) with linespoints lw 3 title 'Inria Result'
EOF



gnuplot -persist << EOF
set term png size
set xtics  norangelimit
set xtics   ()
set output 'vowelmerge.png'
set xlabel "Corpus"
set ylabel "Goodness"
set size 1.0,1.0
plot "vowelmerge" u 1:3:xtic(2) w linespoints lw 3 title 'JNU Result' ,\
                "vowelmerge" using 1:4:xtic(2) with linespoints lw 3 title 'UOH Result' ,\
                            "vowelmerge" using 1:5:xtic(2) with linespoints lw 3 title 'Inria Result'
EOF


gnuplot -persist << EOF
set term png size
set xtics  norangelimit
set xtics   ()
set output 'visarga.png'
set xlabel "Corpus"
set ylabel "Goodness"
set size 1.0,1.0
plot "visarga" u 1:3:xtic(2) w linespoints lw 3 title 'JNU Result' ,\
                "visarga" using 1:4:xtic(2) with linespoints lw 3 title 'UOH Result' ,\
                            "visarga" using 1:5:xtic(2) with linespoints lw 3 title 'Inria Result'
EOF

gnuplot -persist << EOF
set term png size
set xtics  norangelimit
set xtics   ()
set output 'visargamerge.png'
set xlabel "Corpus"
set ylabel "Goodness"
set size 1.0,1.0
plot "visargamerge" u 1:3:xtic(2) w linespoints lw 3 title 'JNU Result' ,\
                "visargamerge" using 1:4:xtic(2) with linespoints lw 3 title 'UOH Result' ,\
                            "visargamerge" using 1:5:xtic(2) with linespoints lw 3 title 'Inria Result'
EOF


gnuplot -persist << EOF
set term png size
set xtics  norangelimit
set xtics   ()
set output 'consonant.png'
set xlabel "Corpus"
set ylabel "Goodness"
set size 1.0,1.0
plot "consonant" u 1:3:xtic(2) w linespoints lw 3 title 'JNU Result' ,\
                "consonant" using 1:4:xtic(2) with linespoints lw 3 title 'UOH Result' ,\
                            "consonant" using 1:5:xtic(2) with linespoints lw 3 title 'Inria Result'
EOF

gnuplot -persist << EOF
set term png size
set xtics  norangelimit
set xtics   ()
set output 'consonantmerge.png'
set xlabel "Corpus"
set ylabel "Goodness"
set size 1.0,1.0
plot "consonantmerge" u 1:3:xtic(2) w linespoints lw 3 title 'JNU Result' ,\
                "consonantmerge" using 1:4:xtic(2) with linespoints lw 3 title 'UOH Result' ,\
                            "consonantmerge" using 1:5:xtic(2) with linespoints lw 3 title 'Inria Result'
EOF



