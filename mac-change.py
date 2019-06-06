# Require Python 3 and Netmiko

# imports
from netmiko import Netmiko
from getpass import getpass
import string

# ask user for a vendor mac address HHHH.HH
userMAC = input ("\nVendor MAC for the devices Ex. HHHH.HH: ")

# ask what VLAN the MAC should be in
userVLAN = input ("VLAN would you like the devices to be in: ")

# get switch IP
userSwitch = input ("IP of the switch the devices connect to: ")

# username and password
username = input ("\nUsername: ")
password = getpass()

# log into switchIP
while True:
    try:
        myDevice = {
        'host': userSwitch,
        'username': username,
        'password': password,
        'device_type': 'cisco_ios',
        }
        print ('\nLogging in now...')
        net_connect = Netmiko(**myDevice)
        net_connect.enable()
        break
    except:
        print ('\nLogin failed. Please try again.')
        continue

print ("Searching for MAC address...")

# run sh mac add | inc userMAC
showMAC = net_connect.send_command("show mac add | inc "+userMAC)

# grabs interfaces
interfaces = [];
for line in showMAC.splitlines():
    interfaces.append(line[38:47].strip())

print ("\nFound:")
print (interfaces)

for intf in interfaces:
    output = net_connect.send_command("sh int "+intf+" status");

    if "trunk" in output:
        print("\n" +intf)
        print ("Skipping, port is a trunk.")

    elif userVLAN in output:
        print("\n" +intf)
        print ("Skipping, VLAN is already set.")

    else:
        print("\n" +intf)
        print("Modifying, please wait...")
        config_commands = ['int '+intf, 'shut', 'swi acc vlan '+userVLAN, 'no shut']
        net_connect.send_config_set(config_commands)
        print("Done!")

net_connect.send_command('write mem')

print ("\nVLAN changes completed! Exiting Program...")

exit()
