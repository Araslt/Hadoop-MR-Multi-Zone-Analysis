<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
</head>
<body>

 <section> 
  <h2>LT</h2>
    <h3>Hadoop MapReduce Projektas</h3>
    <p>Projekto aprašyme yra pateiktas Hadoop MapReduce projekto detalus aprašas. Šiame dokumente yra aprašomas Hadoop, MapReduce modelis, užduotis, jos sprendimo procesas ir kodo fragmentai. Šio projekto tikslas yra rasti maršrutus, kurie aplanko daugiau nei vieną geografinę zoną tą pačią dieną naudojant Hadoop MapReduce modelį.</p>
  </section>
  
  <section id="lt"> 
    <ol>
      <li><a href="#hadoop">Hadoop</a></li>
      <li><a href="#mapreduce">MapReduce</a></li>
      <li><a href="#keyvalue">Raktas/reikšmė</a></li>
      <li>Užduotis
        <ol>
          <li><a href="#map">Map</a></li>
          <li><a href="#shuffle">Shuffle/Sort</a></li>
          <li><a href="#reduce1">Reduce (1)</a></li>
          <li><a href="#reduce2">Reduce (2)</a></li>
        </ol>
      </li>

  </section>


  <section>
    <h3>Hadoop</h3>
    <p>Hadoop yra atviro kodo projektas, skirtas didelio masto duomenų apdorojimui naudojant MapReduce modelį. Projekto pagrindiniai komponentai yra:</p>
    <ul>
      <li>Hadoop Distributed File System (HDFS): Duomenų saugojimo sistema.</li>
      <li>Hadoop MapReduce: Modelis, skirtas duomenų apdorojimui.</li>
    </ul>
    <p>Projekto vykdymui reikės VMware Workstation programos, kurią naudosime paleidžiant Hadoop virtualią mašiną. Po virtualios mašinos įkėlimo galėsime pradėti naudoti Hadoop.</p>
  </section>

  <section>
    <h3>MapReduce Modelis</h3>
    <p>MapReduce yra programavimo modelis, skirtas didelių duomenų apdorojimui naudojant klasterio architektūrą. Šis modelis apima tris pagrindinius komponentus:</p>
    <ul>
      <li>Map: Duomenų apdorojimo etapas, skirtas įrašams pavieniui apdoroti ir sugeneruoti tikslesnę išvestį.</li>
      <li>Shuffle/Sort: Etapas, kuriame sugeneruota informacija yra surūšiuojama ir pasiruošiama perduoti "reduce" funkcijai.</li>
      <li>Reduce: Duomenų apdorojimo etapas, skirtas sujungti "map" funkcijos išvestis ir gauti galutinį rezultatą.</li>
    </ul>
  </section>

  <section>
    <h3>Užduotis</h3>
    <p>Šio projekto užduotis yra rasti maršrutus, kurie aplanko daugiau nei vieną geografinę zoną tą pačią dieną. Šiai užduočiai yra naudojamas MapReduce modelis, kuriame yra trys etapai: "map", "shuffle/sort" ir "reduce".</p>
    <section>
      <h3>Map</h3>
      <p>"Map" etapo kodas nuskaito įvesties duomenis iš failo "duom_full.txt", apdoroja juos ir įrašo rezultatus į failą "mapout_2.txt". Duomenys faile yra atskirti skliaustais "{}" ir dalijami į reikiamas eilutes bei kintamuosius. Šis etapas atlieka šias pagrindines funkcijas:</p>
      <ul>
        <li>Apdoroja duomenis eilutėmis.</li>
        <li>Dalija eilutes į parametrų sąrašus.</li>
        <li>Atrenka reikiamus parametrus (pvz., "marsrutas", "geografine zona", "sustojimo data").</li>
      </ul>
    </section>
    <section>
      <h3>Shuffle/Sort</h3>
      <p>"Shuffle/Sort" etapo kodas skaito duomenis iš failo "mapout_2.txt", juos surūšiuoja ir rašo rezultatus į failą "smapout_2.txt". Čia atliekamos šios pagrindinės užduotys:</p>
      <ul>
        <li>Duomenys nuskaitomi iš vieno failo, surūšiuojami ir rašomi į kitą failą.</li>
        <li>Duomenys yra suskaidomi į atskirus parametrus ir surūšiuojami pagal tuos parametrus.</li>
      </ul>
    </section>
    <section>
      <h3>Reduce</h3>
      <p>"Reduce" etapas skirtas apdoroti duomenis, sugeneruotus ankstesniais etapais, ir rasti maršrutus, kurie aplanko daugiau nei vieną geografinę zoną tą pačią dieną. Šiame etape naudojamas žodynas "marsrutai_zonu_kiekiams", kuriame saugoma informacija apie maršrutų apsilankytas geografines zonas.</p>
    </section>
  </section>

  <section>
    <h3>Baigiamasis žodis</h3>
    <p>Šis projektas demonstruoja Hadoop MapReduce modelio pritaikymą duomenų apdorojimui, suskaidant užduotį į "map", "shuffle/sort" ir "reduce" etapus. Projekto aprašyme pateikti kodo fragmentai padeda suprasti, kaip vyksta duomenų apdorojimas kiekviename etape. Norint išsamiau susipažinti su projekto detaliais veiksmais, būtų gerai susipažinti su kodo fragmentais ir giliau išstudijuoti Hadoop MapReduce modelį bei jo veikimo principus.</p>
  </section>
  
  <!-- Kitos sekcijos -->


   <section>
    <h2>EN</h2>
    <h3>Hadoop MapReduce Project</h3>
    <p>Introduction</p>
    <p>This document outlines a Hadoop MapReduce project with a detailed description. The project's focus is to find routes that visit more than one geographic zone on the same day using the Hadoop MapReduce model. The description covers Hadoop, the MapReduce model, the task, the solution process, and code snippets.</p>
  </section>
    
  <section id="en">
    <ol>
      <li><a href="#hadoop">Hadoop</a></li>
      <li><a href="#mapreduce">MapReduce</a></li>
      <li><a href="#keyvalue">Key/Value</a></li>
      <li>Task
        <ol>
              <li><a href="#map">Map</a></li>
              <li><a href="#shuffle">Shuffle/Sort</a></li>
              <li><a href="#reduce1">Reduce (1)</a></li>
              <li><a href="#reduce2">Reduce (2)</a></li>
        </ol>
      </li>
    </ol>
 <section>


  <section>
    <h3>Hadoop</h3>
    <p>Hadoop is an open-source project designed for processing large-scale data using the MapReduce model. The key components of the project include:</p>
    <ul>
      <li>Hadoop Distributed File System (HDFS): A data storage system.</li>
      <li>Hadoop MapReduce: A model for data processing.</li>
    </ul>
    <p>For executing the project, you'll need the VMware Workstation program to run the Hadoop virtual machine. After loading the virtual machine, you can begin using Hadoop.</p>
  </section>

  <section>
    <h3>MapReduce Model</h3>
    <p>MapReduce is a programming model aimed at processing large data sets using a cluster architecture. This model consists of three main components:</p>
    <ul>
      <li>Map: The data processing stage that handles individual records and generates more precise output.</li>
      <li>Shuffle/Sort: An intermediate stage where generated information is sorted and prepared for the "reduce" function.</li>
      <li>Reduce: The data processing stage that combines the outputs of the "map" function to obtain the final result.</li>
    </ul>
  </section>

  <section>
    <h3>Task</h3>
    <p>The task of this project is to find routes that visit more than one geographic zone on the same day. The MapReduce model is used for this task, employing three stages: "map," "shuffle/sort," and "reduce."</p>
    <section>
      <h3>Map</h3>
      <p>The "Map" stage's code reads input data from the "duom_full.txt" file, processes it, and writes the results to the "mapout_2.txt" file. Data in the file is enclosed in curly braces "{}" and divided into relevant lines and variables. This stage performs the following functions:</p>
      <ul>
        <li>Processes data line by line.</li>
        <li>Divides lines into parameter lists.</li>
        <li>Selects relevant parameters (e.g., "marsrutas," "geografine zona," "sustojimo data").</li>
      </ul>
    </section>
    <section>
      <h3>Shuffle/Sort</h3>
      <p>The code in the "Shuffle/Sort" stage reads data from the "mapout_2.txt" file, sorts it, and writes the results to the "smapout_2.txt" file. The main tasks performed here are:</p>
      <ul>
        <li>Reading data from one file, sorting it, and writing it to another file.</li>
        <li>Splitting data into separate parameters and sorting based on those parameters.</li>
      </ul>
    </section>
    <section>
      <h3>Reduce</h3>
      <p>The "Reduce" stage is meant to process data generated in previous stages, find routes that visit more than one geographic zone on the same day, and utilize the "marsrutai_zonu_kiekiams" dictionary to store information about visited geographic zones.</p>
    </section>
  </section>

  <section>
    <h3>Conclusion</h3>
    <p>This project showcases the application of the Hadoop MapReduce model to data processing, breaking down the task into "map," "shuffle/sort," and "reduce" stages. Code snippets provided in the project description help understand the data processing that occurs in each stage. To gain a deeper understanding of the project's detailed actions, it would be beneficial to study the code fragments and delve into the workings of the Hadoop MapReduce model and its principles.</p>
  </section>

    
  <footer>
    <h2></h2>
    <p>© 2023 Hadoop MapReduce Projektas. Visos teisės saugomos.</p>
  </footer>
</body>
</html>
