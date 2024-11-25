import os
import filecmp
from pathlib import Path

SUFIX_1 = 'l_english.yml'
SUFIX_2 = 'l_spanish.yml'

dir1_list = []
dir2_list = []

def get_files(dir1, dir2):
    for root, dirs, files in os.walk(dir1):
        for file in files:
                dir1_list.append(os.path.join(root, file))
    for root, dirs, files in os.walk(dir2):
        for file in files:
                dir2_list.append(os.path.join(root, file))
    print("Archivos en dir1: "+str(len(dir1_list)))
    print("Archivos en dir2: "+str(len(dir2_list)))


def debug_files():
        for file in dir1_list:
            print(file)
        for file in dir2_list:
            print(file)


def ordenar_comparar():
    # Crear listas temporales para los nombres de archivos sin sufijos
    dir1_nombres = [os.path.basename(i).replace(
        SUFIX_1, '') for i in dir1_list]
    dir2_nombres = [os.path.basename(i).replace(
        SUFIX_2, '') for i in dir2_list]

    # Ordenar ambas listas
    dir1_nombres.sort()
    dir2_nombres.sort()
    print("Archivos en dir1: "+str(len(dir1_list)))
    print("Archivos en dir2: "+str(len(dir2_list)))
    print("Archivos en dir1: "+str(len(dir1_nombres)))
    print("Archivos en dir2: "+str(len(dir2_nombres)))

    # Listas para almacenar archivos repetidos y no repetidos
    archivos_repetidos = []
    archivos_no_repetidos = []

    # Comparar ambos directorios y guardar los archivos que se repiten
    for archivo in dir1_nombres:
        if archivo in dir2_nombres:
            archivos_repetidos.append(archivo)
        else:
            archivos_no_repetidos.append(archivo)

    # Agregar los archivos de dir2 que no están en dir1
    for archivo in dir1_nombres:
        if archivo not in dir2_nombres:
            archivos_no_repetidos.append(archivo)

    return archivos_repetidos, archivos_no_repetidos


def main():
  get_files("C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\1158310\\2962333032\\localization\\replace",
            "C: \\Users\\david\\OneDrive\\Documentos\\Paradox Interactive\\Crusader Kings III\\AGOTSpanish - copia\\C\\localization\\replace")
  archivos_repetidos, archivos_no_repetidos = ordenar_comparar()
  print("Archivos repetidos: "+str(len(archivos_repetidos)))
  print("Archivos no repetidos: "+str(len(archivos_no_repetidos)))



if __name__ == "__main__":
    main()