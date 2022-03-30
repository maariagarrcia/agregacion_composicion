# 3) En el último ejercicio de la sección sobre la herencia, se mostraron los límites
# de la herencia múltiple: acoplamientos de clases cuyo vínculo no es tan obvio, 
# atajos tomados en el código que tienen mucho riesgo de error. Este ejercicio utiliza 
# otro enfoque del problema: la asociación (ya sea composición o agregación).
# Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, 
# cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.
# Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.
# Enunciado: modifique el código para que el programa funcione de nuevo.


class Cristal:
    # Metodo constructor
    def __init__(self, superficie):
        self.__superficie = superficie
    # Atributo superficie
    def superficie(self):
        return self.__superficie

class Pared:
    def __init__(self, orientacion):
        self.__orientacion = orientacion
        self.__ventanas = []

    def ventanas(self):
        return self.__ventanas

    def superficie_cristal(self):
        superficie = 0
        for ventana in self.ventanas(): # ES UNA LISTA Y HAY Q RECORRERLA CIN UN BUCLE 
            superficie += ventana.superficie()
        return superficie

class Ventana:
    def __init__(self, pared, superficie, proteccion): # PARAMETROS DEL CONSTRUCTOR
        self.__pared = pared
        
        self.__cristal = Cristal(superficie)
        self.__pared.ventanas().append(self)
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.__proteccion = proteccion

    # Encapsulación de la superficie en un acestro, para conservar
    # privado el atributo SuperficieDeCristal.
    def superficie(self):
        return self.__cristal.superficie()

class Casa():
    def __init__(self, paredes):
        self.__paredes = paredes

    def paredes(self):
        return self.__paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes():
            superficie += pared.superficie_cristal()
        return superficie

## INSTANCIAMOS
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTEE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
ventana_norte = Ventana(pared_norte, 0.5, "persiana")
ventana_oeste = Ventana(pared_oeste, 1, "persiana")
ventana_sur = Ventana(pared_sur, 2, "estor veneciano")
ventana_este = Ventana(pared_este, 1, "persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_cristal())

# Una ParedCortina en una Pared
class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        self.__cristal = Cristal(superficie)

    def superficie_cristal(self):
        return self.__cristal.superficie() # self.clase.atributo()

pared_cortina = ParedCortina("SUR", 10)
casa = Casa([pared_norte, pared_oeste, pared_cortina, pared_este])
print(casa.superficie_cristal())
