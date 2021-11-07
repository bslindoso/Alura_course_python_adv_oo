from filme import Filme
from serie import Serie

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

lista_de_programas = [vingadores, atlanta]

for programa in lista_de_programas:
    print(programa)