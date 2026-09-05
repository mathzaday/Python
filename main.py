import customtkinter as ctk

root = ctk.CTk()
root.title("UNIMAR Match")
root.geometry("1280x720")
root.resizable(False, False)
root.configure(fg_color="#1E1E2E")

titulo = ctk.CTkLabel(root, text="UNIMAR MATCH", font=ctk.CTkFont(size=30, weight="bold"))
titulo.pack(pady=60)

subtitulo = ctk.CTkLabel(root, text="Encontre pessoas com interesses parecidos com os seus.", font=ctk.CTkFont(size=16))
subtitulo.pack(pady=10)

nome = ctk.CTkEntry(root, placeholder_text="Digite seu nome", width=300)
curso = ctk.CTkEntry(root, placeholder_text="Digite seu curso", width=300)
semestre = ctk.CTkEntry(root, placeholder_text="Digite seu semestre", width=300)

interesse1 = ctk.CTkCheckBox(root, text="Programação")
interesse2 = ctk.CTkCheckBox(root, text="Jogos")
interesse3 = ctk.CTkCheckBox(root, text="Esportes")
interesse4 = ctk.CTkCheckBox(root, text="Música")
interesse5 = ctk.CTkCheckBox(root, text="Filmes")
interesse6 = ctk.CTkCheckBox(root, text="Estudos")

objetivo1 = ctk.CTkCheckBox(root, text="Grupo de estudos")
objetivo2 = ctk.CTkCheckBox(root, text="Parceiro para projetos")
objetivo3 = ctk.CTkCheckBox(root, text="Novas amizades")
objetivo4 = ctk.CTkCheckBox(root, text="Hobbies em comum")

resultado = ctk.CTkLabel(root, text="", font=ctk.CTkFont(size=18, weight="bold"))

favorito = ""


def esconder_tudo():
    nome.pack_forget()
    curso.pack_forget()
    semestre.pack_forget()

    interesse1.pack_forget()
    interesse2.pack_forget()
    interesse3.pack_forget()
    interesse4.pack_forget()
    interesse5.pack_forget()
    interesse6.pack_forget()

    objetivo1.pack_forget()
    objetivo2.pack_forget()
    objetivo3.pack_forget()
    objetivo4.pack_forget()

    resultado.pack_forget()

    botao.pack_forget()
    botao_favoritos.pack_forget()
    botao_continuar.pack_forget()
    botao_interesses.pack_forget()
    botao_match.pack_forget()
    botao_favoritar.pack_forget()
    botao_remover.pack_forget()
    botao_voltar.pack_forget()
    botao_menu.pack_forget()


def iniciar():
    esconder_tudo()

    titulo.configure(text="Crie o seu perfil")
    subtitulo.configure(text="Preencha seus dados para começar")

    nome.pack(pady=10)
    curso.pack(pady=10)
    semestre.pack(pady=10)
    botao_continuar.pack(pady=20)

    botao_voltar.configure(command=voltar_inicio)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


def continuar():
    if nome.get() == "" or curso.get() == "" or semestre.get() == "":
        subtitulo.configure(text="Preencha todos os dados para continuar")
        return

    esconder_tudo()

    titulo.configure(text=f"Olá, {nome.get()}!")
    subtitulo.configure(text="Agora escolha seus interesses:")

    interesse1.pack(pady=5)
    interesse2.pack(pady=5)
    interesse3.pack(pady=5)
    interesse4.pack(pady=5)
    interesse5.pack(pady=5)
    interesse6.pack(pady=5)

    botao_interesses.pack(pady=20)

    botao_voltar.configure(command=voltar_dados)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


def interesses():
    if interesse1.get() == 0 and interesse2.get() == 0 and interesse3.get() == 0 and interesse4.get() == 0 and interesse5.get() == 0 and interesse6.get() == 0:
        subtitulo.configure(text="Escolha pelo menos um interesse")
        return

    esconder_tudo()

    titulo.configure(text="O que você procura?")
    subtitulo.configure(text="Escolha o que você gostaria de encontrar:")

    objetivo1.pack(pady=5)
    objetivo2.pack(pady=5)
    objetivo3.pack(pady=5)
    objetivo4.pack(pady=5)

    botao_match.pack(pady=20)

    botao_voltar.configure(command=voltar_interesses)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


def encontrar_match():
    if objetivo1.get() == 0 and objetivo2.get() == 0 and objetivo3.get() == 0 and objetivo4.get() == 0:
        subtitulo.configure(text="Escolha pelo menos um objetivo")
        return

    interesses = ""
    objetivos = ""

    if interesse1.get() == 1:
        interesses = "Programação"

    if interesse2.get() == 1:
        if interesses != "":
            interesses += ", "
        interesses += "Jogos"

    if interesse3.get() == 1:
        if interesses != "":
            interesses += ", "
        interesses += "Esportes"

    if interesse4.get() == 1:
        if interesses != "":
            interesses += ", "
        interesses += "Música"

    if interesse5.get() == 1:
        if interesses != "":
            interesses += ", "
        interesses += "Filmes"

    if interesse6.get() == 1:
        if interesses != "":
            interesses += ", "
        interesses += "Estudos"

    if objetivo1.get() == 1:
        objetivos = "Grupo de estudos"

    if objetivo2.get() == 1:
        if objetivos != "":
            objetivos += ", "
        objetivos += "Projetos"

    if objetivo3.get() == 1:
        if objetivos != "":
            objetivos += ", "
        objetivos += "Amizades"

    if objetivo4.get() == 1:
        if objetivos != "":
            objetivos += ", "
        objetivos += "Hobbies"

    esconder_tudo()

    titulo.configure(text="Seu Match")
    subtitulo.configure(text="Encontramos uma pessoa que pode combinar com você:")

    resultado.configure(text=f"João - Engenharia de Software\n\n"
                             f"Interesses em comum: {interesses}\n"
                             f"Objetivos em comum: {objetivos}")

    resultado.pack(pady=30)
    botao_favoritar.pack(pady=10)
    botao_voltar.configure(command=voltar_objetivos)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


def favoritar():
    global favorito

    favorito = "João - Engenharia de Software"
    subtitulo.configure(text=f"{favorito} foi adicionado aos favoritos!")


def remover_favorito():
    global favorito

    favorito = ""
    subtitulo.configure(text="Favorito removido!")


def mostrar_favoritos():
    esconder_tudo()

    titulo.configure(text="Meus Favoritos")

    if favorito == "":
        subtitulo.configure(text="Você ainda não possui favoritos.")
    else:
        subtitulo.configure(text=f"{favorito}")
        botao_remover.pack(pady=20)

    botao_voltar.configure(command=voltar_inicio)
    botao_voltar.pack(pady=30)


def voltar_inicio():
    esconder_tudo()

    titulo.configure(text="UNIMAR MATCH")
    subtitulo.configure(text="Encontre pessoas com interesses parecidos com os seus.")

    botao.pack(pady=20)
    botao_favoritos.pack(pady=10)


def voltar_dados():
    esconder_tudo()

    titulo.configure(text="Crie o seu perfil")
    subtitulo.configure(text="Preencha seus dados para começar")

    nome.pack(pady=10)
    curso.pack(pady=10)
    semestre.pack(pady=10)
    botao_continuar.pack(pady=20)

    botao_voltar.configure(command=voltar_inicio)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


def voltar_interesses():
    esconder_tudo()

    titulo.configure(text=f"Olá, {nome.get()}!")
    subtitulo.configure(text="Agora escolha seus interesses:")

    interesse1.pack(pady=5)
    interesse2.pack(pady=5)
    interesse3.pack(pady=5)
    interesse4.pack(pady=5)
    interesse5.pack(pady=5)
    interesse6.pack(pady=5)

    botao_interesses.pack(pady=20)

    botao_voltar.configure(command=voltar_dados)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


def voltar_objetivos():
    esconder_tudo()

    titulo.configure(text="O que você procura?")
    subtitulo.configure(text="Escolha o que você gostaria de encontrar:")

    objetivo1.pack(pady=5)
    objetivo2.pack(pady=5)
    objetivo3.pack(pady=5)
    objetivo4.pack(pady=5)

    botao_match.pack(pady=20)

    botao_voltar.configure(command=voltar_interesses)
    botao_voltar.pack(pady=10)
    botao_menu.pack(pady=10)


botao = ctk.CTkButton(root, text="Começar", command=iniciar)
botao.pack(pady=20)

botao_favoritos = ctk.CTkButton(root, text="Meus Favoritos", command=mostrar_favoritos)
botao_favoritos.pack(pady=10)

botao_continuar = ctk.CTkButton(root, text="Continuar", command=continuar)
botao_interesses = ctk.CTkButton(root, text="Continuar", command=interesses)
botao_match = ctk.CTkButton(root, text="Encontrar meu Match", command=encontrar_match)
botao_favoritar = ctk.CTkButton(root, text="Favoritar", command=favoritar)
botao_remover = ctk.CTkButton(root, text="Remover favorito", command=remover_favorito)
botao_voltar = ctk.CTkButton(root, text="Voltar")
botao_menu = ctk.CTkButton(root, text="Menu Principal", command=voltar_inicio)

root.mainloop()