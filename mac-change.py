# Require Python 3 and Netmiko

# imports
from netmiko import Netmiko
from getpass import getpass
import string

# ask user for a vendor mac address HHHH.HH
userMAC = input("\nVendor MAC for the devices Ex. HHHH.HH: ")

# ask what VLAN the MAC should be in
userVLAN = input("VLAN would you like the devices to be in: ")

# get switch IP
userSwitch = input("IP of the switch the devices connect to: ")

# username and password
username = input("\nUsername: ")
password = getpass()

# log into switchIP
while True:
    try:
        myDevice = {
        'host': deviceName,
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

# run sh mac add | inc userMAC

# loop through list

# if trunk in output of sh int intMAC status

    # skip

# else change VLAN to userVLAN

    # shut
    # swi acc vlan userVLAN
    # no shut

# wr mem after

exit()
