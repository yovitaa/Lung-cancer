import pickle
import streamlit as st

lungcancer_model = pickle.load(open('model.pkl', 'wb'))

st.title('Data Mining Prediksi Kanker Paru-Paru')

col1, col2 = st.columns(2)

with col1:
    GENDER = st.selectbox(
        ("Ya", "Tidak"),
    )

with col2:
    AGE = st.text_input ('Umur')

with col1:
    SMOKING = st.selectbox(
        ("Ya", "Tidak"),
    )

with col2:
    YELLOW_FINGERS = st.selectbox(
        ("Ya", "Tidak"),
    )

with col1:
    ANXIETY = st.selectbox(
        ("Ya", "Tidak"),
    )

with col2:
    PEER_PRESSURE = st.selectbox(
        ("Ya", "Tidak"),
    )

with col1:
    CHRONIC_DISEASE = st.selectbox(
        ("Ya", "Tidak"),
    )

with col2:
    FATIGUE = st.selectbox(
        ("Ya", "Tidak"),
    )

with col1:
    ALLERGY = st.selectbox(
        ("Ya", "Tidak"),
    )

with col2:
    WHEEZING = st.selectbox(
        ("Ya", "Tidak"),
    )

with col1:
    ALCOHOL_CONSUMING = st.selectbox(
        "ALCOHOL CONSUMING",
        ("Ya", "Tidak"),
    )

with col2:
    COUGHING = st.selectbox(
        ("Ya", "Tidak"),
    )

with col1:
    SHORTNESS_OF_BREATH = st.selectbox(
        ("Ya", "Tidak"),
    )

with col2:
    SWALLOWING_DIFFICULTY = st.selectbox(
        ("Ya", "Tidak"),
    )

with col1:
    CHEST_PAIN = st.selectbox(
        ("Ya", "Tidak"),
    )

lungcancer_diagnosis = ''

if st.button('Test Prediksi Kanker Paru-Paru') :
    lungcancer_prediction = lungcancer_model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY ,WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

    if(lungcancer_diagnosis[0] == 1) :
        lungcancer_diagnosis = 'Pasien Terkena Kanker Paru-Paru'
    else:
        lungcancer_diagnosis = 'Pasien Tidak Terkena Kanker Paru-Paru'
st.success(lungcancer_diagnosis)
