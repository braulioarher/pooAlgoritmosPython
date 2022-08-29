# Curso de Programacion Orientada a Objetos en python

Para crear una clase en python basta con utilizar la pabla class seguido del nombre de la clase ejemplo:

        class Hotel:
            pass

Para crear una instancia a una clase creada se debe de llamar al constructor de la clase

        hotel = Hotel()

## Atributos de la instancia

En python todo es un objeto y todo tiene un tipo.

En python nosotros usamos el metodo init que es un constructor

        class <nombre_de_la_clase>(<super_clase>):
            
            def __init__(self, <params>):
                <expresion>

            def <nombre_del_metodo>(self, <params>):
                <expresion>

al crear una clase el primer metodo que se ejecuta es el constructor el cual se define con __init__

la palabra self simplemente hace referencia a esa misma clase donde fue declarado el atributo o el metodo

Las clases son un tipo de molde que las pueden utilizar cualquir instancias

Las clases son moldes y las instancias son objetos

        Variables de instancias

## Decomposicion

Es partir un problema en problemas mas pequenos un ejemplo de decomposicion es un automovil un automovil tiene diferentes sistemas que funcionan independientemente pero cuando se juntas forman completamente un automovil
en nuestro programa podriamos definir diferentes clases por ejemplo la clase automovil, luego la clase motor, la clase suspencion etceterea

## Abstraccion

La abstraccion es enfocarse en informacion relevante

La abstraccion la vemos en todas partes en un automvil, un elevador etcetera

La abtraccion 

## Funciones decoradoras

Una funcion decoradora es una funcion que agrega funcionalidades adicionales a otra funcion ejemplo:

        def funcion_decoradora(funcion_externa):

                funcion_interna():
                print("")
                funcion_externa()

        return funcion_interna()

        @funcion_decoradora
        def funcion_externa():
                print(20 + 30)

        funcion_externa()
        ##Decorado de la funcion decoradora
        ##50

Para mandar llamar a la funcion decoradora se debe de porner un @funcion_decoradora una linea antes de la funcion que queremos decorar

Nota importante es que la funcion decoradora la podemos aplicar a cuantas funciones queramos por lo que si en un programa queremos modificar 30 funciones no tenemos meternos con las funciones de una a una si no que podemos simplemete usar @funcion_decoradora

Otra utilidad de ejemplo es que al trabajar con bases de datos debesmo a abrir y cerrar comunicacion por lo que podemos implementar esta funcion decoradora para hacer el trabaja mas automatico

## Encapsulacion Getters and Setters

La encapsulacion permite:

                -Agrupar datos y su comportamiento
                -Controlar el acceso a dichos datos
                -Previene modificaciones no autorizadas

### @property

Es un contructor de objetos que se usa como decoradorar de una funcion cuando tenemos nuestra funcion y queremos implementar metos de getter y setter vasta con usar @property para definir a nuestro getter y @funcion_get.setter para definir nuestro settter

                class Celsius:
                    def __init__(self, temperature=0):
                        self.temperature = temperature

                    def to_fahrenheit(self):
                        return (self.temperature * 1.8) + 32

                    @property
                    def temperature(self):
                        print("Getting value...")
                        return self._temperature

                    @temperature.setter
                    def temperature(self, value):
                        print("Setting value...")
                        if value < -273.15:
                            raise ValueError("Temperature below -273 is not possible")
                        self._temperature = value


                human = Celsius(37)

                print(human.temperature)

                print(human.to_fahrenheit())

                coldest_thing = Celsius(-300)

## Herencia

-La herencia permite modelar una jerarquia de clases
-Permite compartir comportamiento comun en la jerarquia
-Al padre se conoce como superclase y al hijo como subclase

Un aspecto importante de la programacion orientada a objetos es la reutilizacion de codigo y mediante herencias podemos reutilizar comportamientos en comun de un objeto padre a un objeto hijo esto facilita mucho la escritura de codigo y su mantenimiento

## Poliformismo

-La habilidad de tomar varias formas
-En python nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase

En python el pilimorfismo a diferencia de la herencia cambia o modifica los metodos dependiendo de la funcion que realice y dependiendo a que objeto se le aplique

## Complejidad algoritmica

Una forma de medir la complejidad algoritmica es medir el tiempo de ejecucion de un algoritmo esto se logra con la funcion time.time() del modulo time de python, a pesar de que es un metodo que mide tiempo este puede variar mucho ya que depende de muchos factores como la capacidad del dipositivo en que se ejecuta y las aplicaciones corriendo en ese momento

## Conteo abstracto de operacion

## Notacion asintotica

-No importan variaciones pequenas
-El enfoque se centra en lo que pasa conforme el tamano del problema se acerca al infinito
-Mejor de los casos, promedio, peor de los casos
-Big O
-Nada mas importante el termino de mayor tamano

        Un loop => crecimiento lineal.                          O(n)
        Un loop dentro de otro => crecimiento cuadratico        O(n**2)
        Llamadas recursivas => crecimiento exponecncial.        O(a**n)

## Clases de complejidad algoritmica

-O(1) Constante
-O(n) Lineal
-O(log n) Logaritmica
-O(n log n) log lineal
-O(n ** 2) Polinomial*
-O(2**n) Exponencial

Debemos evitar los algoritmos exponeciales o recursivos si lo que buscamos es rendimiento este tipos de algoritmos solo sirven para determinadas cosas

La busqueda binaria son de los algorimos mas utilizados ene la industria

## Algoritmos de busqueda y abstraccion

## Busqueda lineal

Busca en todos los elementos de manera secuencial en el peor de lo casos es que se tengan millones o bastantes elementos en una lista

## Busqueda binaria

Utiliza la premisa divide y conquista el problema se divide en 2 cada iteracion

Este algoritmo asume que la lista esta ordenada por lo que se debe de recorrir a un algoritmo para ordenar una lista

Cambiamos tiempo por espacio si queremos menos tiempo tendriamos que ocupar mas memoria y vis eversa

## Ordenamiento de burbuja

El ordenamiento de burbuja itera una lista comparando elemento por elemento en caso de que un elemento sea mayor a otro los elementos se cambian de posicion

Ordenamiento de burbuha garantiza que podemos encontrar al elemento mas grande en un solo paso o sea O(n) que es lineal

El ordenamiento de burbuja tiene una complejidad algoritmica polinomial O(n**2) lo que sigunifica que si tenemos una lista de elementoa arribal del millo este algoritmo no se comportaria correctamente

## Ordenamiento por insersion

El ordenamiento por insersion es intuitivo y facil de implementar pero es poco eficientes para listas de gran tamano la caracteristicas es que no requiere memoria aidiciona pra realizar el ordenamiento

## Ordenamiento por mezcla

El ordenamiento por mezcla es un algoritmo de divide y conquista primero divide una lista en partes iguales hasta que queden sublistas de 1 o 0 elementos, Luego las recombina en forma ordenada

## Ambientes virtuales

-Permite aislar el ambiente para poder instalar diverss versiones de paqutes

- Apartit de python 3 se incluye una libreria estandar en el modulo venv

-Ningun ingeniero profesional de Python trabaja sin ellos

### Pip

- Pip permite descargar paquete de terceros para utilizar en nuestro programa

- Permite compartir nuestros paquetes con terceros

- Permite especificar la cersion que necesitemso

Para  crear un entorno virtual en python 3 se utiliza el siguiente comando:

                python3.10 -m venv venv

Para activar el ambiente virtual se utiliza el comando

                source env/bin/activate