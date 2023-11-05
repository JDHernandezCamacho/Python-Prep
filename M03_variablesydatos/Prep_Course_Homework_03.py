#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
a = 2.71;
print(a);



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5));




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(a));




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = "Juan Diego Hernández Camacho";
print(nombre);



# 5) Crear una variable que contenga un número complejo

# In[3]:
complejo = 2 + 1j;
print(complejo);




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(complejo));




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
numero_pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
var1 = "True";
var2 = True;
print (var1 == var2);




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print("La variable 1 es de tipo ", type(var1));
print("La variable 2 es de tipo ", type(var2));




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
numero_entero = 30;
numero_decimal = 2.981;
suma = numero_entero + numero_decimal;
print(suma);


# 11) Realizar una operación de suma de números complejos

# In[2]:
complejo1 = 15 + 8j;
complejo2 = 12 - 10j;
suma_complejos = complejo1 + complejo2;
print(suma_complejos);


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
numero_real = 15;
suma_complejo_real = suma_complejos + numero_real;
print(suma_complejo_real);


# 13) Realizar una operación de multiplicación

# In[5]:
producto = 3 * numero_real;
print(producto);


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
potencia = 2 ** 8;
print(potencia);

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27 / 4;
print(cociente);


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
cociente_entero = int(cociente);
print(cociente_entero);


cociente_int = 27 // 4;
print(cociente_int);

# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
resto = 27 % 4;
print (resto);




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
resultado = (4 * cociente_int) + resto;
print(resultado);




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
mi_edad = 30;
mi_telefono = 1234567890;
mi_pais = 'Mexico';
mi_estado = 'Puebla';

concat = "Hola, soy " + nombre + " vivo en " + mi_estado + ", " + mi_pais + ".";
persona = f"Hola! Mi nombre es {nombre} actualmente radico en {mi_estado} ubicado en {mi_pais}, tengo {mi_edad} años de edad y mi número de teléfono es: {mi_telefono}, contactame.";

print(concat);
print(persona);


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
string_compare1 = "2";
int_compare1 = 2;
print(string_compare1 == int_compare1);

## Un valor de ellos es de tipo string, mientras que el otro es de 
## tipo entero


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print (int(string_compare1) == int_compare1);

print(string_compare1 == str(int_compare1));



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float('3,8');

    ## Por que tiene una coma "," en lugar del punto decimal "."




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
var = 3;
var -= 1;

print (var);




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1 << 2);

## La simbología '<<' indica desplazamiento
## es decir, el primer núero se dezplazará
## el número de veces que indica el segundo número
## En este caso, el número uno se dezplazará dos
## lugares a la izquierda y el resto se rellena
## con ceros, quedando 100 en número binario

## El sistema binario es la forma de expresión
## numérica mediante ceros y unos, realizando 
## operaciones de potencias de forma ascendente
## de derecha a izquierda [4,3,2,1,0] con base "2" 
## y la suma de las potencias calculadas.

## El número 100 en binario índica los iguiente:
##  1*(2^2) + 0*(2^1) + 0*(2^0) = 1*4 + 0*2 + 0*1 = 4






# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

operacion2 = 2 + "2";
print(operacion2);

## Un valor de ellos es un número de tipo entero
## mientras que el otro es una variable de tipo string
## para que estos dos tipos de variables se puedan sumar,
## concatenar o unir, es necesario convertirlas al mismo 
## tipo.



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
string4 = "Juan Diego Hernández Camacho ";
repetir = 6;

print(repetir * string4, "el estring ", string4, "se repite", repetir, " veces");



# %%
