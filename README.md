## Graveler

A fork of ShoddyCast's graveler repository for the graveller code challenge that simulates the rolling of a 4-sided die 231 times for a billion samples. This is done to see the highest number of "ones" rolled over these samples.

The original python code made by ShoddyCast is available for reference with modifications made to measure runtime as well as an optimized python version of the code, a version written in java, and a version written in c. A version written in python that takes advantage of threading was also made to see if it would have any measurable improvement, but it seems to only decrease performance. All versions measure runtime in the code by calculating time elapsed from just after imports are completed to just after calculations are completed (and before the final results are printed out).
