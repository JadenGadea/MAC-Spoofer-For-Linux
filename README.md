## MAC-Address Spoofer script for Linux.
This script allows you to change the MAC address of a network interface on a Linux system.

#### Requirements

Python3:
- optparse.
- re modules.

Usage.
To use this script, open a terminal and navigate to the directory where the spoofer.py script is located.

Then, run the script with the following command: **(It has to be run with sudo privlieges)**.
sudo python3 spoofer.py -i <interface> -m <new_mac_address>
Replace <interface> with the name of the network interface you want to change the MAC address for, and <new_mac_address> with the new MAC address you want to set.

For example, to change the MAC address of the eth0 interface to 00:11:22:33:44:55, you would run the following command:

python spoofer.py -i eth0 -m 00:11:22:33:44:55
The script will first check if the specified interface and MAC address are valid. If they are, it will change the MAC address of the specified interface and print the new MAC address. If there is an error, it will print an error message.

#### Options:

**The following options are available:**

**-i, --interface: The name of the network interface to change the MAC address for.**
**-m, --mac: The new MAC address to set for the specified network interface.**

### Example

Here is an example of how to use the script to change the MAC address of the eth0 interface to 00:11:22:33:44:55:

	sudo python3 spoofer.py -i eth0 -m 00:11:22:33:44:55
