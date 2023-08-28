#!/usr/bin/env python

import sys

sys.stdin = open("smapout.txt", "r")
sys.stdout = open("redout.txt", "w")

# priskiriamos pradinės reikšmės, kadangi kintamieji bus naudojami kaip laikikliai, kurie atsimena paskutinio "dienos" reikšmę ir klientų skaičių.
current_diena = None
current_count = 0

# šis kintamasis naudojamas kaip laikiklis, kuriame laikomas kiekvienos eilutės raktas (diena) po to, kai jis yra apdorojamas.
diena = None

# input comes from STDIN
for line in sys.stdin:
  # pašalinamas pradžios ir pabaigos tarpas (jei yra).
  line = line.strip()

  # dalijama eilutė į dvi dalis, naudojant atskyrimą per tabuliacijos simbolį. Pirmoji dalis yra "diena", o antroji yra "count"
  diena, count = line.split('\t', 1)

  # convert count (currently a string) to int
  try:
    count = int(count)
  except ValueError:
    # count was not a number, so silently
    # ignore/discard this line
    continue

  # this IF-switch only works because Hadoop sorts map output
  # by key (here: word) before it is passed to the reducer
  # patikrinama, ar dabartinė "diena" yra ta pati kaip ir "current_diena".
  # Jei taip, tada "count" yra pridėtas prie "current_count".
  if current_diena == diena:
    current_count += count

#       jei dabartinė "diena" nesutampa su "current_diena", tada į STDOUT (standartinį išvesties srautą) yra išspausdinama "current_diena" ir "current_count" reikšmės, ir tada "current_count"
# yra priskiriamas dabartinio raktų reikšmės (count) reikšmės, o dabartinis raktas yra
# priskiriamas kintamajam "current_diena
  else:

    # šis kodas yra skirtas apdoroti paskutinę eilutę. Jei dabartinė "diena" yra ta pati kaip ir
    # "current_diena", tada "count" yra pridėtas prie "current_count" ir išspausdinamas
    # paskutinis poros rezultatas.
    if current_diena != None:
      # write result to STDOUT
      # print ('%s\t%s' % (current_diena, current_count))
      print(f'{str(current_diena)}\t{str(current_count)}')
    current_count = count
    current_diena = diena

# do not forget to output the last word if needed!
if current_diena == diena:
  # print('%s\t%s' % (current_diena, current_count))
  print(f'{str(current_diena)}\t{str(current_count)}')
