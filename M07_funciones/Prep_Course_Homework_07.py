#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def es_numero_primo (numero, es_primo = True):
    if numero >= 2:
        for divisor in range (2, numero):
            if (numero % divisor == 0):
                es_primo = False;
                return es_primo;
        if (es_primo):
            return es_primo;
        else:
            es_primo = True;
            return es_primo;
    return False;

print(es_numero_primo(22));




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
lista_de_primos = [];
def comprobar_primos (lista, es_primo = True):
    print(f"Lista identificada: {lista}");
    for numero in lista:
        es_primo = es_numero_primo(numero);
        if (es_primo):
            lista_de_primos.append(numero);
    return lista_de_primos;

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17];
lista_creada = comprobar_primos(lista_de_numeros);
print (f"Numeros primos en la lista: {lista_creada}");



# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def moda (lista_recibida):
    numeros_repetidos = [];
    for i in range(len(lista_recibida)):
        for j in range(len(lista_recibida)):
            if i != j:
                if lista_recibida[i] == lista_recibida[j] and lista_recibida[i] not in numeros_repetidos:
                    numeros_repetidos.append(lista_recibida[i]);
    
    lista_conteo = [];
    for i in range(len(numeros_repetidos)):
        contador = 0;
        for j in range(len(lista_recibida)):
            if numeros_repetidos[i] == lista_recibida[j]:
                contador += 1;
            lista = [numeros_repetidos[i], contador];
        lista_conteo.append(lista);
        
    mayor = 0;
    lista_moda = [];
    for i in range(len(lista_conteo)):
        for j in range(len(lista_conteo[i])):
            if lista_conteo[i][1] > mayor:
                mayor = lista_conteo[i][1];
                lista_moda = lista_conteo[i];

    return (f"La moda es el número {lista_moda[0]} con una frecuencia de {lista_moda[1]} veces.");
                    

lista = [1,2,2,2,2,2,2,2,3,1,1,1,4,5,5,5,6,7,5,7,6,8,9,8,7,8,5,6,8];
moda = moda(lista);
print(moda);




# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def conversion_temperatura (valor, unidad_medida, medida_a_convertir):
    if unidad_medida == "Celcius" and medida_a_convertir == "Fahrenheit":
        fahrenheit = (valor * 9/5) + 32;
        return (f"{valor}°C equivalen a {fahrenheit}°F.");
    elif unidad_medida == "Fahrenheit" and medida_a_convertir == "Celcius":
        celcius = (valor - 32) * 5/9;
        return (f"{valor}°F equivalen a {celcius}°C.");
    elif unidad_medida == "Celcius" and medida_a_convertir == "Kelvin":
        kelvin = valor + 273.15;
        return (f"{valor}°C equivalen a {kelvin}°K.");
    elif unidad_medida == "Fahrenheit" and medida_a_convertir == "Kelvin":
        celcius = (valor - 32) * 5/9;
        kelvin = celcius + 273.15;
        return (f"{valor}°F equivalen a {kelvin}°K.");
    elif unidad_medida == "Kelvin" and medida_a_convertir == "Celcius":
        celcius = valor - 273.15;
        return (f"{valor}°K equivalen a {celcius}°C.");
    elif unidad_medida == "Kelvin" and medida_a_convertir == "Fahrenheit":
        celcius = valor - 273.15;
        fahrenheit = (celcius * 9/5) + 32;
        return (f"{valor}°K equivalen a {fahrenheit}°F.");
    else:
        return (f"Favor de corroborar sus datos.")


conversion = conversion_temperatura(300, "Kelvin", "Celcius");
print(conversion);




# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
escalas_temperaturas = ["Celcius", "Fahrenheit", "Kelvin"];

for i in range (len(escalas_temperaturas)):
    for j in range (len(escalas_temperaturas)):
        if escalas_temperaturas[i] != escalas_temperaturas[j]:
            print (conversion_temperatura(0, escalas_temperaturas[i], escalas_temperaturas[j]));




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
## Calculando el factorial de un número
def factorial (numero):
    if (type(numero) != int):
        return (f"Lo sentimos {numero} no es un número entero.")
    else:
        if (numero > 0):
            i = 1;
            while numero > 0:
                i = numero * i;
                factorial = numero * i;
                numero -= 1;  
            return (factorial)
        elif (numero < 0):
            return (f"El número introducido {numero} no es postivo.")
        

numero = -4;
factorial_ = factorial(numero);
print(factorial_);


## Calculando el factorial de un número aplicando la recursividad
def factorial_recursiva (num):
    if (type(num) == int):
        if (num == 1):
            return 1;
        elif (num <= 0):
            return (f"El número introducido {num} no es positivo.")
        else:
            return num * factorial_recursiva(num - 1);
    else:
        return (f"El dato introducido no es un número entero.");


numero = 3;
factorial_calculado = factorial_recursiva(numero);
print (factorial_calculado);
# %%
