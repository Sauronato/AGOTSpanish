import sys
import os

def procesar_archivo(archivo):
    extension = os.path.splitext(archivo)[1]
    if extension == ".yml":
        archivo_origen = archivo
        # Abrir ambos archivos en modo lectura
        with open(archivo_origen, 'r+') as readfile:
            # Leer las líneas de ambos archivos en dos listas
            lineas = readfile.readlines()
            # Iterar sobre las líneas de ambos archivos simultáneamente
            for i, linea in enumerate(lineas):
                # Buscar la cadena entre comillas dobles en la línea del archivo de destino
                mayus = linea.find(':0 "')
                if linea[mayus+4:mayus+5].islower():
                    print("Minuscula Cambiada en linea " + str(i) + "")
                    nueva_linea = linea[:mayus+4] + linea[mayus+4].upper() + linea[mayus+5:]
                    lineas[i] = nueva_linea
                mayus = linea.find(': "')
                if linea[mayus+3:mayus+4].islower():
                    print("Minuscula Cambiada en linea " + str(i) + "")
                    nueva_linea = linea[:mayus+4] + linea[mayus+4].upper() + linea[mayus+5:]
                    lineas[i] = nueva_linea

            # Rebobinar el puntero de lectura/escritura al inicio del archivo
            readfile.seek(0)
            # Escribir todas las líneas modificadas en el archivo
            readfile.writelines(lineas)
            # Truncar el archivo en caso de que la nueva versión sea más corta que la original
            readfile.truncate()



def recorrer_directorio(directorio):
    for elemento in os.listdir(directorio):
        ruta_elemento = os.path.join(directorio, elemento)
        if os.path.isfile(ruta_elemento):
            procesar_archivo(ruta_elemento)
        elif os.path.isdir(ruta_elemento):
            recorrer_directorio(ruta_elemento)


recorrer_directorio(sys.argv[1])
sys.exit(1)
