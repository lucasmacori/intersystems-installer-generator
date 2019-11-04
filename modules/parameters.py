import os

cwd = os.getcwd()


def prompt_user():
    """
    Demande à l'utilisateur les paramètres d'entrée du programme
    :return Un tuple contenant dans l'ordre: le dossier de l'installer, le nom de l'installer, le chemin et le nom du fichier de production
    """
    default_directory = 'ANCV/Installer'
    default_filename = 'Installer.cls.xml'

    # Demande des informations de l'installer à l'utilisateur
    directory = str(input('Dossier de génération du fichier (' + default_directory + '): '))
    filename = str(input('Nom du fichier (' + default_filename + '): '))
    production_filename = str(input('Chemin vers la production: '))

    # Applications des valeurs par défaut si non renseignée
    if directory.strip() == '':
        directory = default_directory
    if filename.strip() == '':
        filename = default_filename

    return directory, filename, production_filename


def summarize_parameters(directory, filename, production_filename):
    """
    Récapitule à l'utilisateur les paramètres d'entrée et demande une validation
    :return True si l'utilisateur a validé les paramètres, sinon False
    """
    print('\nParamètres')
    print('------------------------------')
    print('Fichier généré:', directory + filename)
    print('Fichier de production:', cwd + '/' + production_filename)

    response = ''
    while response != 'O' and response != 'N':
        response = str(input('Est-ce-correct ? [O/N]: '))
        response = response.strip().upper()

    return response == 'O'
