import os

from analysing import analyse_files
from generating import generate_installer
from parameters import prompt_user, summarize_parameters


def main():
    # Récupération du répertoire de travail actuel
    cwd = os.getcwd()

    # Récupération des paramètres
    tried = False
    values = (None, None, None)
    while not tried or not summarize_parameters(*values):
        tried = True
        values = prompt_user()

    # Analyse des fichiers
    files = analyse_files(cwd)

    # Génération du fichier installer
    generate_installer(*values, *files)


if __name__ == "__main__": main()
