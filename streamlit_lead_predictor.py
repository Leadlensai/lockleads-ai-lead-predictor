
import streamlit as st
import joblib
import numpy as np

# Laad het AI-model
model = joblib.load("ai_lead_verkoopmodel_compatible.pkl")

st.title("🏡 AI Vastgoed Lead Voorspeller")

st.write("Voer de kenmerken van een potentiële lead in en zie of ze waarschijnlijk hun woning zullen verkopen.")

# Invoervelden voor gebruiker
zoekgedrag_funda = st.slider("Hoe vaak zoekt deze persoon naar huizen?", 0, 10, 5)
recent_verhuisd = st.radio("Heeft deze persoon recent een woning gekocht?", [0, 1])
social_media_interactie = st.slider("Hoe actief is deze persoon op vastgoed social media?", 0, 10, 5)
woningwaarde_gestegen = st.radio("Is de woningwaarde in hun regio gestegen?", [0, 1])
leeftijd = st.slider("Leeftijd van de persoon", 25, 75, 40)
woning_te_koop_in_buurt = st.radio("Zijn er veel woningen te koop in hun buurt?", [0, 1])
inkomensverandering = st.radio("Heeft deze persoon recent een inkomensverandering meegemaakt?", [0, 1])

# Maak een voorspelling
if st.button("🔮 Voorspel of deze persoon zal verkopen"):
    lead_data = np.array([[zoekgedrag_funda, recent_verhuisd, social_media_interactie,
                           woningwaarde_gestegen, leeftijd, woning_te_koop_in_buurt, inkomensverandering]])
    voorspelling = model.predict(lead_data)
    resultaat = "✅ Waarschijnlijk wel" if voorspelling[0] == 1 else "❌ Waarschijnlijk niet"
    st.success(f"Deze persoon zal {resultaat} hun woning verkopen.")
