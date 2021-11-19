# Instructions to automatically create all OPC tags 
 - Download the PowerFactory file - `ERIGRID2-JRA1-BM3.pfd`.
 - Run the three python scripts: `CreateBreakerMeas`, `CreateGenLoadMeas`, and `CreateLinesMeas` in the `OPC_Python` folder through the PowerFactory python interpreter.

# Work Flow
1. Create the OPC tags
2. Start the OPC UA server (refer to *OPC_server folder*)
3. Connect to the OPC UA server from PowerFactoryby creating an OPC link object
4. Enter the address of the OPC UA server (refer to *OPC_server folder*)
5. Calculate inital conditions and run an RMS simulation for 10s
6. You should now see the measurement values being updated on any other connected OPC client
