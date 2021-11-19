# Dependencies
- The emulation of communication networks requires [Mininet](https://github.com/mininet/mininet/wiki/Documentation)
- `Python 2.7`
- It has been tested on a virtual machine running Ubuntu 18.04

# Mininet communication network
To start the mininet network, the following commands must be executed: 
```
> sudo mn -c
```
This command clears any previous sessions and related data
```
> sudo python2 mininet_network.py
```
This command starts the mininet network. Upon a successfull execution, the mininet Command Line Interface (CLI) should open up
From within the mininet CLI, execute the following commands:
```
mininet> xterm s06m1
```
```
mininet> xterm s06m2
```
This should open two xterminal (xterm) windows
# Running the co-simulation
- Check that the OPC UA server is up and running, and that you have connected PowerFactory to it. Refer to their associated folders in the same repository for instructions

- From *Mininet* terminal *s06m1*, execute the following command:
    ```
    > python3 opc_read_volts.py
    ```
- From *Mininet* terminal *s06m2*, execute the following command:
    ```
    > python3 cvc_volts.py
    ```