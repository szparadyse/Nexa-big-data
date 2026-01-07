# 🚲 Big Data Pipeline : Analyse TBM & Architecture Distribuée

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hadoop](https://img.shields.io/badge/Hadoop-3.3-blue.svg)](https://hadoop.apache.org/)
[![Spark](https://img.shields.io/badge/Spark-3.5-orange.svg)](https://spark.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)

Ce projet implémente un pipeline de données complet (ETL) pour l'analyse des vélos en libre-service de Bordeaux (TBM). Il a été conçu dans un cadre éducatif pour démontrer la mise en place d'un cluster Hadoop distribué, l'orchestration de flux de données et le traitement analytique interactif.

## 🏗️ Architecture du Projet

L'infrastructure simule un environnement de production distribué grâce à la conteneurisation Docker.

1.  [cite_start]**Cluster Hadoop** : Configuration multi-nœuds (1 Master + 2 Workers) assurant le stockage (HDFS) et la gestion des ressources (YARN)[cite: 3, 5].
2.  **Orchestration (Airflow)** : Automatisation des scripts d'ingestion pour collecter les données API en temps réel.
3.  **Traitement (Spark Shell)** : Analyse exploratoire et calculs distribués sur les données brutes stockées dans HDFS.

## ⚙️ Prérequis

- **Docker Desktop** (avec support Linux activé).
- **Python 3.x** & **Apache Airflow**.
- [cite_start]Image Docker de base : `liliasfaxi/hadoop-cluster:latest`[cite: 8].

## 🚀 Installation et Déploiement

### 1. Initialisation du Réseau

[cite_start]Création d'un réseau pont (bridge) pour permettre la communication isolée entre les conteneurs du cluster[cite: 14].

```bash
docker network create --driver bridge hadoop
2. Démarrage des Conteneurs
Le déploiement se fait en trois parties : le nœud maître (Master) et les deux nœuds esclaves (Workers).

Nœud Maître (NameNode & ResourceManager) :

Bash

docker run -itd --net hadoop -p 9870:9870 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/hadoop-cluster:latest

[Mapping des ports pour l'accès aux UIs Web depuis la machine hôte].

Nœuds Esclaves (DataNodes) :

Bash

docker run -itd -p 8040:8042 --net hadoop --name hadoop-worker1 --hostname hadoop-worker1 liliasfaxi/hadoop-cluster:latest
docker run -itd -p 8041:8042 --net hadoop --name hadoop-worker2 --hostname hadoop-worker2 liliasfaxi/hadoop-cluster:latest
.

3. Lancement des Services Hadoop
Une fois les conteneurs instanciés, il faut démarrer les démons HDFS et YARN.

Bash

# Accès au shell du conteneur maître
docker exec -it hadoop-master bash

# Script d'initialisation fourni
./start-hadoop.sh
.
+1

Interfaces de Monitoring : * HDFS NameNode : http://localhost:9870 * YARN ResourceManager : http://localhost:8088
+1

🔄 Workflow d'Utilisation
Étape 1 : Ingestion Automatisée (Airflow)
Un DAG Airflow est configuré pour exécuter périodiquement le script de collecte. Ce script récupère les données JSON de l'API TBM et les dépose dans HDFS.

Action équivalente en ligne de commande HDFS :

Bash

# Création du répertoire cible
hdfs dfs -mkdir -p input

# Injection du fichier (effectué par le script Python)
hdfs dfs -put purchases.txt input/
.
+1

Étape 2 : Analyse Interactive (Spark Shell)
Le traitement des données se fait via le shell Spark (Scala), permettant des opérations rapides en mémoire.

Lancement de Spark : Depuis le conteneur hadoop-master :

Bash

spark-shell
.

Exemple de traitement :

Scala

// Chargement du fichier depuis HDFS dans un RDD
val data = sc.textFile("input/data_tbm.json")

// Comptage des entrées
data.count()

// Affichage des premières lignes
data.take(5).foreach(println)
.

👥 Auteurs et Contributeurs
Axel GODART - Developer & DATA

Encadrement : Projet réalisé dans le cadre du cours "Traitement Batch avec Hadoop HDFS".

📄 Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

Plaintext

MIT License

Copyright (c) 2024 [Votre Nom]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
