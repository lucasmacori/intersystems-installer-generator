import os

from untangle import parse

from .production import contains_classname


def analyse_files(directory, production):
    """
    Analyse les fichiers et renvoi les listes (ou un fichier) de ces derniers en fonction de leurs types
    :return Un tuple contenant dans l'ordre : Items de production (BO, BP, BS), Transforms, Routines, Classes
    """
    classes = get_classes(directory, production)  # Ajouter le CWD à la production
    routines = get_routines(directory)
    return classes[0], classes[1], routines, classes[2]


def find_files_from_extension(directory, extension):
    """
    Renvoi la liste des fichiers de l'extension donnée en argument, en cherchant recusivement dans le répertoire donné
    :param directory: Le répertoire dans lequel chercher les fichiers
    :param extension: L'extension des fichiers
    :return: Liste des fichiers
    """

    files_from_extensions = []

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            if name.endswith(extension):
                files_from_extensions.append(os.path.join(root, name))

    return files_from_extensions


def get_classes(directory, production):
    """
    Récupère la liste des classes et sépare les éléments de la production des transforms et des autres classes
    :param directory: Le répertoire dans lequel chercher les classes
    :param production: La production à consulter pour séparer les élements de la production
    :return: Un tuple contenant la liste des éléments de production, les transforms et la liste des autres classes
    """
    prod_items = []
    transforms = []
    classes = find_files_from_extension(directory, '.cls.xml')
    for current_class in classes:
        # Vérifie si la classe est un bo
        current_prod_item = contains_classname(production, current_class[len(directory) + 1:])
        if current_prod_item is not None:
            prod_items.append(current_prod_item)
            classes.remove(current_class)
        # Vérifie si la classe est un transform
        elif is_transform(current_class):
            transforms.append(current_class)
            classes.remove(current_class)

    return prod_items, transforms, classes


def get_routines(directory):
    """
    Récupère la liste des routines
    :return: La liste des routines du projet
    """
    routines = find_files_from_extension(directory, '.mac.xml')
    routines += find_files_from_extension(directory, '.inc.xml')
    return routines


def is_of_type(current_class, type):
    """
    Permet de savoir si une classe est du type donné
    :param current_class: La classe à analyser
    :param type: Le type de données
    :return: True si la classe est du type donné, sinon False
    """
    try:
        xml = parse(current_class).Export.Class.Super
        return str(xml.cdata) == type
    except AttributeError:
        return False


def is_transform(current_class):
    """
    Permet de savoir si une classe est un transform
    :param current_class: La classe à analyser
    :return: True si la classe est un transform, sinon False
    """
    return is_of_type(current_class, 'Ens.DataTransformDTL')
