#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
number = -70;

if number > 0:
    print (f"El número {number} es mayor que cero.");
elif number < 0:
    print (f"El número {number} es menor que cero.");
else:
    print ("El número es cero.");




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
primer_variable = "Soy tipo String";
segunda_variable = "30";

if type(primer_variable) == type(segunda_variable):
    print ("Las variables son del mismo tipo de dato.");
else:
    print ("Las variables son de diferentes tipo de datos.");




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for numero in range (0, 21):
    residuo = numero % 2;
    if numero > 0 and numero <= 20 and residuo == 0:
        print (f"El número {numero} es par");
    elif numero > 0 and numero <= 20 and residuo != 0:
        print (f"El número {numero} es impar");
    else:
        print (f"El número {numero} no esta en el rango entre 1 y 20");





# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
i = 0;
for i in range (0, 6):
    potencia = i**3;
    print (f"El número {i} al elevarlo al cubo resulta {potencia}");




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
num = 10;
j = 0;

for j in range (j, num):
    print (f'Numero de ciclo ejecutado: {j}');




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
valor = 10;
contador = 0;
factorial = 1;

if type(valor) == int:
    if valor > 0:
        while  (contador < valor):
            contador = contador + 1;
            factorial = contador * factorial;
        print (f"El factorial de {valor} es {factorial}");
    else: 
        print (f"Su valor {valor} debe ser mayor a cero.");
else:
    print (f"El valor {valor} no es un número.");




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
counter = 0;
index = 0;
producto = 0;

while counter < 10:
    counter = counter + 1;
    print (f"Tabla del {counter}");
    for index in range (0, 11):
        producto = counter * index;
        print(f"{counter} * {index} = {producto}");




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
indice = 1;
count = 0;

for indice in range (1, 6):
    if (indice == 1):
        print (f"El ciclo for se ha ejecutado {indice} vez.");
    else:
        print (f"El ciclo for se ha ejecutado {indice} veces.");
    while count < 3:
        count = count + 1;
        if (count == 1):
            print (f"   El ciclo while dentro del ciclo for {indice} se ha ejecutado {count} vez.");
        else:
            print (f"   El ciclo while dentro del ciclo for {indice} se ha ejecutado  {count} veces.");
    count = 0;




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
limite = 30;
print (f"Números primos entre 0 y {limite}");
es_primo = True;

k = 0;
for k in range (0, limite + 1):
    if k >= 2:
        for divisor in range (2, k):
            if (k % divisor == 0):
                es_primo = False;
        if (es_primo):
            print (k);
        else:
            es_primo = True;



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
limite = 30;
print (f"Números primos entre 0 y {limite}");
es_primo = True;

k = 0;
for k in range (0, limite + 1):
    if k >= 2:
        for divisor in range (2, k):
            if (k % divisor == 0):
                es_primo = False;
                break;
        if (es_primo):
            print (k);
        else:
            es_primo = True;




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
## Código de números primos sin optimizar ##
limite = 30;
print (f"Números primos entre 0 y {limite}");
es_primo = True;
total_de_ciclos = 0;

k = 0;
for k in range (0, limite + 1):
    if k >= 2:
        for divisor in range (2, k):
            total_de_ciclos += 1;
            if (k % divisor == 0):
                es_primo = False;
        if (es_primo):
            print (k);
        else:
            es_primo = True;


# In[57]:
## Código de números primos optimizado ##
print (f"Números primos entre 0 y {limite}");
es_primo = True;
ciclos_sin_ejecutar = 0;

k = 0;
for k in range (0, limite + 1):
    if k >= 2:
        for divisor in range (2, k):
            ciclos_sin_ejecutar += 1;
            if (k % divisor == 0):
                es_primo = False;
                break;
        if (es_primo):
            print (k);
        else:
            es_primo = True;

optimizacion = ciclos_sin_ejecutar * 100/total_de_ciclos;

print (f"Ciclos no ejecutados {ciclos_sin_ejecutar}, de un total de {total_de_ciclos}");
print (f"El código quedó optimizado un {round(optimizacion , 2)}% ");




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
limite_inferior = 100;
limite_superior = 300;

while (limite_inferior - 1 <= limite_superior):
    limite_inferior += 1;
    if (limite_inferior % 12 != 0):
        continue;
    else:
        print (f"El número {limite_inferior} es divisible entre 12");




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
print (f"Buscador de números primos consecutivos según el usuario.");
es_primo = True;

ejecutar = input ("Desea buscar el primer número primo. y/n");
if (ejecutar == "y" or ejecutar == "Y"):
    k = 1;
    num_a_verificar = 2;
    while (k == 1):
        for divisor in range (2, num_a_verificar):
            if (num_a_verificar % divisor == 0):
                es_primo = False;
                break;
        if (es_primo):
            print (num_a_verificar);
            user_response = input ("Desea continuar con la búsqueda del siguiente número primo y/n.");
            if (user_response == "y" or user_response =="Y"):
                num_a_verificar += 1;
                k == 1;
            else:
                k == 0;
                break;
        else:
            es_primo = True;
            num_a_verificar += 1;

print ("Se finalizó la búsqueda.");



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
limite_menor = 100;
limite_mayor = 300;

while limite_menor <= limite_mayor:
    if (limite_menor % 3 == 0 and limite_menor % 6 == 0):
        print (f"El número {limite_menor} es divisible entre 3 y multiplo de 6");
        break;
    limite_menor += 1;



# %%
