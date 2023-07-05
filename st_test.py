import streamlit as st
import pandas as pd

def calcular_curva_calibracao(num_pontos, concentracao_solucao_mae, volume_diluido, concentracoes_desejadas):
    volume_solucao_mae = []
    volume_solvente = []

    for i, conc_desejada in enumerate(concentracoes_desejadas):
        vol_solucao_mae = volume_diluido * conc_desejada / concentracao_solucao_mae
        vol_solvente = volume_diluido - vol_solucao_mae
        volume_solucao_mae.append(vol_solucao_mae)
        volume_solvente.append(vol_solvente)

    return volume_solucao_mae, volume_solvente

def main():
    st.title("Cálculo de Preparo de Soluções Padrões para Curva de Calibração")

    num_pontos = st.number_input("Número de Pontos para a Curva de Calibração", min_value=1, step=1, value=5)
    concentracao_solucao_mae = st.number_input("Concentração da Solução Mãe (em unidades de sua escolha)", min_value=0.0, step=0.01, value=1.0)
    volume_diluido = st.number_input("Volume da Solução Diluída para cada Ponto (em unidades de sua escolha)", min_value=0.0, step=0.01, value=10.0)

    # Entrada das concentrações desejadas para cada ponto
    concentracoes_desejadas = []
    for i in range(num_pontos):
        conc_desejada = st.number_input(f"Concentração desejada para o Ponto {i+1}", min_value=0.0, step=0.01, value=1.0)
        concentracoes_desejadas.append(conc_desejada)

    if st.button("Calcular"):
        volume_solucao_mae, volume_solvente = calcular_curva_calibracao(num_pontos, concentracao_solucao_mae, volume_diluido, concentracoes_desejadas)

        # Criar DataFrame
        dados = {
            "Ponto": list(range(1, num_pontos + 1)),
            "Sol. mãe (ml)": volume_solucao_mae,
            "Solvente (ml)": volume_solvente
        }
        df_resultado = pd.DataFrame(dados)

        # Exibir DataFrame
        st.write("Quantidade de Solução Mãe e Solvente para cada Ponto:")
        st.dataframe(df_resultado)

if __name__ == "__main__":
    main()


