#  Digital Asset Management - Azure

#  Objectif
Développer une WebApp permettant aux équipes marketing de rechercher et gérer des images automatiquement.

--------------------------------

##  Technologies
- Python (Flask)
- Azure Blob Storage
- Azure Cognitive Services (Computer Vision)
- Azure Web App

---------------------------------

### Installer les dépendances

pip install -r requirements.txt

###  Configurer les variables
Créer un fichier .env :
AZURE_STORAGE_CONNECTION_STRING=xxx
AZURE_COMPUTER_VISION_KEY=xxx
AZURE_ENDPOINT=xxx

##  Lancer le projet
python app.py

##  Deploiement
az webapp up

##  Fonctionnalités
Upload d’images
Suppression / modification
Analyse automatique (tags)
Recherche multi-critères
Téléchargement

##  Intelligence artificielle
Les images sont analysées automatiquement grâce à Azure Computer Vision afin de générer des tags pour améliorer la recherche.

### 1. Cloner
bash
git clone https://github.com/ton-username/projet-azure-dam.git
cd projet-azure-dam
