# Data Lakes and Data Integration

![logo](https://assets.intersystems.com/e4/e5/c7728ffb4f60964a6e7d089905f0/azure-logo-large.jpg)

## Objectifs

* Adapt the python scripts to import all the files in a local directory by
respecting the initial structure on an azure data lake storage

## Etapes

Tout d'abord il est nécessaire de créer un ressource group sur Azure. Nous n'avons pas les droits pour réaliser cette action. Ainsi, nous allons utliser le ressource groupe "DP-100-DataLakes".

Ensuite, on créé un compte de stockage sur ce ressource group, grâce au fichier provision_blob.py :  
![image](https://user-images.githubusercontent.com/57401552/201711064-dccdd658-df1c-47bd-9be1-3c3c89df8e35.png)

Enfin, on construit un script pour uploader les fichiers sur le blob storage azure tout en respectant la structure des fichiers : 

* Pour faire cela, on utilise la méthode os.walk qui liste tous les chemins des tous les fichiers dans le directory.
* Ensuite, la méthode upload_blob est utilisé pour upload chaque fichier sur le blob azure
 

