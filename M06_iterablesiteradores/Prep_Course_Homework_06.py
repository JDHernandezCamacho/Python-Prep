#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
#Utilizando insert, se vuelve más compleja ya que utiliza dos variables (de control y de índice) que se van sumando.
negative_list = [];
x = -15;
index = 0;
while (x <= -1):
    negative_list.insert(index, x);
    index += 1;
    x += 1;
print (negative_list);

#Utilizando apend, esta segunda opción en más simple al solo usar una variable de control.
x = -15;
negative_list2 = [];
while (x < 0):
    negative_list2.append(x);
    x += 1;
print (negative_list2);




# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
##### Con este código se sabe si una variable es iterable 
#from collections.abc import Iterable;
# cadena = "Diego";
# positive_list = [1, 2 ,3 ,4, 5];
# print(isinstance(negative_list, Iterable));
print ("Usando While.");
index = 0;
while index < len(negative_list):
    if (negative_list[index] % 2 == 0):
        print (negative_list[index]);
    index += 1;




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
print ("Usando for.");
for elemento in negative_list:
    if (elemento % 2 == 0):
        print (elemento);




# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
# Utilizando While
print("Usando while.")
iterator = 0;
while (iterator < 3):
    print (negative_list[iterator]);
    iterator += 1;

#Utilizando for
print ("Usando for.")
for element in negative_list[0:3]:
    print (element);



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
for indice, element in enumerate(negative_list):
        print(indice, element);



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20];




# In[11]:
indice = 0;
while indice < 20:
    if (indice + 1 != lista[indice]):
        lista.insert(indice, indice + 1);
    indice += 1;

print(lista);




# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
i = 2;
sucesion_fibonacci = [0, 1];
while i < 30:
    numero_a_insertar = sucesion_fibonacci[i-1] + sucesion_fibonacci[i-2];
    sucesion_fibonacci.insert(i, numero_a_insertar);
    i += 1;
print(sucesion_fibonacci);




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:
suma = 0;
for elemento in sucesion_fibonacci:
    suma = suma + elemento;
print (suma);



# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
## Sólo mencionar que la información que precisan en el ejemplo esta incorrecta
## La forma correcta sería 
#          n(i)/n(i-1)
#          n(i-1)/n(i-2)

## Mediante el ciclo while:
i = 29;
ajustador = 0;
while i > 24:
    numero_aureo = sucesion_fibonacci[i] / sucesion_fibonacci[i-1];
    # print(f"Posicion:{i} valor:{sucesion_fibonacci[i]} / posicion:{i-1} valor:{sucesion_fibonacci[i-1]}, es igual {numero_aureo}");
    print(numero_aureo);
    i -= 1;



# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
cadena = "Hola mundo. Esto es una practica del lenguaje de programación Python";

for i, n in enumerate(cadena):
    if ("n" == n):
        print (f"La letra 'n' se encuentra en la posición {i}");




# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
animales = {"domesticos": ["perro", "gato", "perico", "gallina", "vaca", "cerdos"],
            "salvajes": ["leon","oso", "lagarto", "tigre", "lobo"]};

# Primera forma de acceder a las claves
for clave in animales:
    print (clave);

# Segunda forma de acceder a las claves
print(f"El diccionario 'ánimales' tiene las claves {animales.keys()}");

# Tercera forma de acceder a las claves
print (dict.keys(animales));




# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
cadena = "Hola mundo. Esto es una practica del lenguaje de programación Python";



# In[45]:
#Convirtiendo la cadena a lista
print ("Iterando con ciclo for.");
cadena = "Hola mundo. Esto es una practica del lenguaje de programación Python";
lista_from_cadena = list(cadena);

#Iterando con for
conteo = 0;
for i, element in enumerate(lista_from_cadena):
    if (element == "a"):
        conteo += 1;
        print(f"El conteo de la búsqueda de la letra 'a' es de {conteo}.")

#Iterando con while
print ("\nIterando con ciclo while.");
index_lista = 0
while index_lista < len(lista_from_cadena):
    if (lista_from_cadena[index_lista] == "a"):
        print(f"Letra'a' encontrada en la posición {index_lista}.");
    index_lista += 1;

#Iterando con la función iter
print ("\nIterando con iter.");
my_iterator = iter(lista_from_cadena);
next(my_iterator);
print("Iteracion ejecutada 1 vez.");
next(my_iterator);
print("Iteracion ejecutada 2 veces.");





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
#Creando las listas a partir del diccionario del punto 11.
lista_animales = list(animales.values());
animales_domesticos = [];
animales_salvajes = [];
i = 0;
while i < len(lista_animales):
    for elemento in lista_animales[i]:
        if i == 0:
            animales_domesticos.append(elemento);
        else:
            animales_salvajes.append(elemento);
    i += 1;


#Uniendo las listas con funcion zip 
lista_zip = zip(animales_domesticos, animales_salvajes);
print(f"Unión de dos listas con función zip: \n {list(lista_zip)}\n\n")
lista_zip = zip(animales_domesticos, animales_salvajes);
for elem in lista_zip:
    print(elem);

## Si las listas no tienen los mismos numeros de datos, se perderan estos, solo forma combinaciones




# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:
#Utilizando ciclo for
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100];

divisibles_7 = [];
for elemen in lis:
    if (elemen % 7 == 0):
        divisibles_7.append(elemen);
print(divisibles_7);

#Utilizando condicionales
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100];
multiplos_7 = [i for i in lis if i % 7 == 0];
print(multiplos_7);




# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']];




# In[51]:





# In[57]:
elementos_totales = 0;
for index in lis:
    if (type(index) != list):
        elementos_totales += 1;
    else:
        elementos_totales += len(index);

print(elementos_totales);




# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']];
print(f"Lista original. \n {lis}");

for index, elemento in enumerate(lis):
    if (type(elemento) != list):
        # print (index, elemento);
        lis[index] = list([elemento]);

print(f"\nLista convertida.\n {lis}");



# %%
