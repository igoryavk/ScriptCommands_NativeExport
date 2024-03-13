# import scriptengine
# scriptengine.ScriptProject.export_native()
from os import system

PATH="C://parse//"
SAVER_PATH="C://Users//Igor//PycharmProjects//ObjectExplorer//main.py"

objects=[]
for item in projects.primary.get_children():
    if item.get_name()=="Device":
        objects.append(item)

#print(projects.primary.active_application.get_name())
projects.primary.export_native(objects=objects,destination=PATH,recursive=True,one_file_per_subtree=True)
system("python {0}".format(SAVER_PATH))