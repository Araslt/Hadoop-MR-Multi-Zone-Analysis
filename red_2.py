import sys

sys.stdin = open("mapout_2.txt", "r")
sys.stdout = open("redout_2.txt", "w")

# žodynas naudojamas kaupiant informaciją apie kiekvieno maršruto apsilankytas geografines zonas
marsrutai_zonu_kiekiams = {}

for line in sys.stdin:

  # kintamieji: marsrutas, geografine_zona ir _. Kintamasis _ nereikalingas šiuo atveju,
  # todėl jam yra priskiriamas "šiukšlių" kintamasis, kad jis nebūtų naudojamas vėliau.
  marsrutas, geografine_zona, _ = line.strip().split('\t')

  # tikrinama, ar žodyne marsrutai_zonu_kiekiams yra jau marsrutas.
  # Jei ne, tai marsrutas yra pridedamas prie žodyno kaip raktas, o jo reikšme priskiriama tuščiai aibei.
  # Kitu atveju, geografinė zona, kurią pasiekė maršrutas, yra pridėta prie to maršruto aibės.
  if marsrutas not in marsrutai_zonu_kiekiams:
    marsrutai_zonu_kiekiams[marsrutas] = set()
  marsrutai_zonu_kiekiams[marsrutas].add(geografine_zona)

# Paskutinėje programos eilutėje tikrinama kiekvieno maršruto geografinių zonų aibės ilgis.
# Jei jis yra didesnis nei 1, tai reiškia, kad maršrutas aplankė daugiau nei vieną geografinę zoną.
# Šiuo atveju marsrutas tiesiog spausdinamas kaip išvesties duomenys.
for marsrutas, zonos in marsrutai_zonu_kiekiams.items():
  if len(zonos) > 1:
    print(marsrutas)
#
##
##
###
##
##
##
##
##
#
##
#
# if marsrutas not in marsrutai_zonu_kiekiams:
#   marsrutai_zonu_kiekiams[marsrutas] = {"zonos": set(), "kiekis": 0}
# marsrutai_zonu_kiekiams[marsrutas]["zonos"].add(geografine_zona)
# marsrutai_zonu_kiekiams[marsrutas]["kiekis"] += 1
#
#
#  if len(info["zonos"]) > 1:
# print(f"{marsrutas}\t{info['kiekis']}\t{len(info['zonos'])}")
