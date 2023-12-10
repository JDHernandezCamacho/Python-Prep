#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:
import sys;
# print(sys.path);
sys.path.append (r"C:/Users/ingdi/SoyHenry/SH-DS/Python-Prep/M08_classesyOOP/toolbox.py");

import toolbox as t;
var_a_evaluar = "Hola soy Diego";
tool = t.Toolsclass(var_a_evaluar);

# Al parecer aquí no marco ningún error, por ser una variable iterable, sin embargo, sigue existiendo un error
# la letra "o" no es un número
tool.valor_modal();

#Para poder llevar a cabo la función es necesario que se envien datos numéricos, de tipo int o float.
tool.conversion_tempratura("Fahrenheit","Celcius");

#Dentro de la función se encuentra un if que evalua si el dato es un dato de tipo número, en caso de que no,
#envia el mensaje de no es un número entero para calcular factorial
#por esa razón devuelve ese resultado.
tool.operacion_factorial();

# Mismo caso que la función conversión de temperaturas, es necesario un valor númerico de tipo int.
tool.verificar_primo();

import toolbox as t;
var_a_evaluar = "Hola, soy una variable string.";

tool = t.Toolsclass(var_a_evaluar);

tool.verificar_primo();

#Mandando la variable de tipo lista que si es aceptada para la lectura del código.
import toolbox as t;
var_a_evaluar = [1,6,3,4,2,6,1,5,4,8,1,0,5];
tool = t.Toolsclass (var_a_evaluar);
tool.valor_modal();



# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:
import importlib;
importlib.reload(t);

var_a_evaluar = [1,6,3,4,2,6,1,5,4,8,1,0,5];
tool = t.Toolsclass (var_a_evaluar);

print(f"La lista {var_a_evaluar} convertida es: {tool.conversion_tempratura("Celcius", "Kelvin")}");




# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:
import importlib;
importlib.reload(t);

import toolbox as t;
var_a_evaluar = [1,6,3,4,2,6,1,5,4,8,1,0,5];
tool = t.Toolsclass (var_a_evaluar);

import unittest;

class PruebaDeErrores (unittest.TestCase):
    def test_crear_objeto_error (self):
        param = "Hola soy Diego";
        self.assertRaises(ValueError, t.Toolsclass, param);

    def test_crear_objeto_ok (self):
        param = [1,7,6,5,3,6];
        tool = t.Toolsclass(param);
        self.assertEqual(tool.lista, param);

    def test_moda (self):
        lista = [1,7,6,5,3,6];
        tool = t.Toolsclass(lista);
        moda = tool.valor_modal();
        moda_esperada = [6, 2];
        self.assertEqual(moda, moda_esperada);

unittest.main(argv=[''], verbosity=2, exit=False);



# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:
tool = t.Toolsclass("Diego");

importlib;
importlib.reload(t);

import toolbox as t;
lista = [-5,1,3,-4];
tool = t.Toolsclass(lista);
factorial = tool.operacion_factorial();
print(factorial);



# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:
import toolbox as t;

lista = [1,2,3,4,2,3,3];
tool = t.Toolsclass(lista);
primos = tool.verificar_primo();
print(primos);

importlib;
importlib.reload(t);

import unittest;

class PruebaDeErroresNumerosPrimos (unittest.TestCase):
    def test_verificar_num_primos (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        no_primos = tool.verificar_primo();
        result_ok = [False, True, True, False, True, True, True];
        self.assertEqual(no_primos, result_ok);


unittest.main(argv=[''], verbosity=2, exit=False);



# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:
import unittest;

class PruebaDeErroresConversion(unittest.TestCase):
    def test_conversion_celcius_to_fahrenheit (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        a_grados_fhr = tool.conversion_tempratura("Celcius", "Fahrenheit");
        result_ok = [33.8, 35.6, 37.4, 39.2, 35.6, 37.4, 37.4];
        self.assertEqual(a_grados_fhr, result_ok);

    def test_conversion_celcius_to_kelvin (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        a_grados_klvn = tool.conversion_tempratura("Celcius", "Kelvin");
        result_ok = [274.1, 275.1, 276.1, 277.1, 275.1, 276.1, 276.1];
        self.assertEqual(a_grados_klvn, result_ok);

    def test_conversion_fahrenheit_to_celcius (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        a_grados_clcs = tool.conversion_tempratura("Fahrenheit", "Celcius");
        result_ok = [-17.2, -16.7, -16.1, -15.6, -16.7, -16.1, -16.1];
        self.assertEqual(a_grados_clcs, result_ok);

    def test_conversion_fahrenheit_to_kelvin (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        a_grados_klvn = tool.conversion_tempratura("Fahrenheit", "Kelvin");
        result_ok = [255.9, 256.5, 257.0, 257.6, 256.5, 257.0, 257.0];
        self.assertEqual(a_grados_klvn, result_ok);

    def test_conversion_kelvin_to_celcius (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        a_grados_clcs = tool.conversion_tempratura("Kelvin", "Celcius");
        result_ok = [-272.1, -271.1, -270.1, -269.1, -271.1, -270.1, -270.1];
        self.assertEqual(a_grados_clcs, result_ok);

    def test_conversion_kelvin_to_fahrenheit (self):
        lista = [1,2,3,4,2,3,3];
        tool = t.Toolsclass(lista);
        a_grados_fhr = tool.conversion_tempratura("Kelvin", "Fahrenheit");
        result_ok = [-457.9, -456.1, -454.3, -452.5, -456.1, -454.3, -454.3];
        self.assertEqual(a_grados_fhr, result_ok);

importlib.reload(t);

unittest.main(argv=[''], verbosity=2, exit=False);




# 8) Agregar casos de pruebas para el método factorial()

# In[20]:

importlib.reload(t);

lista = [3,5,12,15];
tool = t.Toolsclass(lista);

print(tool.operacion_factorial());

class PruebaDeErroresFactorial (unittest.TestCase):
    def test_factorial (self):
        lista = [3,5,12,15];
        tool = t.Toolsclass(lista);
        resultado_factorial = tool.operacion_factorial();
        result_ok = [6, 120, 479001600, 1307674368000];
        self.assertEqual(resultado_factorial, result_ok);



unittest.main(argv=[''], verbosity=2, exit=False);
