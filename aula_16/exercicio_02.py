class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Titulo: {self.titulo}, duração: {self.duracao_seg}.")

    def __str__(self):
        return f"{self.titulo}"

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Titulo: {self.titulo}, Artista: {self.artista}, duração: {self.duracao_seg}.")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Titulo: {self.titulo}, Resolução: {self.resolucao}, duração: {self.duracao_seg}.")

m1 = Musica("Superman", 180, "Eminem")
v1 = Video("OZ", 120, "2040x3060")


dicionarios_mida:dict[str, list[Midia]] = {"musicas":[], "videos":[]}
dicionarios_mida["musicas"].append(m1)
dicionarios_mida["videos"].append(v1)

print(dicionarios_mida)

for item in dicionarios_mida.values():
    for midia in item:
        midia.exibir()
