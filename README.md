# 🚲 Big Data Pipeline : Analyse TBM & Architecture Distribuée

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hadoop](https://img.shields.io/badge/Hadoop-3.3-blue.svg)](https://hadoop.apache.org/)
[![Spark](https://img.shields.io/badge/Spark-3.5-orange.svg)](https://spark.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)

Ce projet implémente un **pipeline Big Data complet (ETL)** pour l’analyse des données de vélos en libre-service de Bordeaux (TBM).  
Il a été conçu dans un cadre éducatif afin de démontrer :

- la mise en place d’un **cluster Hadoop distribué**,
- l’orchestration des flux de données,
- le traitement analytique interactif avec Spark.

---

## 🏗️ Architecture du Projet

L’infrastructure simule un environnement de production distribué grâce à la conteneurisation Docker.

- **Cluster Hadoop** :  
  Configuration multi-nœuds (1 Master + 2 Workers) assurant le stockage via **HDFS** et la gestion des ressources avec **YARN**.

- **Orchestration (Apache Airflow)** :  
  Automatisation de l’ingestion des données via un DAG récupérant les données depuis l’API TBM.

- **Traitement (Spark Shell)** :  
  Analyse exploratoire et calculs distribués sur les données stockées dans HDFS.

---

## ⚙️ Prérequis

- **Docker Desktop** (avec support Linux activé)
- **Python 3.x**
- **Apache Airflow**
- Image Docker Hadoop :  
  `liliasfaxi/hadoop-cluster:latest`

---

## 🚀 Installation et Déploiement

### 1. Création du réseau Docker

Création d’un réseau bridge pour permettre la communication isolée entre les conteneurs Hadoop.

```bash
docker network create --driver bridge hadoop
```

2. Démarrage des conteneurs Hadoop
   Le cluster est composé d’un nœud maître et de deux nœuds workers.

Nœud maître (NameNode & ResourceManager)
bash
Copier le code
docker run -itd \
 --net hadoop \
 -p 9870:9870 \
 -p 8088:8088 \
 -p 7077:7077 \
 -p 16010:16010 \
 --name hadoop-master \
 --hostname hadoop-master \
 liliasfaxi/hadoop-cluster:latest
Ces ports permettent l’accès aux interfaces Web Hadoop depuis la machine hôte.

Nœuds workers (DataNodes)
bash
Copier le code
docker run -itd \
 --net hadoop \
 -p 8040:8042 \
 --name hadoop-worker1 \
 --hostname hadoop-worker1 \
 liliasfaxi/hadoop-cluster:latest
bash
Copier le code
docker run -itd \
 --net hadoop \
 -p 8041:8042 \
 --name hadoop-worker2 \
 --hostname hadoop-worker2 \
 liliasfaxi/hadoop-cluster:latest 3. Lancement des services Hadoop
Connexion au conteneur maître :

bash
Copier le code
docker exec -it hadoop-master bash
Démarrage de HDFS et YARN :

bash
Copier le code
./start-hadoop.sh
Interfaces de monitoring
HDFS NameNode : http://localhost:9870

YARN ResourceManager : http://localhost:8088

🔄 Workflow d’Utilisation
Étape 1 : Ingestion automatisée (Airflow)
Un DAG Apache Airflow exécute périodiquement un script Python qui :

récupère les données JSON depuis l’API TBM,

stocke les fichiers dans HDFS.

Équivalent en ligne de commande HDFS :

bash
Copier le code

# Création du répertoire cible

hdfs dfs -mkdir -p input

# Injection du fichier dans HDFS

hdfs dfs -put purchases.txt input/
Étape 2 : Analyse interactive (Spark Shell)
Les analyses sont réalisées via Spark Shell (Scala) pour un traitement rapide en mémoire.

Lancement de Spark depuis le conteneur hadoop-master :

bash
Copier le code
spark-shell
Exemple de traitement :

scala
Copier le code
// Chargement des données depuis HDFS
val data = sc.textFile("input/data_tbm.json")

// Comptage du nombre d’entrées
data.count()

// Affichage des premières lignes
data.take(5).foreach(println)
👥 Auteurs et Contributeurs
Axel GODART — Developer & Data

Encadrement :
Projet réalisé dans le cadre du cours « Traitement Batch avec Hadoop HDFS ».

📄 Licence
Ce projet est sous licence MIT.
Consultez le fichier LICENSE pour plus de détails.

vbnet
Copier le code
MIT License

Copyright (c) 2024 Axel GODART

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT W## 2. 🚀 Démarrage des conteneurs Hadoop

Le cluster est composé de **trois conteneurs** :

- 1 nœud maître (NameNode & ResourceManager)
- 2 nœuds workers (DataNodes)

---

### 🧠 Nœud maître (NameNode & ResourceManager)

```bash
docker run -itd \
  --net hadoop \
  -p 9870:9870 \
  -p 8088:8088 \
  -p 7077:7077 \
  -p 16010:16010 \
  --name hadoop-master \
  --hostname hadoop-master \
  liliasfaxi/hadoop-cluster:latest
Ces ports permettent l’accès aux interfaces Web Hadoop depuis la machine hôte.

🗄️ Nœuds workers (DataNodes)
Worker 1

bash
Copier le code
docker run -itd \
  --net hadoop \
  -p 8040:8042 \
  --name hadoop-worker1 \
  --hostname hadoop-worker1 \
  liliasfaxi/hadoop-cluster:latest
Worker 2

bash
Copier le code
docker run -itd \
  --net hadoop \
  -p 8041:8042 \
  --name hadoop-worker2 \
  --hostname hadoop-worker2 \
  liliasfaxi/hadoop-cluster:latest
3. ⚙️ Lancement des services Hadoop
Connexion au conteneur maître
bash
Copier le code
docker exec -it hadoop-master bash
Démarrage de HDFS et YARN
bash
Copier le code
./start-hadoop.sh
📊 Interfaces de monitoring
HDFS NameNode : http://localhost:9870

YARN ResourceManager : http://localhost:8088

🔄 Workflow d’utilisation
Étape 1 : Ingestion automatisée (Apache Airflow)
Un DAG Apache Airflow exécute périodiquement un script Python qui :

récupère les données JSON depuis l’API TBM,

stocke les fichiers dans HDFS.

Équivalent en ligne de commande HDFS
bash
Copier le code
# Création du répertoire cible
hdfs dfs -mkdir -p input

# Injection du fichier dans HDFS
hdfs dfs -put purchases.txt input/
Étape 2 : Analyse interactive (Spark Shell)
Les analyses sont réalisées via Spark Shell (Scala) pour un traitement rapide en mémoire.

Lancement de Spark (depuis hadoop-master)
bash
Copier le code
spark-shell
Exemple de traitement Spark
scala
Copier le code
// Chargement des données depuis HDFS
val data = sc.textFile("input/data_tbm.json")

// Comptage du nombre d’entrées
data.count()

// Affichage des premières lignes
data.take(5).foreach(println)
👥 Auteurs et Contributeurs
Axel GODART — Developer & Data

Encadrement :
Projet réalisé dans le cadre du cours
« Traitement Batch avec Hadoop HDFS ».

📄 Licence
Ce projet est sous licence MIT.
Consultez le fichier LICENSE pour plus de détails.

pgsql
Copier le code
MIT License

Copyright (c) 2024 Axel GODART

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.ARRANTY OF ANY KIND.
```
