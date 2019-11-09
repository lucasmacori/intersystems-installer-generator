import os

from modules.analysing import analyse_files
from modules.generating import generate_installer
from modules.parameters import prompt_user, summarize_parameters
from modules.production import open_production


def main():
    # Récupération du répertoire de travail actuel
    cwd = os.getcwd()
    cwd = 'C:/Users/Lucas/Desktop/Temp/SVCREMB'  # Enlever une fois l'application packagée

    # Récupération des paramètres
    tried = False
    production = None
    values = None, None, None
    while not tried or not summarize_parameters(*values):
        tried = True
        values = prompt_user()
        # Récupération du contenu de la production
        production = open_production(cwd + '/' + values[2])
        if production is None:
            print('Le fichier de production n\'existe pas, veuillez recommencer')
            tried = False

    # Analyse des fichiers
    # files = analyse_files(cwd, production)
    files = analyse_files(cwd, production)

    # Génération du fichier installer
    generate_installer(*values, *files)


if __name__ == "__main__":
    main()
