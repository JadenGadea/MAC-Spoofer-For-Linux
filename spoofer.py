import subprocess
import random

def change_mac_address(interface):
    # Check if user has root privileges
    if subprocess.call(["id", "-u"]) != 0:
        return 1, "Insufficient privileges. Must be run as root."
    
    # Check if specified wireless adapter exists
    if interface not in subprocess.getoutput("ip link").split():
        return 2, "Wireless adapter not found."
    
    # Generate a random Mac-address
    new_mac_address = ":".join(["{:02x}".format(random.randint(0, 255)) for _ in range(6)])
    
    # Change the Mac-address
    try:
        subprocess.check_output(["ip", "link", "set", "dev", interface, "address", new_mac_address])
    except subprocess.CalledProcessError:
        return 3, "Failed to change Mac-address. Check wireless adapter name and try again."
    
    # Verify that the Mac-address has been changed
    current_mac_address = subprocess.getoutput("ip link show {} | awk '/ether/ {{print $2}}'".format(interface))
    if current_mac_address.strip() != new_mac_address:
        return 4, "Failed to change Mac-address. Try again."
    
    return 0, "Successfully changed Mac-address to {}".format(new_mac_address)
