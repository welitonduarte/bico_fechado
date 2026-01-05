import pandas as pd
import streamlit as st

# -----------------------------
# Configuração inicial
# -----------------------------
st.set_page_config(page_title="Bico Fechado", page_icon="🤐", layout="centered")

st.title("🤐 Bico Fechado")

# -----------------------------
# Caminhos dos arquivos
# -----------------------------

ARQUIVOS = {
    "Intermediário": "bico_fechado_intermediario.csv",
    "Avançado": "bico_fechado_avancado.csv"
}

# -----------------------------
# Seleção de nível
# -----------------------------
nivel = st.selectbox(
    "Selecione o nível do jogo:",
    options=["Intermediário", "Avançado"]
)

# -----------------------------
# Carregar base
# -----------------------------
df = pd.read_csv(ARQUIVOS[nivel])

# -----------------------------
# Botão de gerar palavra
# -----------------------------
if st.button("🎲 Gerar palavra"):
    selecionado = df.sample(1).iloc[0]

    st.markdown("---")
    #st.subheader("🎭 Palavra")
    st.info(f"## **{selecionado['palavra']}**")

    #st.subheader("💡 Dica")
    st.warning(f"### {selecionado['categoria']}")