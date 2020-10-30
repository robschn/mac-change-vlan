# mac-change-vlan
This script will allow you to change VLANs based on the vendor MAC address.

### Installation
1. `git clone https://github.com/robschn/mac-change-vlan/`
2. `cd mac-change-vlan/`
3. `python -m venv ven`
4. `source ven/bin/activate
5. `pip install requirements.txt`

### Usage
1. Run `python mac-change.py`.
2. Enter the vendor MAC of the devices. This is the first 6 of a MAC address and must be in Cisco format, HHHH.HH.
3. Enter what VLAN you want all the devices to be in.
4. Enter the IP of the switch the devices are connected to.
```
Vendor MAC for the devices. Must be HHHH.HH format: 0000.0c
VLAN would you like the devices to be in: 10
IP of the switch the devices connect to: 192.168.1.1
```
5. Once you log in, the script will run a search for devices containing the vendor MAC. If a device is already in the VLAN you specified, it will not be added to the list.
```
Username: cisco
Password: 

Logging in now...
Searching for MAC address...

Found these interfaces:
['Gi1/0/3', 'Gi1/0/5', 'Gi1/0/9', 'Gi1/0/11']
```
If the interface is a trunk:

```
Gi1/0/3
Skipping, port is a trunk.
```

Else:
```
Gi1/0/5
Modifying, please wait...
Done!

Gi1/0/9
Modifying, please wait...
Done!

Gi1/0/11
Modifying, please wait...
Done!
```
6. After the interfaces are done, it will write memory and exit:
```
Writing to memory, please wait...

VLAN changes completed! Exiting program...
```

### Requirements
- Python 3

- Netmiko
