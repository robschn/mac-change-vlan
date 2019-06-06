# Requires Python 3 and Netmiko

# imports
from netmiko import Netmiko
from getpass import getpass

# ask for MAC in HHHH.HH format
userMAC = input("\nVendor MAC for the devices. Must be HHHH.HH format: ")

# ask for VLAN
userVLAN = input("VLAN would you like the devices to be in: ")

# ask for switch IP
userSwitch = input("IP of the switch the devices connect to: ")

# log into switchIP
while True:
    try:
        username = input("\nUsername: ")
        password = getpass()
        myDevice = {
        'host': userSwitch,
        'username': username,
        'password': password,
        'device_type': 'cisco_ios',
        }
        print("\nLogging in now...")
        net_connect = Netmiko(**myDevice)
        net_connect.enable()
        break
    except:
        print("Login failed. Please try again.")
        continue

print("Searching for MAC addresses...")

# run sh mac add | inc userMAC
showMAC = net_connect.send_command("show mac add | inc "+userMAC)

# grabs interfaces
interfaces = [];
for line in showMAC.splitlines():
        #only grabs interfaces that are not equal to userVLAN
        if line[2:4] != userVLAN:
            interfaces.append(line[38:47].strip())

print("\nFound these interfaces:")
print(interfaces)

# starts a loop to iterate
for intf in interfaces:
        output = net_connect.send_command("sh int "+intf+" status");

        # skip if trunk
        if "trunk" in output:
            print("\n" +intf)
            print("Skipping, port is a trunk.")

        else:
            print("\n" +intf)
            print("Modifying, please wait...")

            # issue commands
            config_commands = [
            'int '+intf,
            'shut',
            'swi acc vlan '+userVLAN,
            'no shut']

            net_connect.send_config_set(config_commands)
            print("Done!")

# write mem
print("\nWriting to memory, please wait...")
net_connect.send_command('write mem')

# exit program
print("\nVLAN changes completed! Exiting program...")
exit()
