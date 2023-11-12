#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
ciudades = ["México", "Londres", "Nueva York", "Barcelona", "Buenos Aires", "Guadalajara"];
print (ciudades);



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:
print(ciudades[1]);



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
print (ciudades[1:4]);

#Por medio del ciclo for
index = 1;
for index in range (1, 4):
    print (ciudades[index]);




# 4) Visualizar el tipo de dato de la lista

# In[12]:
print(type(ciudades));




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:
print (ciudades[2:]);

#Por medio del ciclo for
for index in range (2, len(ciudades)):
    print (ciudades[index]);




# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
print (ciudades[:4]);

#Por medio del ciclo for
for index in range (0, 4):
    print (ciudades[index]);


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:
ciudades.append("Nueva York");
ciudades.append("Bogota");
print(ciudades);








# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
ciudades.insert(3, "Monterrey");




# In[21]:
print(ciudades);



# 9) Concatenar otra lista a la ya creada

# In[22]:
cities_other_list = ["California", "Reino Unido", "Puebla", "Tehuacán", "Guadalajara"];
ciudades.extend(cities_other_list);
print(ciudades);



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:
print(ciudades.index("Nueva York"));




# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:
print(ciudades.index("Bogotá"));
## Sucede un error




# 12) Eliminar un elemento de la lista

# In[25]:
ciudades.remove("Nueva York");
print(ciudades);




# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:
ciudades.remove("New York");
## Sucede un error




# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
ultima_ciudad = ciudades.pop();
print(ultima_ciudad);




# 15) Mostrar la lista multiplicada por 4

# In[29]:
print(ciudades * 4);



# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
tupla_numerica = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20);
print(tupla_numerica);



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print(tupla_numerica[10: 16]);



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
num_a_evaluar1 = 20;
num_a_evaluar2 = 30;

if (20 in tupla_numerica):
    print (f"El numero {num_a_evaluar1} está en la tupla.");
else:
    print (f"El numero {num_a_evaluar2} no está en la tupla.");

if (30 in tupla_numerica):
    print (f"El numero {num_a_evaluar1} está en la tupla.");
else:
    print (f"El numero {num_a_evaluar2} no está en la tupla.");




# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
ciudad_a_agregar = "París";

if (ciudad_a_agregar in ciudades):
    print (f"La ciudad {ciudad_a_agregar} ya se encuentra en la lista.");
else:
    ciudades.append(ciudad_a_agregar);
    print (f"La ciudad {ciudad_a_agregar} se ha agregado a la lista.");




# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
elemento_en_tupla = 10;
elemento_en_lista = "Monterrey";

print (f"El número {elemento_en_tupla} se encuentra {tupla_numerica.count(elemento_en_tupla)} veces en la lista.");
print (f"La ciudad {elemento_en_lista} se encuentra {ciudades.count(elemento_en_lista)} veces en la lista.");




# 21) Convertir la tupla en una lista

# In[52]:
nueva_lista = list(tupla_numerica);
print (nueva_lista);




# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
num1 = tupla_numerica[0];
num2 = tupla_numerica[1];
num3 = tupla_numerica[2];

print(num1, num2, num3);




# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
diccionario_ciudades = dict();

for i in range (0, len(ciudades)):
    diccionario_ciudades[f"Ciudad {i+1}"] = ciudades[i] ;

diccionario_ciudades ["paises"] = "";
diccionario_ciudades ["continentes"] = ["America", "Europa"];

print (diccionario_ciudades);





# 24) Imprimir las claves del diccionario

# In[59]:
print (diccionario_ciudades.keys());



# 25) Imprimir las ciudades a través de su clave

# In[61]:
print (diccionario_ciudades.values());



