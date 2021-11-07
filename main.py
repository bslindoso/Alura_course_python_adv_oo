from filme import Filme
from serie import Serie

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} minutos : Likes: {vingadores.like}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} temporadas : Likes: {atlanta.like}')