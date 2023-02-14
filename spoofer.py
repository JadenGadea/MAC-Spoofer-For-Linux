import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address)
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, user --helpfor more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, user --help for more info")
    return options

    
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + + new_ mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.callable(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_adress_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_adress_search_result:
        return (mac_adress_search_result.group(0))
    else:
        print("[-] Could not read MAC adress.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

# change_mac(options.interface, options.new_mac)




