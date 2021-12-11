from os import getcwd, mkdir
from os.path import isdir, join
from shutil import rmtree

def reiniciar_hugo():
    packsPath = join(getcwd(), 'hugo','content', 'Packs') # C:\...\proyecto-devops\content\Packs
    if isdir(packsPath):
        rmtree(packsPath) # Borra la carpeta recursivamente
    if not isdir(packsPath):
        mkdir(packsPath) # En caso de no existir la crea
reiniciar_hugo()