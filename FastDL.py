# Made by Lord-Giganticus. Please do not remake this without crediting me :)

import os

def extractfiles():
    for dir in os.walk(os.getcwd()):
        os.chdir(dir[0])
        for file in os.listdir(os.getcwd()):
            if file.endswith('.bz2'):
                os.system('cmd /c 7z.exe x *.bz2')
                os.system('cmd /c del /f *.bz2')
def extractmaps():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.bz2'):
            os.system('cmd /c 7z.exe x *.bz2')
            os.system('cmd /c del /f *.bz2')

steam_normal = input("Is Steam installed in the defalt location?\nIf so enter 1.\nIf not enter 2.\n")
if steam_normal == "1":
    if os.path.isdir("C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2") == False:
        input("The Team Fortess 2 folder doesn't exist! Press enter to exit.")
        exit()
    os.chdir("C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2")
    os.chdir("tf")
    tf = os.getcwd()
    os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/FastDL.zip -o FastDL.zip')
    os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
    os.system('cmd /c unzip *zip')
    os.system('cmd /c del /f *.zip')
    os.system('cmd /c del /f *.exe')
    extractfiles()
    maps = input("Do you wish to also download the maps from the server?\n If so, enter 1.\nIf not, enter 2.\n")
    if maps == "1":
        os.chdir(tf)
        if os.path.isdir('maps') == False:
            os.mkdir('maps')
        os.chdir('maps')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/af_tf2_party_a12.bsp.bz2 -o af_tf2_party_a12.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/boss_jevil_v4a.bsp.bz2 -o boss_jevil_v4a.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/cp_clash_royale.bsp.bz2 -o cp_clash_royale.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/koth_tf2craps_b1.bsp.bz2 -o koth_tf2craps_b1.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/my_world_x9b.bsp.bz2 -o my_world_x9b.bsp.bz2')
        extractmaps()
        input("Complete. Press enter to exit.")
        exit()
    elif maps == "2":
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
    tf = os.getcwd()
    os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/FastDL.zip -o FastDL.zip')
    os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
    os.system('cmd /c unzip *zip')
    os.system('cmd /c del /f *.zip')
    os.system('cmd /c del /f *.exe')
    extractfiles()
    maps = input("Do you wish to also download the maps from the server?\n If so, enter 1.\nIf not, enter 2.\n")
    if maps == "1":
        os.chdir(tf)
        if os.path.isdir('maps') == False:
            os.mkdir('maps')
        os.chdir('maps')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/af_tf2_party_a12.bsp.bz2 -o af_tf2_party_a12.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/boss_jevil_v4a.bsp.bz2 -o boss_jevil_v4a.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/cp_clash_royale.bsp.bz2 -o cp_clash_royale.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/koth_tf2craps_b1.bsp.bz2 -o koth_tf2craps_b1.bsp.bz2')
        os.system('cmd /c curl https://chaos-crew.000webhostapp.com/FastDL/tf/maps/my_world_x9b.bsp.bz2 -o my_world_x9b.bsp.bz2')
        extractmaps()
        input("Complete. Press enter to exit.")
        exit()
    elif maps == "2":
        input("Complete. Press enter to exit.")
        exit()
else:
    input("Whoops! You chose wrong! Press enter to exit.")
    exit()