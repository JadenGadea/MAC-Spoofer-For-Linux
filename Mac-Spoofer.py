# Path: spoofer.py
import subprocess
import optparse
import re

# where is there error in the code?


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, user --helpfor more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, user --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    mac_adress_search_result = re.search("([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", ifconfig_result.stdout)

    if mac_adress_search_result:
        return mac_adress_search_result.group(0)
    else:
        print("[-] Could not read MAC adress.")

options = get_arguments()

current_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

if current_mac == options.new_mac:
    print("[+] MAC adress was successfully changed to " + current_mac)
else:
    print("[-] MAC adress did not get changed.")
    




