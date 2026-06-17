
# =========================
# IMPORTAÇÃO DAS BIBLIOTECAS
# =========================

import time

import random

import csv

import os


from os import system, name


# =========================
# LISTA DOS USUÁRIOS
# =========================

usuarios = []


# =========================
# FUNÇÃO LIMPAR TELA
# =========================

def Limpa_tela():

    
    if name == "nt":

        system("cls")

    else:

        
        system("clear")

# =========================
# FUNÇÃO EFEITO DE DIGITAÇÃO
# =========================

def digitar(texto):

    
    for letra in texto:

        
        print(letra, end="", flush=True)

        
        time.sleep(0.03)

   
    print()


# =========================
# FUNÇÃO SALVAR USUÁRIOS
# =========================


def salvar_usuarios():

    
    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:

        
        escritor = csv.writer(arquivo)

        
        escritor.writerow(["login", "senha", "pontos"])

        
        for usuario in usuarios:

            
            escritor.writerow([
                usuario["login"],
                usuario["senha"],
                usuario["pontos"]
            ])

# =========================
# FUNÇÃO CARREGAR USUÁRIOS
# =========================

def carregar_usuarios():

    
    if not os.path.exists("usuarios.csv"):
        return

    
    with open("usuarios.csv", "r", encoding="utf-8") as arquivo:

        
        leitor = csv.DictReader(arquivo)

        
        for linha in leitor:

            
            usuario = {

                
                "login": linha["login"],
                "senha": linha["senha"],

                
                "pontos": int(linha["pontos"])
            }

            usuarios.append(usuario)

# =========================
# FUNÇÃO CADASTRAR USUÁRIO
# =========================


def cadastrar_usuario():

   
    Limpa_tela()

    
    while True:

        print("=== CADASTRO DE USUÁRIO ===")

        
        login = input("Login: ")
        senha = input("Senha: ")

        
        usuario = {

           
            "login": login,

            
            "senha": senha,

            
            "pontos": 0
        }

       
        usuarios.append(usuario)

        
        salvar_usuarios()

        print("\nUsuário cadastrado com sucesso!")

        
        continuar = input(
            "\nDeseja cadastrar outro usuário? [s/n]: "
        )

       
        if continuar.lower() != "s":
            break

       
        Limpa_tela()


# =========================
# FUNÇÃO LISTAR USUÁRIOS
# =========================


def listar_usuarios():

    
    Limpa_tela()

    print("=== USUÁRIOS CADASTRADOS ===\n")

    
    if len(usuarios) == 0:

        print("Nenhum usuário cadastrado.")

    else:

        
        for i, usuario in enumerate(usuarios, start=1):

            
            print(f"{i}. {usuario['login']}")

    
    input("\nPressione ENTER para continuar...")


# =========================
# FUNÇÃO QUIZ
# =========================


def jogar():

    
    Limpa_tela()

    print("=== INICIANDO QUIZ ===\n")

    
    perguntas = [

        {
            "pergunta": "Qual a capital do Brasil? ",
            "resposta": ["brasilia", "brasília"]
        },

        {
            "pergunta": "Qual a capital da Argentina? ",
            "resposta": ["buenos aires"]
        },

        {
            "pergunta": "Qual é o maior oceano? ",
            "resposta": [
                "oceano pacífico",
                "oceano pacifico",
                "pacífico",
                "pacifico"
            ]
        },

        {
            "pergunta": "Quanto é 20% de 400? ",
            "resposta": ["80"]
        },

        {
            "pergunta": "Quanto é 7 x 8 - 12? ",
            "resposta": ["44"]
        },

        {
            "pergunta": "Em que ano o Brasil foi descoberto? ",
            "resposta": ["1500"]
        }
    ]

    
    random.shuffle(perguntas)

    
    pontos = 0

    # =========================
    # LOOP DAS PERGUNTAS
    # =========================

    
    for item in perguntas:

       
        resposta_usuario = input(
            item["pergunta"]
        ).lower().strip()

        
        if resposta_usuario in item["resposta"]:

            print("✅ Resposta correta!")

           
            pontos += 10

        else:

            print("❌ Resposta errada!")

        time.sleep(1)

    # =========================
    # VERIFICA USUÁRIOS
    # =========================

    
    if len(usuarios) == 0:

        print("\nNenhum jogador cadastrado.")

        input("\nPressione ENTER...")

        return

    # =========================
    # ESCOLHER JOGADOR
    # =========================

    print("\n=== JOGADORES ===")

    
    for i, usuario in enumerate(usuarios):

        print(f"{i} - {usuario['login']}")

    
    try:

        
        escolha = int(input("\nEscolha o jogador: "))

        
        if escolha < 0 or escolha >= len(usuarios):

            print("Jogador inválido.")

            return

    
    except:

        print("Digite apenas números.")

        return

    # =========================
    # ADICIONAR PONTOS
    # =========================

    
    jogador = usuarios[escolha]

    
    jogador["pontos"] += pontos

   
    salvar_usuarios()

   
    print(f"\nJogador: {jogador['login']}")
    print(f"Pontos ganhos: {pontos}")

    input("\nPressione ENTER para continuar...")


# =========================
# FUNÇÃO RANKING
# =========================


def ranking():

    
    Limpa_tela()

    print("=== RANKING ===\n")

    
    if len(usuarios) == 0:

        print("Nenhum jogador cadastrado.")

        input("\nPressione ENTER...")

        return

    
    ranking_ordenado = sorted(
        usuarios,
        key=lambda usuario: usuario["pontos"],
        reverse=True
    )

   
    for posicao, usuario in enumerate(
        ranking_ordenado,
        start=1
    ):

        print(
            f"{posicao}º lugar - "
            f"{usuario['login']} "
            f"({usuario['pontos']} pontos)"
        )

    input("\nPressione ENTER para continuar...")


# =========================
# CARREGAR DADOS DO CSV
# =========================


carregar_usuarios()


# =========================
# TÍTULO DO PROGRAMA 
# =========================


Limpa_tela()


digitar("==============================")
digitar("====== NOVO QUIZ NA ÁREA =====")
digitar("==============================")

digitar("\nOlá jogador, seja bem-vindo!\n")


# =========================
# MENU PRINCIPAL
# =========================


while True:

    
    Limpa_tela()

    
    print("1 - Jogar")
    print("2 - Cadastrar Jogador")
    print("3 - Listar Jogadores")
    print("4 - Ranking")
    print("5 - Sair")

    
    opcao = input("\nEscolha: ")

    # =========================
    # OPÇÃO 1 -> JOGAR
    # =========================
    if opcao == "1":

        jogar()

    # =========================
    # OPÇÃO 2 -> CADASTRAR
    # =========================
    elif opcao == "2":

        cadastrar_usuario()

    # =========================
    # OPÇÃO 3 -> LISTAR
    # =========================
    elif opcao == "3":

        listar_usuarios()

    # =========================
    # OPÇÃO 4 -> RANKING
    # =========================
    elif opcao == "4":

        ranking()

    # =========================
    # OPÇÃO 5 -> SAIR
    # =========================
    elif opcao == "5":

        Limpa_tela()

        print("Saindo...")

        
        break

    # =========================
    # OPÇÃO INVÁLIDA
    # =========================
    else:

        print("Opção inválida.")

        
        time.sleep(1)