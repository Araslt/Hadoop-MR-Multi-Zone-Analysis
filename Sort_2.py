#!/usr/bin/env python
import sys

sys.stdin = open("mapout_2.txt", "r")
sys.stdout = open("smapout_2.txt", "w")
A = []
for line in sys.stdin:
  line = line.strip()
  marsr, zona, data = line.split('\t')
  A.append([marsr, zona, data])
A.sort(key=lambda tup: (tup[0], tup[1], tup[2]))
for el in A:
  print(f"{el[0]}\t{el[1]}\t{el[2]}")
