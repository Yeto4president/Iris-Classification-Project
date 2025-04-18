# Iris-Classification-Project
# 🌸 Classification du Dataset Iris - Comparaison d'Algorithmes ML

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📌 Enjeux du Projet

Ce projet explore un problème fondamental en machine learning : **la classification multi-classe**. À travers le dataset Iris (un benchmark classique), nous répondons à plusieurs enjeux cruciaux :

1. **Comparaison objective d'algorithmes** :  
   Quels modèles performent le mieux sur un jeu de données bien équilibré mais avec des frontières de décision complexes ?

2. **Impact du pré-traitement** :  
   Analyse de l'influence de la normalisation des features sur des algorithmes sensibles aux échelles (comme KNN).

3. **Interprétabilité vs Performance** :  
   Dilemme entre modèles "boîte noire" (Random Forest) et modèles interprétables (Arbres de décision).

4. **Robustesse aux overfitting** :  
   Évaluation par validation croisée pour identifier les modèles qui généralisent le mieux.

## 🎯 Applications Concrètes

Les enseignements de ce projet s'appliquent à des problématiques réelles :

- **Botanique automatisée** : Classification d'espèces végétales par morphométrie
- **Diagnostic médical** : Reconnaissance de patterns dans des mesures biologiques
- **Contrôle qualité industriel** : Catégorisation de produits basée sur des caractéristiques physiques

## 🔍 Insights Clés

| Modèle               | Avantages                          | Limitations                          | Cas d'usage idéal                |
|----------------------|------------------------------------|--------------------------------------|----------------------------------|
| **KNN**              | Simple, pas d'entraînement formel  | Coûteux en calcul pour grands datasets | Prototypage rapide              |
| **Arbre de Décision**| Interprétable, handles non-linéarité | Tendance à overfitter               | Besoin d'explicabilité          |
| **Random Forest**    | Robustesse, haute performance      | Complexité computationnelle         | Applications critiques           |
| **Régression Log.** | Probabilités calibrées             | Limité aux relations linéaires       | Quand on besoin de scores        |

# Classification sur le Dataset Iris
## Progression du Notebook

![Dernière exécution](https://github.com/votre-user/mon-projet/workflows/Notebook%20Staged%20Execution/badge.svg)

[📊 Voir les derniers résultats](https://github.com/votre-user/mon-projet/actions)
## 🚀 Fonctionnalités
- Comparaison de 4 algorithmes de ML
- Visualisation complète des données
- Métriques d'évaluation détaillées

## 📊 Résultats Principaux
| Modèle               | Accuracy | AUC-ROC |
|----------------------|----------|---------|
| KNN                  | 0.97     | 0.99    |
| Decision Tree        | 0.93     | 0.96    |
| Random Forest        | 0.98     | 1.00    |
| Logistic Regression  | 0.96     | 0.99    |

## 🔧 Installation
```bash
git clone https://github.com/votre-user/iris-classification.git
pip install -r requirements.txt

```bash
git clone https://github.com/votre-utilisateur/iris-ml-benchmark.git
cd iris-ml-benchmark
pip install -r requirements.txt
jupyter notebook notebooks/Iris_Analysis.ipynb
