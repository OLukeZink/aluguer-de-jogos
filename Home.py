import streamlit as st
import pandas as pd
import os
import json

# Caminho do arquivo de usuários
USERS_FILE = "data/usuarios.json"

# Função para carregar usuários do arquivo
def carregar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"admin": "1234"}

# Função para salvar usuários no arquivo
def salvar_usuarios(usuarios):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)

# Carrega os usuários do arquivo
usuarios = carregar_usuarios()

# Simulação de histórico de aluguéis
if "historico" not in st.session_state:
    st.session_state.historico = []
# Limpa registros antigos com menos de 4 colunas
st.session_state.historico = [h for h in st.session_state.historico if len(h) == 4]

# Configuração inicial do estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "Login"

# Inicialização do jogo selecionado
if "jogo_selecionado" not in st.session_state:
    st.session_state.jogo_selecionado = None

# Função para mudar de página
def mudar_para_aluguer():
    st.session_state.pagina = "Aluguer"

def mudar_para_home():
    st.session_state.pagina = "Home"

def logout():
    st.session_state.pagina = "Login"

# Página de login
if st.session_state.pagina == "Login":
    st.title("🎮 Login - Loja de Aluguer de Jogos")
    username = st.text_input("👤 Usuário")
    password = st.text_input("🔒 Senha", type="password")
    if st.button("Entrar"):
        if username in usuarios and usuarios[username] == password:
            st.session_state.username = username
            mudar_para_home()
            st.rerun()  # Use este se estiver com Streamlit atualizado
        else:
            st.error("❌ Usuário ou senha incorretos.")
    if st.button("Registrar"):
        st.session_state.pagina = "Registro"

# Página de registro
elif st.session_state.pagina == "Registro":
    st.title("📝 Registrar - Loja de Aluguer de Jogos")
    new_username = st.text_input("👤 Novo Usuário")
    new_password = st.text_input("🔒 Nova Senha", type="password")
    if st.button("Registrar"):
        if new_username in usuarios:
            st.error("❌ Usuário já existe!")
        else:
            usuarios[new_username] = new_password
            salvar_usuarios(usuarios)  # Salva no arquivo
            st.success("✅ Usuário registrado com sucesso!")
            st.session_state.pagina = "Login"

# Página de detalhes do jogo selecionado (igual para todos os jogos)
elif st.session_state.jogo_selecionado:
    # Junta todos os jogos num só dicionário
    todos_os_jogos = {}

    # Biblioteca principal
    todos_os_jogos.update({
        "FIFA 23": {
            "preco": 0.25,
            "imagem": "c:/Users/a25679/Downloads/fifa.png",
            "descricao": "O melhor do futebol virtual, com gráficos incríveis e jogabilidade realista.",
            "genero": "Esporte",
            "ano": "2023",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=o3V-GvvzjE4"
        },
        "Call of Duty": {
            "preco": 0.29,
            "imagem": "c:/Users/a25679/Downloads/call_of_duty-logo-brandlogos.net_.png",
            "descricao": "Ação intensa em primeira pessoa em batalhas épicas.",
            "genero": "Tiro em primeira pessoa",
            "ano": "2022",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=EE-4GvjKcfs"
        },
        "GTA V": {
            "preco": 0.27,
            "imagem": "c:/Users/a25679/Downloads/gta.png",
            "descricao": "Explore Los Santos em um dos maiores sucessos de mundo aberto.",
            "genero": "Ação/Aventura",
            "ano": "2013",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=QkkoHAzjnUs"
        },
        "Minecraft": {
            "preco": 0.19,
            "imagem": "c:/Users/a25679/Downloads/minecraft-logo-with-basic-block-structure-03dch9gg2iy4hthk.jpg",  # nova imagem local
            "descricao": "Construa e explore mundos infinitos em Minecraft.",
            "genero": "Sandbox",
            "ano": "2011",
            "plataformas": "PC, PlayStation, Xbox, Switch, Mobile",
            "trailer": "https://www.youtube.com/watch?v=MmB9b5njVbA"
        },
        "The Witcher 3": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/0c/Witcher_3_capa.png",
            "descricao": "Uma aventura épica em um mundo aberto de fantasia.",
            "genero": "RPG",
            "ano": "2015",
            "plataformas": "PC, PlayStation, Xbox, Switch",
            "trailer": "https://www.youtube.com/watch?v=c0i88t0Kacs"
        }
    })

    # Outros jogos
    todos_os_jogos.update({
        "Red Dead Redemption 2": {
            "preco": 0.30,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/4/44/Red_Dead_Redemption_2_capa.png",
            "descricao": "Viva o Velho Oeste em um dos jogos mais imersivos já feitos.",
            "genero": "Ação/Aventura",
            "ano": "2018",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=eaW0tYpxyp0"
        },
        "Cyberpunk 2077": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/9/9f/Cyberpunk_2077_capa.png",
            "descricao": "Explore Night City em um RPG futurista de mundo aberto.",
            "genero": "RPG/Ação",
            "ano": "2020",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=FknHjl7eQ6o"
        },
        "Fortnite": {
            "preco": 0.15,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/09/Fortnite_capa.png",
            "descricao": "O battle royale mais jogado do mundo.",
            "genero": "Battle Royale",
            "ano": "2017",
            "plataformas": "PC, PlayStation, Xbox, Switch, Mobile",
            "trailer": "https://www.youtube.com/watch?v=2gUtfBmw86Y"
        },
        "God of War": {
            "preco": 0.32,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/a/a7/God_of_War_4_capa.png",
            "descricao": "A jornada épica de Kratos e Atreus pela mitologia nórdica.",
            "genero": "Ação/Aventura",
            "ano": "2018",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=K0u_kAWLJOA"
        },
        "Horizon Zero Dawn": {
            "preco": 0.27,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/3/3a/Horizon_Zero_Dawn_capa.png",
            "descricao": "Explore um mundo pós-apocalíptico dominado por máquinas.",
            "genero": "Ação/RPG",
            "ano": "2017",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=wzx96gYA8ek"
        },
        "Assassin's Creed Valhalla": {
            "preco": 0.29,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/9/9b/Assassin%27s_Creed_Valhalla_capa.png",
            "descricao": "Viva como um viking em uma aventura épica.",
            "genero": "Ação/RPG",
            "ano": "2020",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=ssrNcwxALS4"
        },
        "F1 2023": {
            "preco": 0.25,
            "imagem": "https://cdn.cloudflare.steamstatic.com/steam/apps/2108330/header.jpg",
            "descricao": "A experiência definitiva de Fórmula 1.",
            "genero": "Corrida",
            "ano": "2023",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=QFvNhsWMU0c"
        },
        "Elden Ring": {
            "preco": 0.33,
            "imagem": "c:/Users/a25679/Downloads/elden-ring2086.jpg",  # nova imagem local
            "descricao": "Explore as Terras Intermédias neste RPG de ação desafiador.",
            "genero": "RPG/Ação",
            "ano": "2022",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=E3Huy2cdih0"
        },
        "Spider-Man Remastered": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/0c/Spider-Man_PS4_capa.png",
            "descricao": "Viva as aventuras do Homem-Aranha em Nova York.",
            "genero": "Ação/Aventura",
            "ano": "2022",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=Nt9L1jCKGnE"
        },
        "Super Mario Odyssey": {
            "preco": 0.22,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/8/8d/Super_Mario_Odyssey_capa.png",
            "descricao": "A aventura 3D definitiva do Mario pelo mundo.",
            "genero": "Plataforma",
            "ano": "2017",
            "plataformas": "Switch",
            "trailer": "https://www.youtube.com/watch?v=5kcdRBHM7kM"
        }
    })

    jogo = st.session_state.jogo_selecionado
    info = todos_os_jogos[jogo]
    st.title(jogo)
    st.image(info["imagem"], use_container_width=True)
    st.write(info["descricao"])
    st.markdown(f"**Género:** {info['genero']}")
    st.markdown(f"**Ano:** {info['ano']}")
    st.markdown(f"**Plataformas:** {info['plataformas']}")
    st.markdown(f"**Preço de aluguer:** €{info['preco']}/dia")
    st.video(info["trailer"])
    st.markdown("---")
    st.markdown("**Avaliações dos jogadores:**")
    st.info("⭐⭐⭐⭐⭐ 'Muito divertido e viciante!'")
    st.info("⭐⭐⭐⭐ 'Ótimos gráficos e jogabilidade.'")

    # Aluguer direto nesta página
    st.header("📋 Alugar este jogo")
    dias_aluguer = st.number_input("📅 Dias de Aluguer", min_value=1, max_value=30, step=1, key=f"dias_{jogo}")
    preco_total = info["preco"] * dias_aluguer
    st.markdown(f"**💵 Preço Total:** €{preco_total:.2f}")

    if st.button("✅ Confirmar Aluguer", key=f"alugar_{jogo}"):
        if dias_aluguer:
            st.success(f"✅ Aluguer confirmado para {st.session_state.username}!")
            st.write(f"🎮 Jogo: {jogo}")
            st.write(f"📅 Dias de Aluguer: {dias_aluguer}")
            st.write(f"💵 Preço Total: €{preco_total:.2f}")
            st.session_state.historico.append([st.session_state.username, jogo, dias_aluguer, preco_total])
        else:
            st.error("❌ Por favor, preencha todas as informações.")

    if st.button("Voltar"):
        st.session_state.jogo_selecionado = None
        st.session_state.pagina = "Home"
        st.rerun()

# Página inicial
elif st.session_state.pagina == "Home":
    st.markdown("<h1 style='text-align: center;'>🎮 Bem-vindo à Loja de Aluguer de Jogos!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Alugue os melhores jogos e divirta-se com seus amigos!</p>", unsafe_allow_html=True)

    # Adicionando uma imagem para tornar a página mais visual
    st.image("https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80", use_container_width=True)

    # Jogos populares
    st.subheader("🎲 Jogos Populares")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("c:/Users/a25679/Downloads/fifa.png", caption="FIFA 23", use_container_width=True)
        if st.button("Ver FIFA 23"):
            st.session_state.jogo_selecionado = "FIFA 23"
            st.rerun()
    with col2:
        st.image("c:/Users/a25679/Downloads/call_of_duty-logo-brandlogos.net_.png", caption="Call of Duty", use_container_width=True)
        if st.button("Ver Call of Duty"):
            st.session_state.jogo_selecionado = "Call of Duty"
            st.rerun()
    with col3:
        st.image("c:/Users/a25679/Downloads/gta.png", caption="GTA V", use_container_width=True)
        if st.button("Ver GTA V"):
            st.session_state.jogo_selecionado = "GTA V"
            st.rerun()

    # Botões estilizados
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎮 Ir para Aluguer"):
            mudar_para_aluguer()
    with col2:
        if st.button("🚪 Logout"):
            logout()
    with col3:
        if st.button("📚 Ver Biblioteca"):
            st.session_state.pagina = "Biblioteca"
            st.rerun()

    # Histórico de aluguéis
    if st.session_state.historico:
        st.subheader("📜 Histórico de Aluguéis")
        historico_df = pd.DataFrame(
            st.session_state.historico,
            columns=["Usuário", "Jogo", "Dias", "Preço (€)"]
        )
        st.table(historico_df)
        if "username" in st.session_state and st.session_state.username == "admin":
            total_ganho = historico_df["Preço (€)"].sum()
            st.success(f"💰 Total ganho em aluguéis: €{total_ganho:.2f}")
    else:
        st.info("Nenhum histórico de aluguéis disponível.")

# Página de aluguel
elif st.session_state.pagina == "Aluguer":
    st.title("🛒 Aluguer de Jogos")

    # Lista de jogos disponíveis com preços e imagens
    jogos_info = {
        "FIFA 23": {
            "preco": 0.25,
            "imagem": "c:/Users/a25679/Downloads/fifa.png",
            "descricao": "O melhor do futebol virtual, com gráficos incríveis e jogabilidade realista.",
            "genero": "Esporte",
            "ano": "2023",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=o3V-GvvzjE4"
        },
        "Call of Duty": {
            "preco": 0.29,
            "imagem": "c:/Users/a25679/Downloads/call_of_duty-logo-brandlogos.net_.png",
            "descricao": "Ação intensa em primeira pessoa em batalhas épicas.",
            "genero": "Tiro em primeira pessoa",
            "ano": "2022",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=EE-4GvjKcfs"
        },
        "GTA V": {
            "preco": 0.27,
            "imagem": "c:/Users/a25679/Downloads/gta.png",
            "descricao": "Explore Los Santos em um dos maiores sucessos de mundo aberto.",
            "genero": "Ação/Aventura",
            "ano": "2013",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=QkkoHAzjnUs"
        },
        "Minecraft": {
            "preco": 0.19,
            "imagem": "c:/Users/a25679/Downloads/minecraft-logo-with-basic-block-structure-03dch9gg2iy4hthk.jpg",  # nova imagem local
            "descricao": "Construa e explore mundos infinitos em Minecraft.",
            "genero": "Sandbox",
            "ano": "2011",
            "plataformas": "PC, PlayStation, Xbox, Switch, Mobile",
            "trailer": "https://www.youtube.com/watch?v=MmB9b5njVbA"
        },
        "The Witcher 3": {
            "preco": 0.28,
            "imagem": "c:/Users/a25679/Downloads/2529001-witcherlogo.jpg",  # nova imagem local
            "descricao": "Uma aventura épica em um mundo aberto de fantasia.",
            "genero": "RPG",
            "ano": "2015",
            "plataformas": "PC, PlayStation, Xbox, Switch",
            "trailer": "https://www.youtube.com/watch?v=c0i88t0Kacs"
        }
    }

    st.header("🎲 Escolha o jogo que deseja alugar")
    jogos = list(jogos_info.keys())
    jogo_selecionado = st.selectbox("Jogos disponíveis:", jogos)
    st.image(jogos_info[jogo_selecionado]["imagem"], width=250)
    st.markdown(f"**Preço por dia:** €{jogos_info[jogo_selecionado]['preco']:.2f}")

    # Aluguer direto na página do jogo
    st.header("📋 Alugar este jogo")
    dias_aluguer = st.number_input("📅 Dias de Aluguer", min_value=1, max_value=600, step=1, key=f"dias_{jogo_selecionado}")
    preco_total = jogos_info[jogo_selecionado]['preco'] * dias_aluguer
    st.markdown(f"**💵 Preço Total:** €{preco_total:.2f}")

    if st.button("✅ Confirmar Aluguer"):
        if dias_aluguer and jogo_selecionado:
            st.success(f"✅ Aluguer confirmado para {st.session_state.username}!")
            st.write(f"🎮 Jogo: {jogo_selecionado}")
            st.write(f"📅 Dias de Aluguer: {dias_aluguer}")
            st.write(f"💵 Preço Total: €{preco_total:.2f}")
            st.session_state.historico.append([st.session_state.username, jogo_selecionado, dias_aluguer, preco_total])
        else:
            st.error("❌ Por favor, preencha todas as informações.")

    if st.button("🔙 Voltar para Home"):
        mudar_para_home()

# Página Biblioteca de Jogos
elif st.session_state.pagina == "Biblioteca":
    st.title("📚 Biblioteca de Jogos Disponíveis")

    # Junta todos os jogos em um único dicionário
    biblioteca_jogos = {
        "FIFA 23": {
            "preco": 0.25,
            "imagem": "c:/Users/a25679/Downloads/fifa.png",
            "descricao": "O melhor do futebol virtual, com gráficos incríveis e jogabilidade realista.",
            "genero": "Esporte",
            "ano": "2023",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=o3V-GvvzjE4"
        },
        "Call of Duty": {
            "preco": 0.29,
            "imagem": "c:/Users/a25679/Downloads/call_of_duty-logo-brandlogos.net_.png",
            "descricao": "Ação intensa em primeira pessoa em batalhas épicas.",
            "genero": "Tiro em primeira pessoa",
            "ano": "2022",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=EE-4GvjKcfs"
        },
        "GTA V": {
            "preco": 0.27,
            "imagem": "c:/Users/a25679/Downloads/gta.png",
            "descricao": "Explore Los Santos em um dos maiores sucessos de mundo aberto.",
            "genero": "Ação/Aventura",
            "ano": "2013",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=QkkoHAzjnUs"
        },
        "Minecraft": {
            "preco": 0.19,
            "imagem": "c:/Users/a25679/Downloads/minecraft-logo-with-basic-block-structure-03dch9gg2iy4hthk.jpg",
            "descricao": "Construa e explore mundos infinitos em Minecraft.",
            "genero": "Sandbox",
            "ano": "2011",
            "plataformas": "PC, PlayStation, Xbox, Switch, Mobile",
            "trailer": "https://www.youtube.com/watch?v=MmB9b5njVbA"
        },
        "The Witcher 3": {
            "preco": 0.28,
            "imagem": "c:/Users/a25679/Downloads/2529001-witcherlogo.jpg",
            "descricao": "Uma aventura épica em um mundo aberto de fantasia.",
            "genero": "RPG",
            "ano": "2015",
            "plataformas": "PC, PlayStation, Xbox, Switch",
            "trailer": "https://www.youtube.com/watch?v=c0i88t0Kacs"
        },
        "Red Dead Redemption 2": {
            "preco": 0.30,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/4/44/Red_Dead_Redemption_2_capa.png",
            "descricao": "Viva o Velho Oeste em um dos jogos mais imersivos já feitos.",
            "genero": "Ação/Aventura",
            "ano": "2018",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=eaW0tYpxyp0"
        },
        "Cyberpunk 2077": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/9/9f/Cyberpunk_2077_capa.png",
            "descricao": "Explore Night City em um RPG futurista de mundo aberto.",
            "genero": "RPG/Ação",
            "ano": "2020",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=FknHjl7eQ6o"
        },
        "Fortnite": {
            "preco": 0.15,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/09/Fortnite_capa.png",
            "descricao": "O battle royale mais jogado do mundo.",
            "genero": "Battle Royale",
            "ano": "2017",
            "plataformas": "PC, PlayStation, Xbox, Switch, Mobile",
            "trailer": "https://www.youtube.com/watch?v=2gUtfBmw86Y"
        },
        "God of War": {
            "preco": 0.32,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/a/a7/God_of_War_4_capa.png",
            "descricao": "A jornada épica de Kratos e Atreus pela mitologia nórdica.",
            "genero": "Ação/Aventura",
            "ano": "2018",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=K0u_kAWLJOA"
        },
        "Horizon Zero Dawn": {
            "preco": 0.27,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/3/3a/Horizon_Zero_Dawn_capa.png",
            "descricao": "Explore um mundo pós-apocalíptico dominado por máquinas.",
            "genero": "Ação/RPG",
            "ano": "2017",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=wzx96gYA8ek"
        },
        "Assassin's Creed Valhalla": {
            "preco": 0.29,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/9/9b/Assassin%27s_Creed_Valhalla_capa.png",
            "descricao": "Viva como um viking em uma aventura épica.",
            "genero": "Ação/RPG",
            "ano": "2020",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=ssrNcwxALS4"
        },
        "F1 2023": {
            "preco": 0.25,
            "imagem": "https://cdn.cloudflare.steamstatic.com/steam/apps/2108330/header.jpg",
            "descricao": "A experiência definitiva de Fórmula 1.",
            "genero": "Corrida",
            "ano": "2023",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=QFvNhsWMU0c"
        },
        "Elden Ring": {
            "preco": 0.33,
            "imagem": "c:/Users/a25679/Downloads/elden-ring2086.jpg",
            "descricao": "Explore as Terras Intermédias neste RPG de ação desafiador.",
            "genero": "RPG/Ação",
            "ano": "2022",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=E3Huy2cdih0"
        },
        "Spider-Man Remastered": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/0c/Spider-Man_PS4_capa.png",
            "descricao": "Viva as aventuras do Homem-Aranha em Nova York.",
            "genero": "Ação/Aventura",
            "ano": "2022",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=Nt9L1jCKGnE"
        },
        "Super Mario Odyssey": {
            "preco": 0.22,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/8/8d/Super_Mario_Odyssey_capa.png",
            "descricao": "A aventura 3D definitiva do Mario pelo mundo.",
            "genero": "Plataforma",
            "ano": "2017",
            "plataformas": "Switch",
            "trailer": "https://www.youtube.com/watch?v=5kcdRBHM7kM"
        }
    }

    # Layout com filtros à esquerda e jogos à direita
    filtro_col, jogos_col = st.columns([1, 5])  # aumenta a proporção da área dos jogos

    with filtro_col:
        st.subheader("Filtros")
        # Filtro de preço
        precos = [info["preco"] for info in biblioteca_jogos.values()]
        preco_min = min(precos)
        preco_max = max(precos)
        preco_filtro = st.slider("Preço (€ por dia)", float(preco_min), float(preco_max), (float(preco_min), float(preco_max)), step=0.01)

        # Filtro de género
        generos = sorted(set(info["genero"] for info in biblioteca_jogos.values()))
        genero_filtro = st.multiselect("Género", generos, default=generos)

        # Filtro de plataforma
        plataformas = sorted(set(sum([info["plataformas"].replace(" ", "").split(",") for info in biblioteca_jogos.values()], [])))
        plataforma_filtro = st.multiselect("Plataforma", plataformas, default=plataformas)

    with jogos_col:
        # Se nenhum género ou plataforma estiver selecionado, mostra todos os jogos
        if not genero_filtro:
            genero_filtro = generos
        if not plataforma_filtro:
            plataforma_filtro = plataformas

        # Filtra os jogos pelos filtros selecionados
        jogos_filtrados = {
            nome: info for nome, info in biblioteca_jogos.items()
            if preco_filtro[0] <= info["preco"] <= preco_filtro[1]
            and info["genero"] in genero_filtro
            and any(p.strip() in plataforma_filtro for p in info["plataformas"].split(","))
        }

        # Deixa as imagens, nome e preço maiores
        cols = st.columns(4)
        for idx, (nome, info) in enumerate(jogos_filtrados.items()):
            with cols[idx % 4]:
                st.image(info["imagem"], caption="", use_container_width=True, output_format="auto")
                st.markdown(f"<h2 style='text-align:center; font-size:2rem'>{nome}</h2>", unsafe_allow_html=True)
                st.markdown(f"<div style='text-align:center; font-size:1.5rem; color:#16a34a'><b>€{info['preco']:.2f}</b></div>", unsafe_allow_html=True)
                if st.button(f"Ver {nome}", key=f"ver_{nome}"):
                    st.session_state.jogo_selecionado = nome
                    st.session_state.pagina = None
                    st.rerun()

        if st.button("🔙 Voltar para Home"):
            mudar_para_home()

# Página de Outros Jogos
elif st.session_state.pagina == "OutrosJogos":
    st.title("🎮 Outros Jogos Disponíveis")

    outros_jogos = {
        "Red Dead Redemption 2": {
            "preco": 0.30,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/4/44/Red_Dead_Redemption_2_capa.png",
            "descricao": "Viva o Velho Oeste em um dos jogos mais imersivos já feitos.",
            "genero": "Ação/Aventura",
            "ano": "2018",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=eaW0tYpxyp0"
        },
        "Cyberpunk 2077": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/9/9f/Cyberpunk_2077_capa.png",
            "descricao": "Explore Night City em um RPG futurista de mundo aberto.",
            "genero": "RPG/Ação",
            "ano": "2020",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=FknHjl7eQ6o"
        },
        "Fortnite": {
            "preco": 0.15,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/09/Fortnite_capa.png",
            "descricao": "O battle royale mais jogado do mundo.",
            "genero": "Battle Royale",
            "ano": "2017",
            "plataformas": "PC, PlayStation, Xbox, Switch, Mobile",
            "trailer": "https://www.youtube.com/watch?v=2gUtfBmw86Y"
        },
        "God of War": {
            "preco": 0.32,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/a/a7/God_of_War_4_capa.png",
            "descricao": "A jornada épica de Kratos e Atreus pela mitologia nórdica.",
            "genero": "Ação/Aventura",
            "ano": "2018",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=K0u_kAWLJOA"
        },
        "Horizon Zero Dawn": {
            "preco": 0.27,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/3/3a/Horizon_Zero_Dawn_capa.png",
            "descricao": "Explore um mundo pós-apocalíptico dominado por máquinas.",
            "genero": "Ação/RPG",
            "ano": "2017",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=wzx96gYA8ek"
        },
        "Assassin's Creed Valhalla": {
            "preco": 0.29,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/9/9b/Assassin%27s_Creed_Valhalla_capa.png",
            "descricao": "Viva como um viking em uma aventura épica.",
            "genero": "Ação/RPG",
            "ano": "2020",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=ssrNcwxALS4"
        },
        "F1 2023": {
            "preco": 0.25,
            "imagem": "https://cdn.cloudflare.steamstatic.com/steam/apps/2108330/header.jpg",
            "descricao": "A experiência definitiva de Fórmula 1.",
            "genero": "Corrida",
            "ano": "2023",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=QFvNhsWMU0c"
        },
        "Elden Ring": {
            "preco": 0.33,
            "imagem": "c:/Users/a25679/Downloads/elden-ring2086.jpg",
            "descricao": "Explore as Terras Intermédias neste RPG de ação desafiador.",
            "genero": "RPG/Ação",
            "ano": "2022",
            "plataformas": "PC, PlayStation, Xbox",
            "trailer": "https://www.youtube.com/watch?v=E3Huy2cdih0"
        },
        "Spider-Man Remastered": {
            "preco": 0.28,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/0/0c/Spider-Man_PS4_capa.png",
            "descricao": "Viva as aventuras do Homem-Aranha em Nova York.",
            "genero": "Ação/Aventura",
            "ano": "2022",
            "plataformas": "PC, PlayStation",
            "trailer": "https://www.youtube.com/watch?v=Nt9L1jCKGnE"
        },
        "Super Mario Odyssey": {
            "preco": 0.22,
            "imagem": "https://upload.wikimedia.org/wikipedia/pt/8/8d/Super_Mario_Odyssey_capa.png",
            "descricao": "A aventura 3D definitiva do Mario pelo mundo.",
            "genero": "Plataforma",
            "ano": "2017",
            "plataformas": "Switch",
            "trailer": "https://www.youtube.com/watch?v=5kcdRBHM7kM"
        }
    }

    cols = st.columns(4)
    for idx, (nome, info) in enumerate(outros_jogos.items()):
        with cols[idx % 4]:
            st.image(info["imagem"], caption=nome, use_container_width=True)
            st.markdown(f"**{nome}**")
            st.markdown(f"**Preço:** €{info['preco']:.2f}")
            if st.button(f"Ver {nome}", key=f"ver_outro_{nome}"):
                st.session_state.jogo_selecionado = nome
                st.session_state.pagina = None
                st.rerun()

    if st.button("🔙 Voltar para Home", key="voltar_home_outros"):
        mudar_para_home()