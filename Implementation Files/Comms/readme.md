# Dependencies
- The emulation of communication networks requires [Mininet](https://github.com/mininet/mininet/wiki/Documentation) along with `Python 2.7`
- It has been tested on an Ubuntu VM, but should work within a *cygwin* environment as well
# Mininet communication network
To start the mininet network, the following commands must be executed: 
```
> sudo mn -c
```
```
> python2 mininet_network.py
```
From within the mininet CLI, the execute the following commands:
```
> xterm terminal 1
```
```
> xterm terminal 2
```
# Running the voltage control algorithm
- Check that the OPC UA server is up and running, and that you have connected PowerFactory to it. Refer to their associated folders in the same repository.
- From *Mininet* terminal 2, execute the following command:
    ```
    > python client_cvc.py
    ```
- From *Mininet* terminal 1, execute the following command:
    ```
    > python opc_merging_unit.py
    ```