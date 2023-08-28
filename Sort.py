#!/usr/bin/env python
import sys

sys.stdin = open("mapout.txt", "r")
sys.stdout = open("smapout.txt", "w")
A = []
for line in sys.stdin:
  key, val = line.strip().split('\t', 1)
  A.append([key, val])
A.sort(key=lambda tup: (tup[0], tup[1]))
for el in A:
  print(f"{el[0]}\t{el[1]}")
