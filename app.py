
import streamlit as st
import pandas as pd
import json

st.set_page_config(layout="wide", page_title="Dashboard de Estoque")

# --- Carregar Dados ---
@st.cache_data
def load_data():
 with open(\'/home/ubuntu/dashboard-estoque/dados-estoque.json\', \'r\', encoding=\'utf-8\') as f:      data = json.load(f)
    df = pd.DataFrame(data)
    # Converter colunas numéricas que podem ter sido lidas como string
    df['Capacidade'] = pd.to_numeric(df['Capacidade'], errors='coerce')
    df['Quantidade/palete'] = pd.to_numeric(df['Quantidade/palete'], errors='coerce')
    df['Quantidade Total'] = pd.to_numeric(df['Quantidade Total'], errors='coerce')
    df['Qtd. de Palete'] = pd.to_numeric(df['Qtd. de Palete'], errors='coerce')
    return df

df = load_data()

# --- Funções de Cálculo de Estatísticas ---
def calculate_stats(data_frame):
    total_paletes = data_frame['Qtd. de Palete'].sum() if 'Qtd. de Palete' in data_frame.columns else 0
    total_quantidade = data_frame['Quantidade Total'].sum() if 'Quantidade Total' in data_frame.columns else 0
    
    posicoes_unicas = data_frame['Posição atual'].nunique() if 'Posição atual' in data_frame.columns else 0
    capacidade_media = data_frame['Capacidade'].mean() if 'Capacidade' in data_frame.columns else 0
    posicoes_cadastradas = posicoes_unicas * capacidade_media

    produtos_unicos = data_frame['Produto'].nunique() if 'Produto' in data_frame.columns else 0

    # Utilização Média (calculada de forma similar ao React app)
    utilizacao_media = 0
    if not data_frame.empty and 'Quantidade Total' in data_frame.columns and 'Capacidade' in data_frame.columns:
        # Soma das proporções de utilização de cada item / número de itens * 100
        # No React app, era data.reduce((sum, r) => sum + (r['Quantidade Total'] / r['Capacidade']), 0) / data.length * 100
        # Vamos replicar essa lógica com pandas
        valid_capacity_rows = data_frame[data_frame['Capacidade'] > 0]
        if not valid_capacity_rows.empty:
            utilizacao_media = (valid_capacity_rows['Quantidade Total'] / valid_capacity_rows['Capacidade']).sum() / len(valid_capacity_rows) * 100
        
    return {
        "totalPaletes": total_paletes,
        "totalQuantidade": total_quantidade,
        "posicoesCadastradas": posicoes_cadastradas,
        "produtosUnicos": produtos_unicos,
        "utilizacaoMedia": utilizacao_media
    }

# --- Layout do Streamlit ---
st.title("Dashboard de Estoque")
st.markdown("Gestão centralizada de paletes e produtos em tempo real")

# --- Barra de Busca e Filtros ---
search_term = st.text_input("🔍 Buscar por Produto, Posição ou ID Palete", "")

# Opções para filtros
capacidade_options = [''] + sorted(df['Capacidade'].dropna().astype(str).unique().tolist())
nivel_options = [''] + sorted(df['Nivel'].dropna().astype(str).str.split(',').explode().str.strip().unique().tolist())
drive_misturado_options = [''] + sorted(df['Drive Misturado'].dropna().astype(str).unique().tolist())

col1, col2, col3 = st.columns(3)
with col1:
    selected_capacidade = st.selectbox("Filtrar por Capacidade", capacidade_options)
with col2:
    selected_nivel = st.selectbox("Filtrar por Nível", nivel_options)
with col3:
    selected_drive_misturado = st.selectbox("Filtrar por Drive Misturado", drive_misturado_options)

# --- Filtrar Dados ---
filtered_df = df.copy()

if search_term:
    filtered_df = filtered_df[
        filtered_df['Produto'].astype(str).str.contains(search_term, case=False, na=False) |
        filtered_df['Posição atual'].astype(str).str.contains(search_term, case=False, na=False) |
        filtered_df['ID Palete'].astype(str).str.contains(search_term, case=False, na=False)
    ]

if selected_capacidade:
    filtered_df = filtered_df[filtered_df['Capacidade'].astype(str) == selected_capacidade]

if selected_nivel:
    filtered_df = filtered_df[filtered_df['Nivel'].astype(str).str.contains(selected_nivel, case=False, na=False)]

if selected_drive_misturado:
    filtered_df = filtered_df[filtered_df['Drive Misturado'].astype(str) == selected_drive_misturado]

# --- Exibir Estatísticas ---
stats = calculate_stats(filtered_df)

st.subheader("Estatísticas Gerais")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(label="Total de Paletes", value=f"{stats['totalPaletes']:.0f}")
with col2:
    st.metric(label="Quantidade Total", value=f"{stats['totalQuantidade']:.0f}")
with col3:
    st.metric(label="Posições Cadastradas", value=f"{stats['posicoesCadastradas']:.0f}")
with col4:
    st.metric(label="Produtos Diferentes", value=f"{stats['produtosUnicos']:.0f}")
with col5:
    st.metric(label="Utilização Média", value=f"{stats['utilizacaoMedia']:.2f}%")

st.markdown("--- ")

# --- Exibir Tabela de Dados ---
st.subheader("Registros de Estoque")
st.write(f"{len(filtered_df)} de {len(df)} registros")
st.dataframe(filtered_df, use_container_width=True)

# --- Footer ---
st.markdown("\n---")
st.markdown("Dashboard de Estoque © 2026 | Dados carregados de arquivo local")
st.markdown(f"Última atualização: {pd.Timestamp.now().strftime('%d/%m/%Y')}")
