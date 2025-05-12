import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Texto para Áudio", layout="centered")

st.title("🔊 Conversor de Texto para Áudio (gTTS)")
texto = st.text_area("Digite o texto em português que deseja converter para áudio:", height=200)

if texto.strip():
    try:
        tts = gTTS(text=texto, lang='pt-br')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            with open(tmp.name, "rb") as f:
                audio_bytes = f.read()

        st.audio(audio_bytes, format="audio/mp3")
        st.download_button("💾 Baixar MP3", data=audio_bytes, file_name="audio.mp3", mime="audio/mpeg")

    except Exception as e:
        st.error(f"Erro ao gerar áudio: {e}")
