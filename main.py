import os
from parameters import promptUser, summarizeParameters
from analysing import analyseFiles
from generating import generateInstaller

def main():
    # Récupération du répertoire de travail actuel
    cwd = os.getcwd()

    # Récupération des paramètres
    tried = False
    values = (None, None, None)
    while not tried or not summarizeParameters(*values):
        tried = True
        values = promptUser()

    # Analyse des fichiers
    files = analyseFiles(cwd)

    # Génération du fichier installer
    generateInstaller(*values, *files)

if __name__ == "__main__": main()
