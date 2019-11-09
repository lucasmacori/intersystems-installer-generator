import os


def generate_installer(directory, filename, productionFilename, production_items, transforms, routines, classes):
    """
    Génère le fichier d'installer en fonction des fichiers reçus en argument et le sauvegarde
    :return Un booléan informant du bon fonctionnement de la génération de l'installer
    """
    # TODO: Générer l'installer avec les fichiers envoyés en argument et le sauvegarder

    print(production_items, transforms, routines, classes)

    # Récupération du répertoire de travail actuel
    cwd = os.getcwd()
    return True
