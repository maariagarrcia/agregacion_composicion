# 2) Teniendo en cuenta el siguiente código, explique por qué 
# el mensaje Yang destruido, se muestra después del signo de interrogación. 
# ¿Qué hay que hacer para que aparezca antes?

## Definimos las clases 
class Yin():
    pass

class Yang():
    def __del__(self):
        # Cuerpo del destructor
        print("Yang destruido")


yin = Yin()     # instanciamos
yang = Yang()   # instanciamos
yin.yang = yang  #  Ying pasa a tener un atributo de la clase yang  
# el recolector de basura es una entidad que monitoriza las áreas de memoria
# y las libera cuando ya no se hace ninguna referencia a ellas, ya sea por una
# variable, un método, una clase, etc.

print(yang)

print(yang is yin.yang)  # TRUE

del(yang)
print("?")  # ? pero esto sale primero antes que yang destruido