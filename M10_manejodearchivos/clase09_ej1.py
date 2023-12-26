import sys;

if (len(sys.argv) == 4):
    print(f"La persona que utiliza este script, se llama {sys.argv[1]}, tiene {sys.argv[2]} años de edad y es {sys.argv[3]}.");
else:
    print("     Los datos introducidos no corresponden a los (3) parámetros, solicitados: tu nombre, tu edad, tu profesión.");
    print("     Introduce los datos como el ejemplo: Juan-Diego, 22, Programador.");
    print("     Recuerda que cada parámetro se separa por un espacio.");
