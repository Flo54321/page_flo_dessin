<<<<<<< HEAD
import streamlit as st
import pandas as pd

st.title("Bienvenue sur le site web de FLORINDA !")

st.subheader("Oups, je ne suis pas allée jusqu'au bout de la lecture, j'ai donc pris mon propre dataset, merci pour votre compréhension !")

option = st.selectbox(
    "Indiquez le nom de votre personnage",
    ("Léolio", "Gon", "Tanjirō", "M. KORO", "Biscuit Kruger", "Nan"),
)

if option == "Léolio":
    st.write("You selected:", option)
    st.image("IMG_20220917_154318.jpg")
    

elif option == "Gon":
    st.write("You selected:", option)
    st.image("IMG_20220917_160548.jpg")
    

elif option == "Tanjirō":
    st.write("You selected:", option)
    st.image("IMG_20220924_135811.jpg")
    

elif option == "M. KORO":
    st.write("You selected:", option)
    st.image("IMG_20220911_162354.jpg")
    

elif option == "Biscuit Kruger":
    st.write("You selected:", option)
    st.image("IMG_20220928_190432.jpg")
    
else:
    st.write("You selected:", option)
    st.image("NAN.png")
=======
import streamlit as st
import pandas as pd

st.title("Bienvenue sur le site web de FLORINDA !")

st.subheader("Oups, je ne suis pas allée jusqu'au bout de la lecture, j'ai donc pris mon propre dataset, merci pour votre compréhension !")

option = st.selectbox(
    "Indiquez le nom de votre personnage",
    ("Léolio", "Gon", "Tanjirō", "M. KORO", "Biscuit Kruger", "Nan"),
)

if option == "Léolio":
    st.write("You selected:", option)
    st.image("IMG_20220917_154318.jpg")
    

elif option == "Gon":
    st.write("You selected:", option)
    st.image("IMG_20220917_160548.jpg")
    

elif option == "Tanjirō":
    st.write("You selected:", option)
    st.image("IMG_20220924_135811.jpg")
    

elif option == "M. KORO":
    st.write("You selected:", option)
    st.image("IMG_20220911_162354.jpg")
    

elif option == "Biscuit Kruger":
    st.write("You selected:", option)
    st.image("IMG_20220928_190432.jpg")
    
else:
    st.write("You selected:", option)
    st.image("NAN.png")
>>>>>>> 4b2bf8e543d559780ed5c6484dca13a2d9c5000a
    