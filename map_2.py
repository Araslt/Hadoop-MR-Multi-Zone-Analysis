 #!/usr/bin/env python
import sys
# import datetime

sys.stdin = open("duom_cut_cut.txt", "r")
sys.stdout = open("mapout_2.txt", "w")

for line in sys.stdin:
  line = line.strip()
  line = line[2:len(line) - 2]
  susstring = line.split('}}{{')

  # Priskiriame kintamuosius reikalingiems laukams
  marsrutas = None
  geografine_zona = None
  sustojimo_data = None

  for stopas in susstring:
    parstrings = stopas.split('}{')
    for parstring in parstrings:
      (vardas, reiksme) = parstring.split('=')
      if (reiksme != ''):
        if (vardas == 'marsrutas'):
          marsrutas = reiksme
        if (vardas == 'geografine zona'):
          geografine_zona = reiksme
        if (vardas == 'sustojimo data'):
          sustojimo_data = reiksme

    # Patikriname, ar visi reikiami laukai yra priskirti
    if (marsrutas != None and geografine_zona != None
        and sustojimo_data != None):

      # Spausdiname reikiamus duomenis atskirtus tabuliavimo simboliu
      print(f'{marsrutas}\t{geografine_zona}\t{sustojimo_data}')
