import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import os
import tempfile
import pygame

def ouvir_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if texto:
        try:
            tts = gTTS(text=texto, lang='pt-br')

            # Cria arquivo temporário corretamente
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_path = temp_audio.name

            tts.save(temp_path)

            # Inicia o mixer
            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            # Espera até o áudio terminar
            while pygame.mixer.music.get_busy():
                janela.update()

            # Encerra e descarrega mixer para liberar o arquivo
            pygame.mixer.music.stop()
            pygame.mixer.quit()

            # Agora o arquivo pode ser removido com segurança
            os.unlink(temp_path)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao reproduzir o áudio: {e}")
    else:
        messagebox.showwarning("Aviso", "Digite algum texto antes de ouvir.")

def exportar_mp3():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if texto:
        caminho = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                filetypes=[("MP3 files", "*.mp3")])
        if caminho:
            try:
                tts = gTTS(text=texto, lang='pt-br')
                tts.save(caminho)
                messagebox.showinfo("Sucesso", f"Áudio salvo em: {caminho}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar o áudio: {e}")
    else:
        messagebox.showwarning("Aviso", "Digite algum texto antes de exportar.")

# Criação da interface
janela = tk.Tk()
janela.title("Google TTS - Texto para Fala")
janela.geometry("500x400")

tk.Label(janela, text="Digite o texto:", font=("Arial", 12)).pack(pady=10)

entrada_texto = tk.Text(janela, height=10, wrap=tk.WORD, font=("Arial", 11))
entrada_texto.pack(padx=20, fill=tk.BOTH, expand=True)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_ouvir = tk.Button(frame_botoes, text="🔊 Ouvir Áudio", command=ouvir_texto, bg="#0580C1", fg="white", width=15)
botao_ouvir.grid(row=0, column=0, padx=10)

botao_exportar = tk.Button(frame_botoes, text="💾 Exportar MP3", command=exportar_mp3, bg="#0A8754", fg="white", width=15)
botao_exportar.grid(row=0, column=1, padx=10)

janela.mainloop()
