import streamlit as st
import pandas as pd

st. title("DJ Arthur, tudo menos conhecimento")
st.sidebar.title("escolha o seu artista favorito")
st.sidebar.image('logo.png')

#criando um df
df = pd.read_parquet('Dados_Artistas.parquet')

#select box ao lado
artistas = st.sidebar.selectbox('Selecione o artista', df['Artist'].sort_values().unique())
df_artista = df[df['Artist'] == artistas]

## informação da pagina principal
st.subheader(f'playlist dos imunes aqui só toca pedrada e matue infelismente!!')
st.subheader(f'O artista escolhido foi {artistas}')

##looping
for index, row in df_artista.iterrows():
        with st.container():
            st.markdown(f"### 🎵 **{row['Track']}**")
            
            col1, col2 = st.columns(2)
            col1.metric("🎵 Spotify Streams", f"{row['Stream']:,.0f}")
            col2.metric("📺 YouTube Views", f"{row['Views']:,.0f}")
            
            st.video(row['Url_youtube'])
            st.markdown("---")
            st.link_button('ouça no spotify',url=row['Url_spotify'], type='primary')