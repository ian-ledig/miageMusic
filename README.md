# Entraînement d'un modèle de voix d'IA
Pour ce projet, nous avons entraîné deux voix personnalisées sous forme de modèle .pth. Ces voix sont celle de deux rappeurs français.
La première étant celle de Freeze Corleone (2 jours d'entraînement) et la seconde est celle de Laylow (2.5 semaines d'entraînement).

Les étapes d'entraînement de ces modèles ont été les suivantes :

-   Récupérer les fichiers audio de chansons,
-   Extraire les voix des chansons,
-   Découper ces voix en petits échantillons,
-   Entraîner ces échantillons pour générer un fichier modèle .pth.

## Exemple de résultat généré

<audio controls>
  <source src="https://cdn.discordapp.com/attachments/774264633246351370/1118559102612807710/tchoupi-freezecorleone.wav" type="audio/mpeg">
  Votre navigateur ne prend pas en charge la lecture audio.
</audio>

[Générique de tchoupi chanté par Freeze Corleone](https://cdn.discordapp.com/attachments/774264633246351370/1118559102612807710/tchoupi-freezecorleone.wav)

## Découpage des étapes
### Récupération des fichiers audio
Nous avons développé un programme python qui télécharge une vidéo demandée depuis youtube et la convertie en .mp3.

Suite à cette étape, nous avons récupéré les musiques de notre artiste.

### Extraire les voix des chansons
Pour récupérer les voix des chansons en retirant les instruments de fond, nous avons créé un fork d'un dépôt Deezer déjà existant.

[Voir l'outil.](https://github.com/ian-ledig/spleeter)

Suite à cette étape, nous avons récupéré les voix de notre artiste.

### Découper les voix en petits échantillons
Pour découper les voix récupérées en petits échantillons d'en moyenne 5s (durée conseillée), nous avons créé un fork d'un dépôt existant.

[Voir l'outil.](https://github.com/ian-ledig/AudioSlicer)

Suite à cette étape, nous avons créé de multiples fichiers d'échantillons de voix de notre artiste.

### Entraînement des échantillons
Pour la phase d'entraînement des échantillons de voix, nous avons créé un fork d'un dépôt existant.

[Voir l'outil.](https://github.com/ian-ledig/so-vits-svc-fork)

Suite à cette étape, nous avons généré un fichier modèle .pth contenant la voix de notre artiste.

## Automatisation des étapes

Après avoir découpé toutes ces étapes, nous avons développé un nouveau script python qui automatise le tout.
Ainsi, il est simplement nécessaire d'installer les librairies nécessaires et d'exécuter la commande ``python miageMusic.py https://youtu.be/BtZ6tX41eUA`` pour récupérer la version avec la voix d'un de nos artistes.

### Mise en place

Pour la mise en place nous avons utilisé Anaconda3.
Il est important de noter que les commandes si dessous doivent être exécuter dans un terminal qui accepte les commandes Anaconda3.

![Drag Racing](https://cdn.discordapp.com/attachments/1020255179582488657/1123988350496428072/image.png)

1. Creation de deux environnements Anaconda3.
    ```
    conda create --name miage python=3.10
    conda create --name so-vits-svc-fork python=3.10
    ```

2. Activation de l'environnement miage
    ``conda activate miage``

3. Installation des librairies nécessaires
    ```
    pip install https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
    pip install spleeter
    ```

4. Activation de l'environnement so-vits-svc-fork
    ``conda activate so-vits-svc-fork``

5. Installation des librairies nécessaires
    ```
    pip install -U so-vits-svc-fork
    python -m pip install -U pip setuptools wheel
    pip install -U torch torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```

