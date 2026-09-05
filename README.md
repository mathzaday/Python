# UNIMAR Match

## Sobre o projeto

O **UNIMAR Match** é uma aplicação desktop desenvolvida em Python com a biblioteca **CustomTkinter**.

O objetivo do projeto é ajudar estudantes da UNIMAR a encontrar pessoas com interesses e objetivos semelhantes, facilitando a criação de grupos de estudos, parcerias para projetos, novas amizades e a busca por hobbies em comum.

## Funcionalidades

- Criação de perfil com:
  - Nome
  - Curso
  - Semestre
- Seleção de interesses:
  - Programação
  - Jogos
  - Esportes
  - Música
  - Filmes
  - Estudos
- Seleção de objetivos:
  - Grupo de estudos
  - Parceiro para projetos
  - Novas amizades
  - Hobbies em comum
- Exibição de um possível Match
- Sistema de favoritos
- Visualização e remoção de favoritos
- Navegação entre as diferentes telas do aplicativo

## Tecnologias utilizadas

- **Python**
- **CustomTkinter**

O CustomTkinter foi utilizado para criar a interface gráfica do aplicativo, utilizando elementos como botões, campos de texto, caixas de seleção e textos.

## Como instalar

### 1. Instalar o Python

Primeiramente, é necessário ter o Python instalado no computador.

Durante a instalação do Python no Windows, é recomendado marcar a opção:

```text
Add Python to PATH
```

### 2. Instalar o CustomTkinter

Abra o **Prompt de Comando (CMD)** ou o terminal do VS Code e execute:

```bash
pip install customtkinter
```

Após a instalação, o projeto já poderá utilizar:

```python
import customtkinter as ctk
```

### 3. Executar o projeto

Depois de instalar o CustomTkinter, abra a pasta do projeto no VS Code e execute o arquivo principal:

```bash
python main.py
```

Caso o arquivo tenha outro nome, substitua `main.py` pelo nome correto.

## Estrutura básica

Uma possível organização do projeto é:

```text
UNIMAR-Match/
│
├── main.py
└── README.md
```

- `main.py` — contém o código principal da aplicação.
- `README.md` — contém as informações e instruções do projeto.

## Como utilizar

1. Abra o aplicativo.
2. Clique em **Começar**.
3. Preencha seu nome, curso e semestre.
4. Escolha seus interesses.
5. Escolha o objetivo desejado.
6. Clique em **Encontrar meu Match**.
7. Visualize o perfil encontrado.
8. Caso queira, adicione o perfil aos favoritos.
9. Na tela inicial, acesse **Meus Favoritos** para visualizar o perfil salvo.

## Objetivo do projeto

O projeto busca demonstrar como a programação pode ser utilizada para desenvolver uma solução simples para facilitar a interação entre estudantes.

Além disso, o desenvolvimento permitiu aplicar conceitos básicos de Python e criação de interfaces gráficas utilizando o CustomTkinter.
