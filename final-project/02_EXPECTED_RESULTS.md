# Independent expected results

Manually designed synthetic sequences; motif ATA. No biological discoveries.
Counts are bases, length is bases, GC is percent. Order follows FASTA.

| id | length | A | T | G | C | GC% | motif count | starts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Repeat | 6 | 3 | 3 | 0 | 0 | 0.00 | 2 | 0;2 |
| Mixed | 8 | 3 | 3 | 1 | 1 | 25.00 | 1 | 4 |
| GC_rich | 10 | 1 | 1 | 4 | 4 | 80.00 | 0 | empty field |
| Balanced | 12 | 3 | 3 | 3 | 3 | 50.00 | 0 | empty field |
| Tiny | 3 | 1 | 1 | 1 | 0 | 33.33 | 0 | empty field |

First CSV data row: `Repeat,6,3,3,0,0,0.00,2,0;2`.
Tiny's exact GC is 100/3; only displayed/saved text is rounded to 33.33.
Plot bar heights: 0,25,80,50,100/3. Scatter x: 6,8,10,12,3;
y: the same full-precision GC values. No statistical or functional claim follows.
All three outputs must exist and open. A valid rerun must give the same CSV bytes
and the same plotted values, labels and image pixels in the same environment.
Image bytes across different Matplotlib versions are not a portable requirement.
