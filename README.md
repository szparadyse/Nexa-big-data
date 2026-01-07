# 🚲 Big Data Pipeline : Analyse TBM & Architecture Distribuée

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hadoop](https://img.shields.io/badge/Hadoop-3.3-blue.svg)](https://hadoop.apache.org/)
[![Spark](https://img.shields.io/badge/Spark-3.5-orange.svg)](https://spark.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)

Ce projet implémente un pipeline de données complet (ETL) pour l'analyse des vélos en libre-service de Bordeaux (TBM). Il a été conçu dans un cadre éducatif pour démontrer la mise en place d'un cluster Hadoop distribué, l'orchestration de flux de données et le traitement analytique interactif.

🏗️ Architecture du Projet
L'infrastructure simule un environnement de production distribué grâce à la conteneurisation Docker :

Cluster Hadoop : Configuration multi-nœuds (1 Master + 2 Workers) assurant le stockage (HDFS) et la gestion des ressources (YARN).

Orchestration (Airflow) : Automatisation des scripts d'ingestion pour collecter les données API en temps réel.

Traitement (Spark Shell) : Analyse exploratoire et calculs distribués sur les données brutes stockées dans HDFS.

⚙️ Prérequis
Docker Desktop (avec support Linux activé).

Python 3.x & Apache Airflow.

Image Docker de base : liliasfaxi/hadoop-cluster:latest

🚀 Installation et Déploiement

1. Initialisation du Réseau
   Création d'un réseau pont (bridge) pour permettre la communication isolée entre les conteneurs du cluster.

Bash

docker network create --driver bridge hadoop 2. Démarrage des Conteneurs
Le déploiement se fait en trois parties : le nœud maître (Master) et les deux nœuds esclaves (Workers).

Nœud Maître (NameNode & ResourceManager) :

Bash

docker run -itd \
 --net hadoop \
 -p 9870:9870 -p 8088:8088 -p 7077:7077 -p 16010:16010 \
 --name hadoop-master \
 --hostname hadoop-master \
 liliasfaxi/hadoop-cluster:latest
Nœuds Esclaves (DataNodes) :

Bash

docker run -itd -p 8040:8042 --net hadoop --name hadoop-worker1 --hostname hadoop-worker1 liliasfaxi/hadoop-cluster:latest
docker run -itd -p 8041:8042 --net hadoop --name hadoop-worker2 --hostname hadoop-worker2 liliasfaxi/hadoop-cluster:latest 3. Lancement des Services Hadoop
Une fois les conteneurs instanciés, il faut démarrer les démons HDFS et YARN.

Bash

# Accès au shell du conteneur maître

docker exec -it hadoop-master bash

# Lancement du script d'initialisation à l'intérieur du conteneur

./start-hadoop.sh
📊 Interfaces de Monitoring
HDFS NameNode : http://localhost:9870

YARN ResourceManager : http://localhost:8088

🔄 Workflow d'Utilisation
Étape 1 : Ingestion Automatisée (Airflow)
Un DAG Airflow exécute périodiquement un script de collecte qui récupère les données JSON de l'API TBM et les dépose dans HDFS.

Action équivalente en ligne de commande :

Bash

# Création du répertoire cible dans HDFS

hdfs dfs -mkdir -p /user/input

# Injection manuelle d'un fichier

hdfs dfs -put data_tbm.json /user/input/
Étape 2 : Analyse Interactive (Spark Shell)
Le traitement se fait via le shell Spark (Scala) pour des calculs rapides en mémoire.

Lancement de Spark :

Bash

spark-shell
Exemple de traitement Scala :

Scala

// Chargement du fichier depuis HDFS
val data = sc.textFile("/user/input/data_tbm.json")

// Comptage des entrées
println(s"Nombre total d'entrées : ${data.count()}")

// Affichage des 5 premières lignes
data.take(5).foreach(println)
👥 Auteurs et Contributeurs
Axel GODART - Developer & DATA

Projet réalisé dans le cadre du cours "Traitement Batch avec Hadoop HDFS".

📄 Licence
Ce projet est sous licence MIT.

Plaintext

Copyright (c) 2024 Axel GODART

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
