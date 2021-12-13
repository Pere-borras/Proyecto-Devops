from os import getcwd, mkdir
from os.path import isdir, join
from shutil import rmtree

def reiniciar_hugo(carpeta):

    if carpeta == '':
        carpeta = 'Packs'

    packsPath = join(getcwd(), 'hugo','content', carpeta) # C:\...\proyecto-devops\content\ carpeta a elegir o Packs
    if isdir(packsPath):
        rmtree(packsPath) # Borra la carpeta recursivamente
    if not isdir(packsPath):
        mkdir(packsPath) # En caso de no existir la crea
    
    return carpeta