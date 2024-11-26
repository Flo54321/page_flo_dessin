# Import des bibliothèques

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

# Import de 2 datasets de seaborn

flights = sns.load_dataset("flights")
tips = sns.load_dataset("tips")

# Mise en page du dashboard

# 1- Titre

st.title("Manipulation de données et création de graphiques")

# 2- Sélection du dataset via une selectbox

dataset_name = st.selectbox("Quel dataset souhaites-tu utiliser ?", ['flights', 'tips'])

# Afficher le dataset en fonction du choix
if dataset_name == 'flights':
    # Charger le dataset 'flights' de seaborn
    data = flights
    st.write("Voici le dataset 'flights' :")
    st.dataframe(data, hide_index=True)  # Afficher le dataset sous forme de dataframe

elif dataset_name == 'tips':
    # Charger le dataset 'tips' de seaborn
    data = tips
    st.write("Voici le dataset 'tips' :")
    st.dataframe(data, hide_index=True)


# 3- Choix des colonnes X et Y en fonction du dataset

if dataset_name == 'flights':
    colonne_x_flights = st.selectbox("Choisissez la colonne X", ['year', 'month', 'passengers'])
    colonne_y_flights = st.selectbox("Choisissez la colonne Y", ['year', 'month', 'passengers'])

elif dataset_name == 'tips':
    colonne_x_tips = st.selectbox("Choisissez la colonne X", ['total_bill', 'tip', 'sex', 'smoker', 'time', 'size'])
    colonne_y_tips = st.selectbox("Choisissez la colonne Y", ['total_bill', 'tip', 'sex', 'smoker', 'time', 'size'])

# 4- Choix du chart

chart_choice = st.selectbox("Quel dgraphique souhaites-tu utiliser ?", ['Bar_chart', 'Scatter_chart', 'Line_chart'])




# 5- Affichage du graphique en fonction des axes et graphique choisis

# condition bar_chart
if chart_choice == 'Bar_chart':
    if dataset_name == 'flights':
        st.write(f"Bar chart pour {colonne_x_flights} et {colonne_y_flights}")
        chart = sns.barplot(x=colonne_x_flights, y=colonne_y_flights, data=data)
        st.pyplot(chart.figure)
        
    elif dataset_name == 'tips':
        st.write(f"Bar chart pour {colonne_x_tips} et {colonne_y_tips}")
        chart = sns.barplot(x=colonne_x_tips, y=colonne_y_tips, data=data)
        st.pyplot(chart.figure)

# condition scatter_chart
elif chart_choice == 'Scatter_chart':
    if dataset_name == 'flights':
        st.write(f"Scatter chart pour {colonne_x_flights} et {colonne_y_flights}")
        chart = sns.scatterplot(x=colonne_x_flights, y=colonne_y_flights, data=data)
        st.pyplot(chart.figure)
        
    elif dataset_name == 'tips':
        st.write(f"Scatter chart pour {colonne_x_tips} et {colonne_y_tips}")
        chart = sns.scatterplot(x=colonne_x_tips, y=colonne_y_tips, data=data)
        st.pyplot(chart.figure)

# condition pour line_chart
elif chart_choice == 'Line_chart':
    if dataset_name == 'flights':
        st.write(f"Line chart pour {colonne_x_flights} et {colonne_y_flights}")
        chart = sns.lineplot(x=colonne_x_flights, y=colonne_y_flights, data=data)
        st.pyplot(chart.figure)
        
    elif dataset_name == 'tips':
        st.write(f"Line chart pour {colonne_x_tips} et {colonne_y_tips}")
        chart = sns.lineplot(x=colonne_x_tips, y=colonne_y_tips, data=data)
        st.pyplot(chart.figure)

# 6- Checkbox pour afficher ou non la matrice de corrélation
show_corr = st.checkbox('Afficher la matrice de corrélation', key='corr_checkbox')

if show_corr:
    st.write("Matrice de corrélation")

    # Vérifier quel dataset est sélectionné et calculer la matrice de corrélation en fonction des choix X et Y
    if dataset_name == 'flights':
        # Sélectionner les colonnes choisies par l'utilisateur et exclure les colonnes non numériques
        columns_to_use = [colonne_x_flights, colonne_y_flights]
        
        # Exclure les colonnes non numériques (comme 'month' dans 'flights')
        correlation_data = data[columns_to_use]
        correlation_data = correlation_data.select_dtypes(include=[np.number])  # Garde que les colonnes numériques
        
        # Calculer la matrice de corrélation
        corr_matrix = correlation_data.corr()

    elif dataset_name == 'tips':
        # Sélectionner les colonnes choisies par l'utilisateur et exclure les colonnes non numériques
        columns_to_use = [colonne_x_tips, colonne_y_tips]
        
        # Exclure les colonnes non numériques (comme 'sex', 'smoker', 'time' dans 'tips')
        correlation_data = data[columns_to_use]
        correlation_data = correlation_data.select_dtypes(include=[np.number])  # Garde que les colonnes numériques
        
        # Calculer la matrice de corrélation
        corr_matrix = correlation_data.corr()


    # Affichage de la matrice de corrélation avec Seaborn heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)  # Affichage du graphique



