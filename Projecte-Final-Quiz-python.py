print("Fes aquest quiz per saber quant saps de cultura general!")

preguntes_facil = [
    ["Quina és la capital de Francia? Madrid, Paris o Brasil: ", "Paris"],
    ["Quina és la capital d'Alemanya? Paris, Bruselles o Berlin: ", "Berlin"],
    ["En quin any va morir Francisc Franc? 1975, 1990 o 1950: ", "1975"],
    ["Com es diu el típic postre italià al qual es tiren pols de café per sobre? Tiramisú, Pastís de formatge o Crema Catalana: ", "Tiramisú"],
    ["Quan es va crear el fútbol? 1880, 1848 o 1856: ", "1848"],
    ["Quan es va descobrir América? 1500, 1490 o 1492: ", "1492"],
    ["Com es diu la dona del futbolista Sergio Ramos? Pilar Rubio, Juanjose o Paloma Rubio: ", "Pilar Rubio"],
    ["Quina és la capital d'Uruguay? Montefoto, Montevideo o Montserrat: ", "Montevideo"],
    ["En quin continent es roba la India? Asia, America o Africa: ", "Asia"],
    ["Quin és el planeta més proper al Sol? La Terra, Mercuri o Mart: ", "Mercuri"]
]

preguntes_normal = [
    ["Quantes estrelles te la bandera d'Estats Units? 51, 52, 50 o 55: ", "50"],
    ["Qué idioma es parla a Brasil? brasiler, portugués, espanyol o anglès: ", "portugués"],
    ["Qui  va pintar la Mona Lisa? Picasso, Kellerman, Da Vinci o Aleix: ", "Da Vinci"],
    ["Quina és la capital de Noruega? Oslo, Estocolmo, Helsinki o Viena: ", "Oslo"],
    ["Quants anys va durar la Guerra dels 100 anys? 102, 112, 116 o 100: ", "116"],
    ["A quin país es troba la ciutat de Estrasburgo? Croàcia, Francia, Alemanya o Romania: ", "Francia"],
    ["Quina d'aquestes ciutats es troba a Croàcia? Zadar, Estocolmo, Chad o Liechtenstein: ", "Zadar"],
    ["Qui va inventar el telèfon? Gerard Durà, Michael Scofield, Alexander Graham Fell o Jack Sparrow: ", "Alexander Graham Fell"],
    ["Quina és la moneda oficial del Japó? Euros, Dolars, Pilns o Yens: ", "Yens"],
    ["Com es deia el primer home que va trepitjar la Luna? Antonio Lobato, Antonio Merchi, Neil Armstrong o Michael Phelps: ", "Neil Armstrong"]
]

preguntes_dificil = [
    ["En quin any va començar la Guerra Civil Espanyola? 1936, 1935, 1938, 1940 o 1937: ", "1936"],
    ["Com es diu l'autor del llibre 'Charlie i la fàbrica de xocolata'? willy wonka, guileano mortes, roald dahl, descot scotland o scoty sponge: ", "roald dahl"],
    ["En quin any va acabar la Segona Guerra Mundial? 1945, 1950, 1948, 1943 o 1947: ", "1945"],
    ["Quina és la capital de Polònia? lealton, varsinaso, varsovia, trisel o serfa: ", "varsovia"],
    ["En quin continent es troba el país Guyana? america-nord o sud, africa, asia o europa: ", "america-nord o sud"],
    ["En quin any va caure l'imperi romà? 476 d.c, 476 a.c, 467 d.c, 467 a.c o 477 d.d: ", "476 d.c"],
    ["Quin filòsof grec va ser mestre d'Alexandre el Gran? socrates, hermes, aristoteles, apolo o hercules: ", "aristoteles"]
]

preguntes_legendaria = [
    ["En quin any es va crear la UE? 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998 o 1999: ", "1993"],
    ["En quin any es va crear l'imperi romà? 20 a.c, 21 a.c, 22 a.c, 23 a.c, 24 a.c, 25 a.c, 26 a.c, 27 a.c, 28 a.c o 29 a.c: ", "27 a.c"],
    ["En quin any es va signar el Tractat de Pau de Westfàlia que va acabar la Guerra dels Trenta Anys? 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653 o 1654: ", "1648"],
    ["En quin dia va sortir Cristòfor Colom d'Amèrica? 3 d'agost de 1492, 15 de gener de 1493, 7 de maig de 1491, 23 d'abril de 1490, 5 d'octubre de 1495, 12 de desembre de 1499, 9 de setembre de 1497, 28 de febrer de 1480, 8 de març de 2941 o 31 de juliol de 1423: ", "3 d'agost de 1492"],
    ["En quin any David Martirosyan va dir: 'basta!' i es va comprar una casa de 340 milions de dòlars amb 7 piscines, 13 habitacions, 4 helicòpters i el millor, un vàter d'or? 1988, 1999, 1734, 1877, 1234, 4321, 2025, 2026, 1789 o 3810: ", "1999"],
    ["En quin any Iker Díaz va començar a invertir en la moneda de udindindindun i es va fer ultra mega milionari? 1234, 5678, 9101, 1213, 1415, 1617, 1819, 2021, 2223 o 'el de sosiale': ", "2223"]
]

dificultat = input("Escull una dificultat (facil, normal, dificil o legendaria): ")

if dificultat == "facil":
    preguntes = preguntes_facil
elif dificultat == "normal":
    preguntes = preguntes_normal
elif dificultat == "dificil":
    preguntes = preguntes_dificil
elif dificultat == "legendaria":
    preguntes = preguntes_legendaria
else:
    print("Dificultat no vàlida.")
    exit()

num_jugadors = input("Quants jugadors sou? ")

jugadors = []
puntuacions = []

i = 0
while i < int(num_jugadors):
    nom = input("Nom del jugador " + str(i + 1) + ": ")
    jugadors = jugadors + [nom]
    puntuacions = puntuacions + [0]
    i = i + 1

print("\nComença el quiz!\n")

i = 0
while i < len(preguntes):
    jugador_actual = i % int(num_jugadors)
    print(jugadors[jugador_actual] + ", és el teu torn.")
    resposta = input(preguntes[i][0])

    if resposta == preguntes[i][1]:
        print("Correcte!\n")
        puntuacions[jugador_actual] = puntuacions[jugador_actual] + 1
    else:
        print("Incorrecte. La resposta correcta era: " + preguntes[i][1] + "\n")
    i = i + 1

print("Resultats finals:")
i = 0
while i < int(num_jugadors):
    print(jugadors[i] + ": " + str(puntuacions[i]) + " punts")
    i = i + 1









              
