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