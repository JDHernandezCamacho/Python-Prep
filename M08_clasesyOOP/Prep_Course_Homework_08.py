#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:
class Vehiculo:
    def __init__ (self, color, tipo, motor):
        self.color = color;
        self.tipo = tipo;
        self.motor = motor;



# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class Vehiculo:
    def __init__ (self, color, tipo, motor, matricula = "0000000"):
        self.color = color;
        self.tipo = tipo;
        self.motor = motor;
        self.velocidad = 0;
        self.dirección = 0;
        self.sentido = "este";
        self.__matricula = matricula;

    def capturar_matricula (self, matricula):
        if (self.__matricula == "0000000"):
            if (len(matricula) == 7 ):
                self.__matricula = matricula;
            else:
                print("El campo de matrícula es incorrecto.");
        else:
            print("El campo de matrícula contiene datos.");

    def frenar (self, velocidad):
        self.velocidad -= velocidad;
    
    def acelerar (self, velocidad):
        self.velocidad += velocidad;

    def doblar (self, direccion, sentido):
        self.dirección = direccion;
        self.sentido = sentido;




# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
nissan_sentra = Vehiculo("Plata", "Sedán", "1.8 con 4 cil");
vw_jetta = Vehiculo("Negro", "Sedán", "2.5 con 4 cil");
moto_yamaha = Vehiculo("Amarillo/Negro", "Moto Carreras", "450cc");
vw_vocho = Vehiculo("Blanco", "Sedán", "1.6 con 4 cil");
seat_ibiza = Vehiculo("Azúl eléctrico", "HatchBack", "1.2TB 4 cil");

nissan_sentra.capturar_matricula("AXY456H");
vw_jetta.capturar_matricula("TGX789P");
moto_yamaha.capturar_matricula("MPS890S");
vw_vocho.capturar_matricula("HKJ656X");
seat_ibiza.capturar_matricula("RUY787U");

nissan_sentra.acelerar(100);
nissan_sentra.doblar(30, "sureste");
nissan_sentra.frenar(20);
nissan_sentra.acelerar(40);

vw_jetta.acelerar(150);
vw_jetta.doblar(45, "noreste");

moto_yamaha.acelerar(0);
moto_yamaha.doblar(0, "norte");

vw_vocho.acelerar(65);
vw_vocho.doblar(70, "suroeste");

seat_ibiza.acelerar(230);
seat_ibiza.doblar(85, "sureste");




# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:
class Vehiculo:
    def __init__ (self, color, tipo, motor, matricula = "0000000"):
        self.color = color;
        self.tipo = tipo;
        self.motor = motor;
        self.velocidad = 0;
        self.dirección = 0;
        self.sentido = "este";
        self.__matricula = matricula;

    def capturar_matricula (self, matricula):
        if (self.__matricula == "0000000"):
            if (len(matricula) == 7 ):
                self.__matricula = matricula;
            else:
                print("El campo de matrícula es incorrecto.");
        else:
            print("El campo de matrícula contiene datos.");

    def frenar (self, velocidad):
        self.velocidad -= velocidad;
    
    def acelerar (self, velocidad):
        self.velocidad += velocidad;

    def doblar (self, direccion, sentido):
        self.dirección = direccion;
        self.sentido = sentido;
            
    def descripcion (self):
        print(f"El auto es de tipo: '{self.tipo}', color: '{self.color}', con placas de circulación '{self.__matricula}' y motor: '{self.motor}'");

    def estado (self):
        print(f"El auto tipo: '{self.tipo}', color: '{self.color}', con placas de circulación '{self.__matricula}', se dirige a una velocidad de {self.velocidad} km/h y {self.dirección}° hacia el {self.sentido}.");






# In[13]:
nissan_sentra.descripcion();
nissan_sentra.estado();

moto_yamaha.estado();





# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
class Herramientas:
    def __init__(self) -> None:
        pass

    def verificar_primo (self, numero, es_primo = True):
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
    


    def valor_modal (self, lista_recibida):
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
    



    def conversion_temperatura (self, valor, unidad_medida, medida_a_convertir):
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




    def operacion_factorial(self, num):
        if (type(num) == int):
            if (num == 1):
                return 1;
            elif (num <= 0):
                return (f"El número introducido {num} no es positivo.")
            else:
                return num * self.operacion_factorial(num - 1);
        else:
            return (f"El dato introducido no es un número entero.");





# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:
tools = Herramientas();

print (tools.verificar_primo(9));

lista = [0,1,2,3,4,2,3,2,5,2,6,7,8];
print(tools.valor_modal(lista));

temperatura = 58;
medida_origen = "Fahrenheit";
medida_destino = "Celcius";
print(tools.conversion_temperatura(temperatura, medida_origen, medida_destino));

numero = 9;
print (tools.operacion_factorial(numero));




# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:
class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros;

###################################################################################################################
    def verificar_primo (self):
        for numero in self.lista:
            es_primo = self.__verificar_primo(numero);
            if (es_primo):
                print (f"El número {numero} de la lista es primo.");
            else:
                print(f"El número {numero} de la lista no es primo.");

    def __verificar_primo (self, numero, es_primo = True):
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

###################################################################################################################
    def valor_modal (self):
        resultado =  self.__valor_modal(self.lista);
        print (resultado);


    def __valor_modal (self, lista_recibida):
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
    


###################################################################################################################
    def conversion_tempratura (self, unidad_origen, unidad_destino):
        for numero in self.lista:
            conversion = self.__conversion_temperatura(numero, unidad_origen, unidad_destino);
            print(conversion);


    def __conversion_temperatura (self, valor, unidad_medida, medida_a_convertir):
        if unidad_medida == "Celcius" and medida_a_convertir == "Fahrenheit":
            fahrenheit = (valor * 9/5) + 32;
            return (f"{valor}°C equivalen a {round(fahrenheit,1)}°F.");
        elif unidad_medida == "Fahrenheit" and medida_a_convertir == "Celcius":
            celcius = (valor - 32) * 5/9;
            return (f"{valor}°F equivalen a {round(celcius,1)}°C.");
        elif unidad_medida == "Celcius" and medida_a_convertir == "Kelvin":
            kelvin = valor + 273.15;
            return (f"{valor}°C equivalen a {round(kelvin,1)}°K.");
        elif unidad_medida == "Fahrenheit" and medida_a_convertir == "Kelvin":
            celcius = (valor - 32) * 5/9;
            kelvin = celcius + 273.15;
            return (f"{valor}°F equivalen a {round(kelvin,1)}°K.");
        elif unidad_medida == "Kelvin" and medida_a_convertir == "Celcius":
            celcius = valor - 273.15;
            return (f"{valor}°K equivalen a {round(celcius,1)}°C.");
        elif unidad_medida == "Kelvin" and medida_a_convertir == "Fahrenheit":
            celcius = valor - 273.15;
            fahrenheit = (celcius * 9/5) + 32;
            return (f"{valor}°K equivalen a {round(fahrenheit,1)}°F.");
        else:
            return (f"Favor de corroborar sus datos.")


###################################################################################################################
    def operacion_factorial (self):
        for numero in self.lista:
            resultado = self.__operacion_factorial(numero);
            print (f"El factorial de {numero} es {resultado}");

    def __operacion_factorial(self, num):
        if (type(num) == int):
            if (num == 1):
                return 1;
            elif (num <= 0):
                return (f"El número introducido {num} no es positivo.")
            else:
                return num * self.__operacion_factorial(num - 1);
        else:
            return (f"El dato introducido no es un número entero.");


lista_numeros = [1,2,2,3,1,2,4,5,2,6,8,1,3,11,17];
tool_box = Herramientas(lista_numeros);
tool_box.conversion_tempratura("Celcius", "Fahrenheit");

tool_box.operacion_factorial();

tool_box.valor_modal();

tool_box.verificar_primo();


# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:
import toolbox;

lista_a_evaluar = [2,5,3,6,7,8,3,0,17,12,11,13,5,2,4,3,8,9,3,1];
tool_importer = toolbox.Toolsclass(lista_a_evaluar);

tool_importer.conversion_tempratura("Kelvin", "Fahrenheit");

tool_importer.valor_modal();

tool_importer.operacion_factorial();

tool_importer.verificar_primo();


