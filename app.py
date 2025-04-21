import streamlit as st
import time
import numpy as np
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Maladie Thyroïdienne",
    layout="wide",
    page_icon="🧠"
)

# Titre principal
st.markdown("""
<div style='display: flex; align-items: center;'>
    <span style='font-size: 45px; margin-right: 15px;'>🧬</span>
    <h1 style='font-family: serif; color: #4B0082;'>Application de detection de maladie Thyroïdienne</h1>
</div>
""", unsafe_allow_html=True)

# Fonction de prédiction en utilisant le one-hot encoding
def predict_disease(input_data):
    # Exemple d'encodage one-hot (binaire)
    score = 0
    
    # Encodage des critères : chaque option est transformée en binaire
    if input_data['recidive'] == 'Oui':
        score += 1
    if input_data['tabagisme'] == 'Oui':
        score += 1
    if input_data['antecedents_radio'] == 'Oui':
        score += 1
    if input_data['focalite'] == 'Multi-Focale':
        score += 1

    # Autres critères de la tumeur, etc.
    if input_data['n_status'] == 'N1a' or input_data['n_status'] == 'N1b':
        score += 1
    if input_data['m_status'] == 'M1':
        score += 1
    if input_data['t_status'] in ['T3a', 'T3b', 'T4a', 'T4b']:
        score += 1

    # Logique de prédiction basée sur un score simple
    if score >= 4:
        return 'Risque Élevé de maladie thyroïdienne'
    elif score == 3:
        return 'Risque Intermédiaire de maladie thyroïdienne'
    else:
        return 'Risque Faible de maladie thyroïdienne'

# Page de prédiction
st.markdown("<h2 style='color:#4B0082;'>Entrez les informations cliniques :</h2>", unsafe_allow_html=True)

with st.form("thyroid_form"):
    col1, col2 = st.columns(2)

    # Formulaire à gauche
    with col1:
        age = st.number_input("Âge", min_value=0, max_value=120)
        stade = st.selectbox("Stade", ["I", "II", "III", "IVA", "IVB"])
        n_status = st.selectbox("N (implication ganglionnaire)", ["N0", "N1a", "N1b"])
        m_status = st.selectbox("M (présence de métastases à distance)", ["M0", "M1"])
        t_status = st.selectbox("T (taille et extension locale de la tumeur)", ["T1a", "T1b", "T2", "T3a", "T3b", "T4a", "T4b"])
        recidive = st.selectbox("Récidive", ["Oui", "Non"])
        tabagisme = st.selectbox("Tabagisme", ["Oui", "Non"])

    # Formulaire à droite
    with col2:
        antecedents_radio = st.selectbox("Antécédents Radiothérapie", ["Oui", "Non"])
        focalite = st.selectbox("Focalité", ["Uni-Focale", "Multi-Focale"])
        sexe = st.selectbox("Sexe", ["F", "M"])
        ant_tabac = st.selectbox("Antécédents Tabagisme", ["Oui", "Non"])
        examen = st.selectbox("Examen Physique", [
            "Normal", "Goître Diffus", "Goître Multinodulaire",
            "Goître Nodulaire Unique-Gauche", "Goître Nodulaire Unique-Droite"
        ])
        adenopathie = st.selectbox("Adénopathie", [
            "Non", "Bilatérale", "Étendue", "Gauche", "Droite", "Postérieure"
        ])
        reponse = st.selectbox("Réponse", [
            "Excellente", "Biochimique Incomplète",
            "Indéterminée", "Structurale Incomplète"
        ])

    submitted = st.form_submit_button("✨ Prédire maintenant", use_container_width=True)

if submitted:
    # Encodage one-hot : transforme les variables sélectionnées en format binaire
    input_data = {
        'age': age,
        'stade': stade,
        'n_status': n_status,
        'm_status': m_status,
        't_status': t_status,
        'recidive': recidive,
        'tabagisme': tabagisme,
        'antecedents_radio': antecedents_radio,
        'focalite': focalite,
        'sexe': sexe,
        'ant_tabac': ant_tabac,
        'examen': examen,
        'adenopathie': adenopathie,
        'reponse': reponse,
    }

    with st.spinner("🔄 Prédiction en cours..."):
        time.sleep(2)
        prediction = predict_disease(input_data)

    if prediction == 'Risque Faible':
        st.success(f"✅ Risque détecté : {prediction}")
        st.snow()
    elif prediction == 'Risque Intermédiaire':
        st.warning(f"⚠️ Risque détecté : {prediction}")
        st.balloons()
    else:
        st.error(f"🚨 Risque détecté : {prediction}")
        st.balloons()

# Footer
st.markdown("""
---
<center style='color: gray;'>© 2025 – Application conçue par <b>PIERRE EMERIC ANRAI</b></center>
""", unsafe_allow_html=True)
