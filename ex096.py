def area(c, l):
    ar = c * l
    print(f'O terreno com {c} m de comprimento e {l} m de largura tem aŕea {ar} m')


area(
    float(input('Comprimento do terreno [Metros]:')),
    float(input('Largura do terreno [Metros]:'))
)
