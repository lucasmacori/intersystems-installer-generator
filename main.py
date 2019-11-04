import os

# Récupération du répertoire de travail actuel
cwd = os.getcwd()

def promptUser():
    """
    Demande à l'utilisateur les paramètres d'entrée du programme
    :return Un tuple contenant dans l'ordre: le dossier de l'installer, le nom de l'installer, le chemin et le nom du fichier de production
    """
    defaultDirectory = 'ANCV/Installer'
    defaultFilename = 'Installer.cls.xml'

    # Demande des informations de l'installer à l'utilisateur
    directory = str(input('Dossier de génération du fichier (' + defaultDirectory + '): '))
    filename = str(input('Nom du fichier (' + defaultFilename + '): '))
    productionFilename = str(input('Chemin vers la production: '))

    # Applications des valeurs par défaut si non renseignée
    if directory.strip() == '': directory = defaultDirectory
    if filename.strip() == '': filename = defaultFilename

    return (directory, filename, productionFilename)

def summarizeParameters(directory, filename, productionFilename):
    """
    Récapitule à l'utilisateur les paramètres d'entrée et demande une validation
    :return True si l'utilisateur a validé les paramètres, sinon False
    """
    print('\nParamètres')
    print('------------------------------')
    print('Fichier généré:', directory + filename)
    print('Fichier de production:', productionFilename)

    response = ''
    while response != 'O' and response != 'N':
        response = str(input('Est-ce-correct ? [O/N]: '))
        response.strip().upper()

    return response == 'O'

def main():
    tried = False
    values = (None, None, None)
    while not tried or not summarizeParameters(*values):
        tried = True
        values = promptUser()

if __name__ == "__main__": main()