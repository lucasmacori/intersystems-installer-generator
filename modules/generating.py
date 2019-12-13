import os


def generate_installer(directory, filename, productionFilename, production_items, transforms, routines, classes):
	"""
	Génère le fichier d'installer en fonction des fichiers reçus en argument et le sauvegarde
	:return Un booléan informant du bon fonctionnement de la génération de l'installer
	"""
	xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + \
		  "<Export generator=\"Cache\" version=\"25\">\n" + \
		  "<Class name=\"" + directory + "." + filename.replace('.cls.xml', '').replace('/', '.') + "\">\n" + \
		  "<Description></Description>\n" + \
		  "<TimeCreated></TimeCreated>\n" + \
		  "\n" + \
		  "<Method name=\"Exec\">\n" + \
		  "<ClassMethod>1</ClassMethod>\n" + \
		  "<FormalSpec>path:%String</FormalSpec>\n" + \
		  "<ReturnType>%Status</ReturnType>\n" + \
		  "<Implementation><![CDATA[\n" + \
		  "	Set tProjectName = \"\"\n" + \
		  "	Set tProductionName = \"" + productionFilename + "\"\n" + \
		  "	Set tProductionClassIncluded = 1\n" + \
		  "	Set tExportFilename = path_\"\"\n" + \
		  "	Set tComments = \"\"\n" + \
		  "\n" + \
		  "	// Items de la production\n"

	# Items de la production
	for production_item in production_items:
		xml += "	Set tContentsList(\"" + production_item.class_name + "\") = \"\"\n"
	
	# Classes
	xml += "\n	// Classes\n"
	for current_class in classes:
		xml += "	Set tContentsList(\"" + current_class + "\") = \"\"\n"

	# Transforms
	xml += "\n	// Transforms\n"
	for transform in transforms:
		xml += "	Set tContentsList(\"" + transform + "\") = \"\"\n"

	# Routines
	xml += "\n	// Routines\n"
	for routine in routines:
		xml += "	Set tContentsList(\"" + routine + "\") = \"\"\n"

	# Export des items de la production
	index = 0
	xml += "\n	// Export des items de la production\n"
	for production_item in production_items:
		index += 1
		xml += "	Set tItemName = \"" + production_item.name + "\"\n"
		xml += "	Set:(tItemName '[ \"||\") tItemName = tProductionName_\"||\"_tItemName\n"
		xml += "	Set tItem = ##class(Ens.Config.Production).OpenItemByConfigName(tItemName)\n"
		xml += "	If $IsObject(tItem) Set tSC = ##class(Ens.Deployment.Utils).CreatePTDFromItem(.tItem,.tPTDNam" + str(index) + ")\n"
		xml += "	Set tContentsList(tPTDNam" + str(index) + "_\".PTD\")=\"\"\n\n"

	# Package de déploiement
	xml += "	// Export des items de la production\n"
	xml += "	Set tSC = ##class(Ens.Deployment.Utils).CreateExportPackageFromProjectList(\n"
	xml += "		tProjectName,.tContentsList,tExportFilename,tProductionName,tComments,tProductionClassIncluded)\n"

	# Suppression des text documents
	index = 0
	xml += "\n	// Suppression des text documents\n"
	for production_item in production_items:
		index += 1
		xml += "	Do ##class(Ens.Util.ProjectTextDocument).Delete(tPTDNam" + str(index) + "_\".PTD\")\n"

	xml += "\n 	Quit tSC\n"

	xml += "]]></Implementation>\n"
	xml += "</Method>\n"
	xml += "</Class>\n"
	xml += "</Export>\n"

	f = open(directory + "/" + filename, "w")
	f.write(xml)
	f.close()
