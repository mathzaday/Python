import customtkinter as ctk

root = ctk.CTk()

root.title("UNIMAR Match")
root.geometry("700x500")
root.resizable(False, False)
root.configure(fg_color="#1E1E2E")

titulo = ctk.CTkLabel(root, text="UNIMAR MATCH", font=ctk.CTkFont(size=30, weight="bold"))
titulo.pack(pady=60)

subtitulo = ctk.CTkLabel(root, text="Encontre pessoas com interesses parecidos com os seus.", font=ctk.CTkFont(size=16))
subtitulo.pack(pady=10)

nome = ctk.CTkEntry(root, placeholder_text="Digite seu nome", width=300)

curso = ctk.CTkEntry(root, placeholder_text="Digite seu curso", width=300)

interesse1 = ctk.CTkCheckBox(root, text="Programação")
interesse2 = ctk.CTkCheckBox(root, text="Jogos")
interesse3 = ctk.CTkCheckBox(root, text="Esportes")
interesse4 = ctk.CTkCheckBox(root, text="Música")

def iniciar():
    titulo.configure(text="Crie o seu perfil próprio")
    subtitulo.configure(text="Preencha seus dados para começar")

    botao.pack_forget()

    nome.pack(pady=10)
    curso.pack(pady=10)
    botao_continuar.pack(pady=20)

def continuar():
    nome_usuario = nome.get()
    curso_usuario = curso.get()

    titulo.configure(text=f"Olá, {nome_usuario}!")
    subtitulo.configure(text="Agora escolha seus interesses:")

    nome.pack_forget()
    curso.pack_forget()
    botao_continuar.pack_forget()

    interesse1.pack(pady=5)
    interesse2.pack(pady=5)
    interesse3.pack(pady=5)
    interesse4.pack(pady=5)

botao = ctk.CTkButton(root, text="Começar", command=iniciar)
botao.pack(pady=30)

botao_continuar = ctk.CTkButton(root, text="Continuar", command=continuar)

root.mainloop()