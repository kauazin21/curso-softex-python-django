#DESAFIO DE PROGRAMAÇÃO: O "Instagram" Vazado

class Usuario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido


class Post:
    def __init__(self, texto, dono):
        self.texto = texto
        self.dono = dono


class RedeSocial:
    def __init__(self):
        self.banco_de_posts = []

    def criar_post(self, texto, usuario_logado):
        novo_post = Post(texto, usuario_logado)
        self.banco_de_posts.append(novo_post)
        print(f"  Post criado por {usuario_logado.apelido}!")

    def ver_meu_perfil(self, usuario_logado):
        print(f"\n  --- PERFIL DE {usuario_logado.nome.upper()} ---")
        print(f"  Usuário: {usuario_logado.apelido}")
        print("-" * 30)

        encontrou_algo = False

        for post in self.banco_de_posts:
            # AQUI ESTAVA O BUG! Agora só mostra os posts do usuário logado
            if post.dono == usuario_logado:
                print(f"     {post.texto} (Postado por: {post.dono.apelido})")
                encontrou_algo = True

        if not encontrou_algo:
            print("   (Nenhum post encontrado )")

        print("-" * 30 + "\n")

usuario_principal = Usuario("Mariana Silva", "@mari_do_caos")

usuario_secundario = Usuario("João Trollador", "@joao_mestre_do_troll")

minha_rede_social = RedeSocial()

minha_rede_social.criar_post("Acabei de descobrir que café é só água com ansiedade kkkkk", usuario_principal)
minha_rede_social.criar_post("Quem inventou segunda-feira tá devendo explicação pro universo", usuario_secundario)
minha_rede_social.criar_post("Minha planta morreu. Acho que agora sou oficialmente um serial killer", usuario_principal)
minha_rede_social.criar_post("Eu não tô procrastinando, tô fazendo um aquecimento de 8 horas pra começar", usuario_principal)
minha_rede_social.criar_post("Perdi meu celular dentro de casa pela 37ª vez essa semana. Alguém me adota?", usuario_secundario)

minha_rede_social.ver_meu_perfil(usuario_principal)