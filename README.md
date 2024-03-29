# Data Lakes and Data Integration

![logo](https://assets.intersystems.com/e4/e5/c7728ffb4f60964a6e7d089905f0/azure-logo-large.jpg)

## Objectifs

Adapter les scripts python pour importer tous les fichiers dans un répertoire local en respectant la structure initiale sur un stockage azure data lake.

## Etapes

### Upload les données sur Azure 

Tout d'abord il est nécessaire de créer un ressource group sur Azure. Nous n'avons pas les droits pour réaliser cette action. Ainsi, nous allons utliser le ressource groupe "DP-100-DataLakes".

Ensuite, on créé un compte de stockage sur ce ressource group, grâce au fichier provision_blob.py et notamment grâce à la méthode begin_create :  
![image](https://user-images.githubusercontent.com/57401552/201711064-dccdd658-df1c-47bd-9be1-3c3c89df8e35.png)

Enfin, on construit un script pour uploader les fichiers sur le blob storage azure tout en respectant la structure des fichiers : 

* Pour faire cela, on utilise la méthode os.walk qui liste tous les chemins des tous les fichiers dans le directory.
![image](https://user-images.githubusercontent.com/57401552/201712832-44b66dda-a5cc-4a1e-b53e-8cec95b30561.png)

* Ensuite, la méthode upload_blob est utilisé pour upload chaque fichier sur le blob azure.
 ![image](https://user-images.githubusercontent.com/57401552/201713241-3838c24f-832e-4914-a61f-48cefedf7f48.png)
 
 ### ETL sur la data factory
 
Cf video
 
Ici, on peut concaténer les csv et changer le nom de colonne en stock_name sans utiliser de batch activity, juste avec copy data grâce aux fonctionnalités de bases dans data factory. Sinon, on peut utiliser le fichier etl.py dans batch activity.

![image](https://user-images.githubusercontent.com/57401552/210833575-9d651dd8-f523-4c99-8e7e-3293883ce5e6.png)

 
 ### Analyse sur Databricks 
 
 Cf notebook



