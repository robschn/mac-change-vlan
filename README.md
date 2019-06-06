## mac-change-vlan
This script will allow you to change VLANs based on the vendor MAC address.

### Usage
1. Enter the vendor MAC of the devices. This is the first 6 of a MAC address. Must use Cisco format, HHHH.HH.
2. Enter what VLAN you want all the devices to be in.
3. Enter the IP of the switch the devices are connected to.
```
Vendor MAC for the devices. Must be HHHH.HH format: 0000.0c
VLAN would you like the devices to be in: 10
IP of the switch the devices connect to: 192.168.1.1
```
The script will have you log in, then search for the devices with that MAC:
```
Username: cisco
Password: 

Logging in now...
Searching for MAC address...

Found these interfaces:
['Gi1/0/3', 'Gi1/0/5', 'Gi1/0/9', 'Gi1/0/11', 'Gi1/0/12', 'Gi1/0/20']
```

It will then check against two conditons.

Interface is a trunk:
```
Gi1/0/3
Skipping, port is a trunk.
```
Device is already in your specified VLAN:
```
Gi1/0/5
Skipping, VLAN is already set.
```
If none of those conditions match, it will change the VLAN:
```
Gi1/0/9
Modifying, please wait...
Done!
```
After the interfaces are done, it will write memory and exit:
```
Writing to memory, please wait...

VLAN changes completed! Exiting Program...
```

### Requirements
- Python 3

- Netmiko
