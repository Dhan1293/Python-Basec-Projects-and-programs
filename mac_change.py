
import subprocess       #module used to enter commands in terminal using python programming
import optparse         #module used to add further commands while executing program in terminal
import re               #module used to search specif item from the string!!!

'''
functions below are required to change mac address
and to add further commands while executing program
in terminal with help and additional commands!!!
'''

def opt_par():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Enter your mac_changing interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter your new mac address")

    (option, argument) = parser.parse_args()

    if not option.interface:
        parser.error("\n[+] No interface selected use --help or -h for more options")
        # print("[+] eth0 is taken as Default interface")

    elif not option.new_mac:
        parser.error("\n[+] No new mac given use --help or -h for more options")
        # print("[+] default new mac address is taken as 00:11:22:33:44:55")

    return option



def change_mac(interface, mac):
    # reading and storing detected mac address and printing it as old mac!!!

    ifconfig_old = subprocess.check_output(["ifconfig", interface])
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_old)

    # if mac address detected and found it will be changed according to users wish

    if mac_search:
        # printing old mac and chaning details

        print("\n[+] Old mac = " + mac_search.group(0))
        print("[+] Changing mac of " + interface + " to " + mac)

        # commands for mac changing!!!

        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", mac])
        subprocess.call(["ifconfig", interface, "up"])

        # changed mac succesfully!!!

        print("[+] Mac address changed suucessfully!!!")

        # reading and storing detected mac address and printing it as new mac!!!

        ifconfig_new = subprocess.check_output(["ifconfig", interface])
        new_mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_new)
        print("[+] New mac = " + new_mac_search.group(0))

    else:
        print("[+] Could'nt find mac address for interface " + interface)
        print("[-] OR could'nt change mac address of interface " + interface)



'''

Calling required function below
 1) called for executing additional commands
    while running program from terminal with 
    additional help if required!
 2) called for chaning mac address according 
    to the users will!!!
    
'''
# 1st function to be called!!!
option = opt_par()
# 2nd function to be called!!!
change_mac(option.interface, option.new_mac)
