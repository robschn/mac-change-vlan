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

print ("Found:")
print (interfaces)

for intf in interfaces:
    print("Modifying:");
    print(intf);

    output = net_connect.send_command("sh int " +intf+ " status");

    if "trunk" in output:
        print ("trunk")

    else:
        print ("not trunk")


# if trunk in output of sh int intMAC status

    # skip

# else change VLAN to userVLAN

    # shut
    # swi acc vlan userVLAN
    # no shut

# wr mem after

exit()
