import streamlit as st
from gtts import gTTS
import os
import tempfile

st.set_page_config(page_title="Texto para Áudio", layout="centered")

st.title("🔊 Conversor de Texto para Áudio (gTTS)")
texto = st.text_area("Digite o texto em português que deseja converter para áudio:", height=200)

col1, col2 = st.columns(2)

if col1.button("▶️ Ouvir Áudio"):
    if texto.strip():
        try:
            tts = gTTS(text=texto, lang='pt-br')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                caminho_audio = tmp.name
                tts.save(caminho_audio)
                st.audio(caminho_audio, format="audio/mp3")
        except Exception as e:
            st.error(f"Erro ao gerar o áudio: {e}")
    else:
        st.warning("Digite algum texto antes de ouvir.")

if col2.download_button("💾 Baixar MP3", data=None, file_name="audio.mp3", disabled=True):
    st.warning("Use o botão de ouvir primeiro para gerar o áudio.")

# Correção: ativa botão de download somente após gerar o áudio
if texto.strip():
    try:
        tts = gTTS(text=texto, lang='pt-br')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            with open(tmp.name, "rb") as f:
                audio_bytes = f.read()
                st.download_button("💾 Baixar MP3", data=audio_bytes, file_name="audio.mp3", mime="audio/mpeg")
    except Exception as e:
        st.error(f"Erro ao preparar o download: {e}")