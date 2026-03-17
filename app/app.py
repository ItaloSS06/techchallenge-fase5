import streamlit as st
import pandas as pd
import joblib

# Carregar modelo
model = joblib.load('app/modelo_risco.pkl')

st.title("Previsão de Risco de Defasagem")

st.write("Insira os dados do aluno:")

# Inputs
idade = st.number_input("Idade", min_value=0)
ida = st.number_input("IDA")
ieg = st.number_input("IEG")
iaa = st.number_input("IAA")
ips = st.number_input("IPS")
ipv = st.number_input("IPV")
fase = st.number_input("Fase")
matem = st.number_input("Nota Matemática")
portug = st.number_input("Nota Português")
cf = st.number_input("Cf")
cg = st.number_input("Cg")
ct = st.number_input("Ct")
genero = st.selectbox("Gênero", ["Menino", "Menina"])

# Converter gênero
genero_menino = 1 if genero == "Menino" else 0

# Botão
if st.button("Prever"):
    input_data = pd.DataFrame([{
        'IDA': ida,
        'IEG': ieg,
        'IAA': iaa,
        'IPS': ips,
        'IPV': ipv,
        'Fase': fase,
        'Idade 22': idade,
        'Matem': matem,
        'Portug': portug,
        'Cf': cf,
        'Cg': cg,
        'Ct': ct,
        'Gênero_Menino': genero_menino
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Risco de defasagem: {proba:.2%}")
    else:
        st.success(f"✅ Baixo risco: {proba:.2%}")
