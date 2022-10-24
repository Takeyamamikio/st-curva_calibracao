import streamlit as st

st.title("Relatório de ocorrências")

with st.form(key="Responsável"):
    nome = st.text_input(label="Nome:")
    button = st.form_submit_button("enviar")
