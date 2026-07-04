from source.pilotos import lista_pilotos, lista_equipos
from source.circuitos import lista_circuitos
from random import randint
class Piloto:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo
    
    def  estadisticas(self, concentracion, velocidad, resistencia, estadistica):
        self.concentracion = concentracion
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.estadistica = 0


"""
Este 'numero' sirve para recorrer la lista de pilotos y equipos del fichero pilotos.
    Si nos damos cuenta, usará siempre el primero piloto con el primer equipo.
        Esto lo quiero cambiar en un futuro, que se hagan los equipos aleatorios.
            Y que no se repitan los pilotos ni +2 por equipos.

    añadir ahora un randint para los equipos sería una chorrada, pero al menos se elgien equipos aleatorios.
"""
pilotos = []
for numero_pilotos in range(len(lista_pilotos)):
    piloto = Piloto(lista_pilotos[numero_pilotos], lista_equipos[randint(0, len(lista_equipos)-1)])  # Asignar un equipo aleatorio
    pilotos.append(piloto)  # Guardar en la lista

circuitos = []
class Circuito:
    def __init__(self, nombre, numero_vueltas):
        self.nombre = nombre
        self.numero_vueltas = numero_vueltas

for numero_circuitos in range(len(lista_circuitos)):
    circuito = Circuito(lista_circuitos[numero_circuitos], numero_vueltas=randint(20, 30))  # Asignar un número de vueltas aleatorio entre 20 y 30
    circuitos.append(circuito)


class Campeonato:
    def __init__(self, circuito, pilotos):
        self.circuito = circuito
        self.pilotos = pilotos
        self.resultados_carrera = {}

    def Carrera(self):
        for piloto in self.pilotos:
            piloto.estadisticas(randint(0, 100), randint(0, 100), randint(0, 100), 0)
            piloto.estadistica = piloto.concentracion + piloto.velocidad + piloto.resistencia
            
            self.resultados_carrera[piloto.nombre] = {
                "estadistica": piloto.estadistica,
                "concentracion": piloto.concentracion,
                "velocidad": piloto.velocidad,
                "resistencia": piloto.resistencia,
                "equipo": piloto.equipo
            }
        
        self.resultados_carrera = dict(sorted(self.resultados_carrera.items(), key=lambda item: item[1]["estadistica"], reverse=True))
        return self.resultados_carrera
    
for circuito in circuitos:
    campeonato = Campeonato(circuito, pilotos)
    campeonato.Carrera()
    
    print(f"Carrera en {circuito.nombre}:")
    for nombre, datos in list(campeonato.resultados_carrera.items())[:3]:
        print(f"{nombre}: {datos['estadistica']}")
    print(f"\n")