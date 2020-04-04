-[_Parcours Openclassrooms_](https://openclassrooms.com/fr/projects/157/assignment)-

# Projet5

## Utilisez les données publiques d'[Open Food Facts][1]

---
## Énoncé

> La startup _Pur Beurre_ travaille connait bien les habitudes alimentaires françaises. Leur restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs sur la butte de Montmartre.

> L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer. Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ? Leur idée est donc de créer un programme qui interagirait avec la base [Open Food Facts][1] pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

## Fonctionnalités 

- Recherche d'aliments dans la base Open Food Facts
- Affichage de fiches produits
- L'utilisateur :
  * Interagit avec le système dans le terminal
  * Enregistre les produits pour les retrouver plus tard 
- L'utilisateur choisit en tapant des chiffres

## Étapes

1. Organiser son travail
2. L'organiser dans un tableau [Trello][2]
3. Écrire la documentation
4. Coder

## Contraintes

- Le code sera écrit en anglais : variables, noms de fonctions, commentaires, documentation, ...
- Le projet sera versionné et publié sur Github.

## Livrables

- [Tableau Trello][2]
- [Modèle physique de données][3]
- Script de création de la base de données
- [Code source publié sur Github][4]
- Document texte en format pdf n'excédant pas 2 pages contenant :
  * la démarche choisie
  * les difficultés rencontrées/solutions trouvées
  * le lien _Github_
  * le choix de l'algorithme et la méthodologie choisie
  
## Installation:

### 1 - Environnement virtuel :

Créer un environnement virtuel :
```
virtualenv -p python3 env
```
### 2 - Requirements:
```
Pour installer toutes les dépendances requises, ouvrir l'invite de commande et utiliser pip : 
pip install -r requirements.txt
```
### 3 - Modifier votre username et votre password:
```
Dans le fichier constants.py, modifier votre username et votre password afin de vous connecter à la base de données
```
### 4 - Lancer le programme :
```
python main.py
```
[1]: https://fr.openfoodfacts.org/
[2]: https://trello.com/b/edCZfAZI/projet-5
[3]: https://github.com/raoofrachidi/Projet-5/blob/master/P5_01_mod%C3%A8ledonn%C3%A9es.png
[4]: https://github.com/raoofrachidi/Projet-5/tree/master/P5_03_codesource
