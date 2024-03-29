# TP3 : modifier le contenu d'une table

Pour commencer, [ouvrir dans Basthon le notebook exemple](https://notebook.basthon.fr/?kernel=sql&from=https://raw.githubusercontent.com/thfruchart/tnsi/main/02/exemple.ipynb&module=https://raw.githubusercontent.com/thfruchart/tnsi/main/02/livres.sql).

### que peut-on modifier dans une base de données ? 

Toutes les modifications présentées dans ce TP portent sur les **lignes** d'une **table**.

De manière générale, une fois qu'une base de données est créée, les intitulés des colonnes des tables (appelés "champs") ne sont plus modifiés. 
Seules les lignes sont modifiées de façon ordinaire, pour mettre à jour les informations stockées dans la base.

On distingue trois sortes de "modifications" :
1. Modifier certaines valeurs d'une ligne existante
2. Ajouter une nouvelle ligne dans une table
3. Supprimer une ou plusieurs lignes d'une table.



## 1. Modification de certaines lignes

**Prolonger un emprunt**  
Exécuter la requête : 
* `SELECT * FROM emprunt WHERE retour='2020-01-01';`

On obtient les deux lignes de la table emprunt pour lesquelles le retour est fixé au premier janvier 2020.

|code_barre	|isbn	|retour	|
|:--|:--|:--|
|934701281931582	|978-2260019183	|2020-01-01	|
|934701281931582	|978-2371240087	|2020-01-01|


L'objectif est de "prolonger  pour un mois" l'emprunt du livre dont l'isbn est 978-2260019183, c'est à dire de modifier uniquement la date de retour de cet ouvrage au 1er février 2020.

Exécuter : 
* `UPDATE emprunt SET retour='2020-02-01' WHERE isbn=  '978-2260019183';`
* `SELECT * FROM emprunt WHERE isbn=  '978-2260019183';`

On peut vérifier que la date de retour pour cet ouvrage a bien été modifiée.

|code_barre	|isbn	|retour	|
|:--|:--|:--|
|934701281931582	|978-2260019183	|2020-**02**-01|

Exécuter : 
* `SELECT * FROM emprunt WHERE retour='2020-01-01';`

On obtient alors une seule ligne de la table emprunt pour laquelle le retour reste fixé au premier janvier 2020. 
En effet, nous n'avons modifié qu'une seule ligne de la table emprunt. 

|code_barre	|isbn	|retour	|
|:--|:--|:--|
|934701281931582	|978-2371240087	|2020-01-01|


**prolonger tous les emprunts d'un usager**
On souhaite prolonger jusqu'au 18 mars 2020 tous les livres empruntés par l'usager dont le code barre est : 035184062854281

Exécuter : 
* `SELECT * FROM emprunt WHERE code_barre='035184062854281';`
* `UPDATE emprunt SET retour='2020-03-18' WHERE code_barre='035184062854281';`
* `SELECT * FROM emprunt WHERE code_barre='035184062854281';`



Remarquer que l'exécution de la requête UPDATE modifie **3** lignes. 

|code_barre	|isbn	|retour	|
|:--|:--|:--|	
|035184062854281|	978-2072762093|	2020-03-18	|
|035184062854281|	978-2742744824|	2020-03-18	|
|035184062854281|	978-2745989857|	2020-03-18	|

## UPDATE `table` SET ... WHERE ...
**-A RETENIR**  
Syntaxe d'une requête qui **modifie** certaines valeurs dans une (ou plusieurs) ligne(s) :

**`UPDATE nom_de_la_table  SET  nom_de_colonne_modifiée1 = valeur1 , nom_de_colonne_modifiée2 = valeur2 WHERE condition;`**

## 2. Ajout de nouvelles lignes
Valérie MICHEL (qui a pour code-barre 199614051174633) souhaite emprunter le livre '1984' dont l'isbn  est 978-0547249643.

Pour saisir ce nouvel emprunt dans la base de données, on **ajoute** une nouvelle ligne dans la **table** emprunt :

Exécuter : 
* `INSERT INTO emprunt(code_barre, isbn, retour) VALUES ('199614051174633', '978-0547249643', '2020-12-24');`

Puis vérifier dans la table emprunt que ce nouvel emprunt est ajouté : 
* `SELECT * FROM emprunt WHERE code_barre='199614051174633';`

## INSERT INTO `table` VALUES ... 
Syntaxe pour ajouter une nouvelle ligne dans une table : 

**`INSERT INTO nom_de_la_table VALUES (valeur1, valeur2...);`**  
Les valeurs sont à écrire dans l'ordre des champs de la table.  

Remarque : on peut aussi utiliser la syntaxe suivante :  
`INSERT INTO nom_de_la_table(colonne1, colonne2...) VALUES (valeur1, valeur2...);`  
C'est utile lorsque certaines valeurs sont laissées vides (`NULL` en SQL).


## 3. Suppression de lignes
La commande pour supprimer une ou plusieurs lignes d'une table suit la syntaxe : 

## DELETE FROM `table` WHERE condition;

ATTENTION : 
* une opération de suppression est irréversible ! 
* il est fortement conseille d'effectuer une sauvegarde de sa base de données AVANT de supprimer quoi que ce soit.
* on n'insistera jamais trop sur la **condition** qui permet de définir quelles lignes seront supprimées.
   * un simple `DELETE FROM table` efface TOUTES les lignes de la table ! 

CONSEIL : 
*  commencer par une requête de SÉLECTION des données qu'on souhaite supprimer

Exécuter : 
* `SELECT * FROM emprunt WHERE isbn='978-0547249643';`

Après avoir vérifié que cette condition correspond bien au livre que Valérie vient de rapporter, on peut supprimer la ligne avec : 
* `DELETE FROM emprunt WHERE isbn='978-0547249643';`

Cela permet ensuite d'ajouter dans la base l'emprunt de ce livre par un autre utilisateur, par exemple Julien :
* `INSERT INTO emprunt(code_barre, isbn, retour) VALUES ('782124241492509', '978-0547249643', '2020-12-31');`

Cette insertion se fait alors sans provoquer d'erreur.

# Exercice 3
Écrire les requêtes permettant de réaliser les objectifs suivants
1. Inscrire un nouvel usager : vous !
2. Effectuer pour vous-même un emprunt, pour le livre que vous choisissez, et pour une durée de deux semaines. 
3. Prolonger cet emprunt d'une semaine.
4. Effectuer pour vous-même l'emprunt d'un livre rendu par un autre usager : il faudra donc effectuer deux requêtes.
   1. la première pour "retourner le livre", rendu par l'autre usager.
   2. la deuxième pour "emprunter le livre" à votre tour. 
