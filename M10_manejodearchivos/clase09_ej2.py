import sys;

def cargar_datos (fecha_y_hora, temperatura, humedad, lluvia):
    import os;
    linea = (f"{fecha_y_hora},{temperatura},{humedad},{lluvia}");
    print(f"    Los datos a registrar son: {linea}");
    user_response = input("    ¿Está de acuerdo con la línea de datos? y/n, y = si; n = no:");
    if (user_response == "y" or user_response == "Y"):
        logs_weater = open("clase09_ej2.csv", "a");
        logs_weater.write(linea + "\n");
        print("    El proceso ha finalizado, se han guardado los datos en el archivo.");
        logs_weater.close();
        print (" ");
    if (user_response == "n" or user_response == "N"):
        print("    El proceso ha finalizado, no se han guardado datos.");



if (sys.argv[1] == "Activar"):
    import datetime;
    fyh_actual = datetime.datetime.now();
    fyh_actual_stmp = datetime.datetime.timestamp(fyh_actual);
    print(f"    La fecha y hora actual es: {fyh_actual}");
    temperatura = float(input("    Introduce el valor de la temperatura en grados celcius con un número."));
    humedad = float(input("    Introduce el valor de la humedad relativa actual con un número."));
    hay_lluvia = input("    Actualmente, ¿Está lloviendo? y/n, y = True; n = False:");
    
    if (hay_lluvia == "y" or hay_lluvia == "Y"):
        lluvia = True;
        cargar_datos(fyh_actual_stmp, temperatura, humedad, lluvia);
    elif (hay_lluvia == "n" or hay_lluvia == "N"):
        lluvia = False;
        cargar_datos(fyh_actual_stmp, temperatura, humedad, lluvia);
    else :
        print ("    El valor introducido no es aceptado. Se ha finalizado el proceso. No se guardaron datos.");
        print (" ");

else:
    print ("    Para ejecutar el script, mande un sólo parámetro con la palabra 'Activar'");
    print ("    Ejemplo: py clase09_ej2.py Activar");
    print ("    El proceso se ha finalizado. No se guardaron datos.");
    print (" ");


