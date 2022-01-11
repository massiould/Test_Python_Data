# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:05:34 2022 

@author: Massi
"""
import pandas as pd
import matplotlib.pyplot as plt
#Transformation du fichier CSV en dataframe

film_dataframe = pd.read_csv("IMDB-Movie-Data.csv")
print(Film_Dataframe)

#Calcul de la moyenne des notes 
moyenne_note = film_dataframe['Rating'].mean()
print(moyenne_note)

#Calcul  des notes par réalisateur , ainsi que le total au box-office
notes_realisateur_boxoffice= film_dataframe.groupby(['Director'])['Rating','Revenue (Millions)'].mean()
print (notes_realisateur_boxoffice)
# exportation de ce dataframme en un fichier CSV
notes_realisateur_boxoffice.to_csv('notes_realisateur_boxoffice.csv')

# A vrai dire je n'ai pas tres bien compris cette question et je ne vois pas comment mettre en lien la valeur de 
#l'inflation et le revenue par manque de temps
Inflation = pd.read_csv("DP_LIVE_11012022200816304.csv")
Inflation.drop(columns=["LOCATION", "INDICATOR", "SUBJECT", "MEASURE","FREQUENCY","Flag Codes"])

#Graphique de la representation de la moyenne des notes de films par an
graphique=film_dataframe.groupby(['Year'])['Rating'].mean().plot()

plt.savefig('Graphique de la moyenne des notes de films par an .jpeg')
#Creation d'une matrice de correlation afin de voir les impacts les plus remarquant sur le score

corr_df = film_dataframe.corr()

print(corr_df)

#Selon la matrice de correlation les parametres qui impacte sur le score sont :
#1 le metascore avec un score de 0.63
#2 les votes avec un score de 0.51

#les autres parametre qui semble avoir un faible impact sont :
#le Runtimes ainsi que le revenue