from untangle import parse

from classes.item import Item


def open_production(production_filename):
    """
    Ouvre le fichier de production et lit son contenu
    :return: Un objet Python représentant le contenu de la production
    """
    try:
        f = open(production_filename)
        production = f.read()
        xml = str(parse(production).Export.Class.XData.Data)
        xml = xml[xml.index('<Production'):]
        production_xml = parse(xml).Production
        f.close()
        return production_xml
    except FileNotFoundError:
        return None


def contains_classname(production, class_name):
    """
    Indique si la classe envoyée en argument existe dans la production
    :param production: La production à inspecter
    :param class_name: Le nom de la classe à rechercher
    :return: L'item de la production si existant, sinon None
    """
    class_name = class_name.replace('\\', '/').replace('/', '.').replace('.cls.xml', '')
    for item in production.Item:
        if item['ClassName'] == class_name:
            return Item(item['Name'], item['ClassName'])
    return None
