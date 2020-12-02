# Made by Lord-Giganticus. Please do not remake this without crediting me :)

import os

steam_normal = input("Is Steam installed in the defalt location?\nIf so enter 1.\nIf not enter 2.\n")
if steam_normal == "1":
    if os.path.isdir("C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2") == False:
        input("The Team Fortess 2 folder doesn't exist! Press enter to exit.")
        exit()
    os.chdir("C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2")
    os.chdir("tf")
    os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/FastDL.zip -o FastDL.zip')
    os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
    os.system('cmd /c unzip *zip')
    os.system('cmd /c del /f *.zip')
    os.system('cmd /c del /f *.exe')
    for dir in os.walk(os.getcwd()):
        os.chdir(dir[0])
        for file in os.listdir(os.getcwd()):
                if file.endswith('.bz2'):
                    os.system('cmd /c 7z.exe x *.bz2')
                    os.system('cmd /c del /f *.bz2')
    input("Complete. Press enter to exit.")
    exit()
elif steam_normal =="2":
    location = input("Enter the location of your custom Steam install (NOT TF2).\n")
    os.chdir(location)
    if os.path.isdir("steamapps") == False:
        input("The steamapps folder doesn't exist! Press enter to exit.")
        exit()
    os.chdir("steamapps\common")
    if os.path.isdir("Team Fortress 2") == False:
        input("The Team Fortress 2 folder dosen't exist! Press enter to exit.")
        exit()
    os.chdir("Team Fortress 2")
    os.chdir("tf")
    os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/FastDL.zip -o FastDL.zip')
    os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
    os.system('cmd /c unzip *zip')
    os.system('cmd /c del /f *.zip')
    os.system('cmd /c del /f *.exe')
    for dir in os.walk(os.getcwd()):
        os.chdir(dir[0])
        for file in os.listdir(os.getcwd()):
            if file.endswith('.bz2'):
                if file.endswith('.bz2'):
                    os.system('cmd /c 7z.exe x *.bz2')
                    os.system('cmd /c del /f *.bz2')
    input("Complete. Press enter to exit.")
    exit()
else:
    input("Whoops! You chose wrong! Press enter to exit.")
    exit()