class Toolsclass:
    def __init__(self, lista_numeros):
        if (type(lista_numeros) != list):
            self.lista = [];
            raise ValueError ("La variable no es una lista de números, se ha creado una lista vacia.");
        else :
            self.lista = lista_numeros;

###################################################################################################################
    def verificar_primo (self):
        lista_result_primos = [];
        for numero in self.lista:
            es_primo = self.__verificar_primo(numero);
            if (es_primo):
                # print (f"El número {numero} de la lista es primo.");
                lista_result_primos.append(es_primo);
            else:
                lista_result_primos.append(es_primo);
                #  print(f"El número {numero} de la lista no es primo.");
        return lista_result_primos;

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
        moda, repetida =  self.__valor_modal(self.lista);
        resultado = [moda, repetida];
        return (resultado);


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

        return (lista_moda[0], lista_moda[1]);
    


###################################################################################################################
    def conversion_tempratura (self, unidad_origen, unidad_destino):
        conversion_list = [];
        unidades_soportadas = ["Celcius", "Fahrenheit", "Kelvin"];
        if (unidad_origen == "Celcius" or unidad_origen == "Kelvin" or unidad_origen == "Fahrenheit"):
            if (unidad_destino == "Celcius" or unidad_destino == "Kelvin" or unidad_destino == "Fahrenheit"):
                for numero in self.lista:
                    conversion_list.append (self.__conversion_temperatura(numero, unidad_origen, unidad_destino));
                    #print(conversion_list);
            else:
                print (f"La unidades de medida soportadas son: {unidades_soportadas}.");
                return conversion_list;
        else:
            print (f"La unidades de medida soportadas son: {unidades_soportadas}.");
            return conversion_list;
        
        return (conversion_list);


    def __conversion_temperatura (self, valor, unidad_medida, medida_a_convertir):
        if unidad_medida == "Celcius" and medida_a_convertir == "Fahrenheit":
            fahrenheit = (valor * 9/5) + 32;
            return (round(fahrenheit,1));
        elif unidad_medida == "Fahrenheit" and medida_a_convertir == "Celcius":
            celcius = (valor - 32) * 5/9;
            return (round(celcius,1));
        elif unidad_medida == "Celcius" and medida_a_convertir == "Kelvin":
            kelvin = valor + 273.15;
            return (round(kelvin,1));
        elif unidad_medida == "Fahrenheit" and medida_a_convertir == "Kelvin":
            celcius = (valor - 32) * 5/9;
            kelvin = celcius + 273.15;
            return (round(kelvin,1));
        elif unidad_medida == "Kelvin" and medida_a_convertir == "Celcius":
            celcius = valor - 273.15;
            return (round(celcius,1));
        elif unidad_medida == "Kelvin" and medida_a_convertir == "Fahrenheit":
            celcius = valor - 273.15;
            fahrenheit = (celcius * 9/5) + 32;
            return (round(fahrenheit,1));
        else:
            return (f"Error. Favor de corroborar sus datos.")


###################################################################################################################
    def operacion_factorial (self):
        resultado = [];
        for numero in self.lista:
            if (numero >= 0):
                resultado.append(self.__operacion_factorial(numero));
                # print (f"El factorial de {numero} es {resultado}");
            else:
                resultado = [];
                raise ValueError ("La lista contiene números negativos, se ha creado una lista vacia.");
        
        return resultado;

    def __operacion_factorial(self, num):
        if (type(num) == int):
            if (num == 1):
                return 1;
            elif (num <= 0):
                return (f"El número introducido {num} no es positivo.")
            else:
                return num * self.__operacion_factorial(num - 1);
        else:
            raise ValueError ("La variable no es una lista de números, se ha creado una lista vacia.");
            return (f"El dato introducido no es un número entero.");