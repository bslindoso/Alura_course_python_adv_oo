class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)