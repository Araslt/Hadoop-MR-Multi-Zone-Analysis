import sys
import time

start_time = time.time()

sys.stdin = open("smapout_2.txt", "r")
sys.stdout = open("redout_2.txt", "w")

# žodynas marsrutai_zonu_kiekiams, kuriame bus kaupiami duomenys
# marsrutai_zonu_kiekiams yra žodynas (dict), kuriame raktai yra marsrutas, o reikšmės yra dar vienas žodynas. 
# Šio vidinio žodyno raktai yra data, o reikšmės yra rinkiniai (set) geografine_zona reikšmių.
# Tai leidžia lengvai atlikti užduotis, kurios susijusios su skirtingomis reikšmėmis skirtingais 
# laikais tam pačiam maršrutui.
marsrutai_zonu_kiekiams = {}

for line in sys.stdin:
  # suskaidoma eilutė pagal tabuliavimo simbolius ir priskiriamos reikšmės kintamiesiems
  marsrutas, geografine_zona, data = line.strip().split('\t')

  # patikrinama, ar marsrutas yra žodyne marsrutai_zonu_kiekiams.
  # Jei nėra, tai pridedamas naujas raktas su tuščiu reikšmių žodynu.
  if marsrutas not in marsrutai_zonu_kiekiams:
    marsrutai_zonu_kiekiams[marsrutas] = {}

  # patikrinama, ar data yra marsrutai_zonu_kiekiams žodyne, esančiame po raktu marsrutas.
  # Jei nėra, tai pridedamas naujas raktas su tuščiu reikšmių aibiu.
  if data not in marsrutai_zonu_kiekiams[marsrutas]:
    marsrutai_zonu_kiekiams[marsrutas][data] = set()

  # į aibę, esančią po raktu data ir marsrutas žodyne marsrutai_zonu_kiekiams,
  # pridedama reikšmė geografine_zona
  marsrutai_zonu_kiekiams[marsrutas][data].add(geografine_zona)

# einama per žodyno marsrutai_zonu_kiekiams raktus ir reikšmes.
# Raktas priskiriamas kintamajam marsrutas, o reikšmė - kintamajam data_zonos
for marsrutas, data_zonos in marsrutai_zonu_kiekiams.items():

  # einama per data_zonos žodyno raktus ir reikšmes.
  # Raktas priskiriamas kintamajam data, o reikšmė - kintamajam zonos
  for data, zonos in data_zonos.items():

    # tikrinama, ar aibėje zonos yra daugiau nei vienas elementas
    if len(zonos) > 1:
      print(f"{marsrutas}\t{data}\t{','.join(zonos)}")

print("--- %s seconds ---" % (time.time() - start_time))
