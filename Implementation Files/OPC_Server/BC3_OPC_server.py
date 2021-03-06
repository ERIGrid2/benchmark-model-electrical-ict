from opcua import Server
from opcua import ua
from opcua import Client
from random import randint
import datetime
import time

# start server
server = Server()
url = "opc.tcp://0.0.0.0:8899/freeopcua/server/"
server.set_endpoint(url)
# name for server 
name="OPC_UA_SERVER"
addspace = server.register_namespace(name)

# define variant = Integer ; variant2 = float
variant = None
variant = ua.Variant(0, ua.VariantType.Int16)
variant2 = None
variant2 = ua.Variant(0, ua.VariantType.Float)

node = server.get_objects_node()
# namespace
PF = node.add_object(addspace,"PF")
# Code for server
BB00_Elem01_S_Ctr =PF.add_variable(addspace,"BB00_Elem01_S_Ctr",variant)
BB00_Elem01_S_Ctr.set_writable(True)
BB00_Elem01_S_Res =PF.add_variable(addspace,"BB00_Elem01_S_Res",variant)
BB00_Elem01_S_Res.set_writable(True)
BB00_Tr01_00_01_P_Res =PF.add_variable(addspace,"BB00_Tr01_00_01_P_Res",variant2)
BB00_Tr01_00_01_P_Res.set_writable(True)
BB00_Tr01_00_01_Q_Res =PF.add_variable(addspace,"BB00_Tr01_00_01_Q_Res",variant2)
BB00_Tr01_00_01_Q_Res.set_writable(True)
BB00_Tr01_00_01_S_Ctr =PF.add_variable(addspace,"BB00_Tr01_00_01_S_Ctr",variant)
BB00_Tr01_00_01_S_Ctr.set_writable(True)
BB00_Tr01_00_01_S_Res =PF.add_variable(addspace,"BB00_Tr01_00_01_S_Res",variant)
BB00_Tr01_00_01_S_Res.set_writable(True)
BB00_Tr01_00_01_Tap =PF.add_variable(addspace,"BB00_Tr01_00_01_Tap",variant)
BB00_Tr01_00_01_Tap.set_writable(True)
BB00_Tr01_00_01_Tap_Ctr =PF.add_variable(addspace,"BB00_Tr01_00_01_Tap_Ctr",variant)
BB00_Tr01_00_01_Tap_Ctr.set_writable(True)
BB00_Tr01_00_01_Tap_Res =PF.add_variable(addspace,"BB00_Tr01_00_01_Tap_Res",variant)
BB00_Tr01_00_01_Tap_Res.set_writable(True)
BB00_Tr01_00_12_P_Res =PF.add_variable(addspace,"BB00_Tr01_00_12_P_Res",variant2)
BB00_Tr01_00_12_P_Res.set_writable(True)
BB00_Tr01_00_12_Q_Res =PF.add_variable(addspace,"BB00_Tr01_00_12_Q_Res",variant2)
BB00_Tr01_00_12_Q_Res.set_writable(True)
BB00_Tr01_00_12_Tap =PF.add_variable(addspace,"BB00_Tr01_00_12_Tap",variant)
BB00_Tr01_00_12_Tap.set_writable(True)
BB00_Tr01_00_12_Tap_Ctr =PF.add_variable(addspace,"BB00_Tr01_00_12_Tap_Ctr",variant)
BB00_Tr01_00_12_Tap_Ctr.set_writable(True)
BB00_Tr01_00_12_Tap_Res =PF.add_variable(addspace,"BB00_Tr01_00_12_Tap_Res",variant)
BB00_Tr01_00_12_Tap_Res.set_writable(True)
BB00_V_Res =PF.add_variable(addspace,"BB00_V_Res",variant2)
BB00_V_Res.set_writable(True)
BB01_Cap01_P_Res =PF.add_variable(addspace,"BB01_Cap01_P_Res",variant2)
BB01_Cap01_P_Res.set_writable(True)
BB01_Cap01_Q_Res =PF.add_variable(addspace,"BB01_Cap01_Q_Res",variant2)
BB01_Cap01_Q_Res.set_writable(True)
BB01_Cap01_S_Ctr =PF.add_variable(addspace,"BB01_Cap01_S_Ctr",variant)
BB01_Cap01_S_Ctr.set_writable(True)
BB01_Cap01_S_Res =PF.add_variable(addspace,"BB01_Cap01_S_Res",variant)
BB01_Cap01_S_Res.set_writable(True)
BB01_Cap01_Step_Ctr =PF.add_variable(addspace,"BB01_Cap01_Step_Ctr",variant)
BB01_Cap01_Step_Ctr.set_writable(True)
BB01_Cap01_Step_Res =PF.add_variable(addspace,"BB01_Cap01_Step_Res",variant)
BB01_Cap01_Step_Res.set_writable(True)
BB01_Ld01_S_Ctr =PF.add_variable(addspace,"BB01_Ld01_S_Ctr",variant)
BB01_Ld01_S_Ctr.set_writable(True)
BB01_Ld01_S_Res =PF.add_variable(addspace,"BB01_Ld01_S_Res",variant)
BB01_Ld01_S_Res.set_writable(True)
BB01_Ld02_S_Ctr =PF.add_variable(addspace,"BB01_Ld02_S_Ctr",variant)
BB01_Ld02_S_Ctr.set_writable(True)
BB01_Ld02_S_Res =PF.add_variable(addspace,"BB01_Ld02_S_Res",variant)
BB01_Ld02_S_Res.set_writable(True)
BB01_Ln01_01_02_P_Res =PF.add_variable(addspace,"BB01_Ln01_01_02_P_Res",variant2)
BB01_Ln01_01_02_P_Res.set_writable(True)
BB01_Ln01_01_02_Q_Res =PF.add_variable(addspace,"BB01_Ln01_01_02_Q_Res",variant2)
BB01_Ln01_01_02_Q_Res.set_writable(True)
BB01_Tr01_00_01_P_Res =PF.add_variable(addspace,"BB01_Tr01_00_01_P_Res",variant2)
BB01_Tr01_00_01_P_Res.set_writable(True)
BB01_Tr01_00_01_Q_Res =PF.add_variable(addspace,"BB01_Tr01_00_01_Q_Res",variant2)
BB01_Tr01_00_01_Q_Res.set_writable(True)
BB01_V_Res =PF.add_variable(addspace,"BB01_V_Res",variant2)
BB01_V_Res.set_writable(True)
BB02_Ln01_01_02_P_Res =PF.add_variable(addspace,"BB02_Ln01_01_02_P_Res",variant2)
BB02_Ln01_01_02_P_Res.set_writable(True)
BB02_Ln01_01_02_Q_Res =PF.add_variable(addspace,"BB02_Ln01_01_02_Q_Res",variant2)
BB02_Ln01_01_02_Q_Res.set_writable(True)
BB02_Ln01_02_03_P_Res =PF.add_variable(addspace,"BB02_Ln01_02_03_P_Res",variant2)
BB02_Ln01_02_03_P_Res.set_writable(True)
BB02_Ln01_02_03_Q_Res =PF.add_variable(addspace,"BB02_Ln01_02_03_Q_Res",variant2)
BB02_Ln01_02_03_Q_Res.set_writable(True)
BB02_V_Res =PF.add_variable(addspace,"BB02_V_Res",variant2)
BB02_V_Res.set_writable(True)
BB03_Ld01_S_Ctr =PF.add_variable(addspace,"BB03_Ld01_S_Ctr",variant)
BB03_Ld01_S_Ctr.set_writable(True)
BB03_Ld01_S_Res =PF.add_variable(addspace,"BB03_Ld01_S_Res",variant)
BB03_Ld01_S_Res.set_writable(True)
BB03_Ld02_S_Ctr =PF.add_variable(addspace,"BB03_Ld02_S_Ctr",variant)
BB03_Ld02_S_Ctr.set_writable(True)
BB03_Ld02_S_Res =PF.add_variable(addspace,"BB03_Ld02_S_Res",variant)
BB03_Ld02_S_Res.set_writable(True)
BB03_Ln01_02_03_P_Res =PF.add_variable(addspace,"BB03_Ln01_02_03_P_Res",variant2)
BB03_Ln01_02_03_P_Res.set_writable(True)
BB03_Ln01_02_03_Q_Res =PF.add_variable(addspace,"BB03_Ln01_02_03_Q_Res",variant2)
BB03_Ln01_02_03_Q_Res.set_writable(True)
BB03_Ln01_03_04_P_Res =PF.add_variable(addspace,"BB03_Ln01_03_04_P_Res",variant2)
BB03_Ln01_03_04_P_Res.set_writable(True)
BB03_Ln01_03_04_Q_Res =PF.add_variable(addspace,"BB03_Ln01_03_04_Q_Res",variant2)
BB03_Ln01_03_04_Q_Res.set_writable(True)
BB03_Ln01_03_08_P_Res =PF.add_variable(addspace,"BB03_Ln01_03_08_P_Res",variant2)
BB03_Ln01_03_08_P_Res.set_writable(True)
BB03_Ln01_03_08_Q_Res =PF.add_variable(addspace,"BB03_Ln01_03_08_Q_Res",variant2)
BB03_Ln01_03_08_Q_Res.set_writable(True)
BB03_PV01_P_Ctr =PF.add_variable(addspace,"BB03_PV01_P_Ctr",variant2)
BB03_PV01_P_Ctr.set_writable(True)
BB03_PV01_P_Res =PF.add_variable(addspace,"BB03_PV01_P_Res",variant2)
BB03_PV01_P_Res.set_writable(True)
BB03_PV01_Q_Ctr =PF.add_variable(addspace,"BB03_PV01_Q_Ctr",variant2)
BB03_PV01_Q_Ctr.set_writable(True)
BB03_PV01_Q_Res =PF.add_variable(addspace,"BB03_PV01_Q_Res",variant2)
BB03_PV01_Q_Res.set_writable(True)
BB03_PV01_S_Ctr =PF.add_variable(addspace,"BB03_PV01_S_Ctr",variant)
BB03_PV01_S_Ctr.set_writable(True)
BB03_PV01_S_Res =PF.add_variable(addspace,"BB03_PV01_S_Res",variant)
BB03_PV01_S_Res.set_writable(True)
BB03_V_Res =PF.add_variable(addspace,"BB03_V_Res",variant2)
BB03_V_Res.set_writable(True)
BB04_Ld01_S_Ctr =PF.add_variable(addspace,"BB04_Ld01_S_Ctr",variant)
BB04_Ld01_S_Ctr.set_writable(True)
BB04_Ld01_S_Res =PF.add_variable(addspace,"BB04_Ld01_S_Res",variant)
BB04_Ld01_S_Res.set_writable(True)
BB04_Ln01_03_04_P_Res =PF.add_variable(addspace,"BB04_Ln01_03_04_P_Res",variant2)
BB04_Ln01_03_04_P_Res.set_writable(True)
BB04_Ln01_03_04_Q_Res =PF.add_variable(addspace,"BB04_Ln01_03_04_Q_Res",variant2)
BB04_Ln01_03_04_Q_Res.set_writable(True)
BB04_Ln01_04_05_P_Res =PF.add_variable(addspace,"BB04_Ln01_04_05_P_Res",variant2)
BB04_Ln01_04_05_P_Res.set_writable(True)
BB04_Ln01_04_05_Q_Res =PF.add_variable(addspace,"BB04_Ln01_04_05_Q_Res",variant2)
BB04_Ln01_04_05_Q_Res.set_writable(True)
BB04_Ln01_04_11_P_Res =PF.add_variable(addspace,"BB04_Ln01_04_11_P_Res",variant2)
BB04_Ln01_04_11_P_Res.set_writable(True)
BB04_Ln01_04_11_Q_Res =PF.add_variable(addspace,"BB04_Ln01_04_11_Q_Res",variant2)
BB04_Ln01_04_11_Q_Res.set_writable(True)
BB04_Ln01_04_11_S_Ctr =PF.add_variable(addspace,"BB04_Ln01_04_11_S_Ctr",variant)
BB04_Ln01_04_11_S_Ctr.set_writable(True)
BB04_Ln01_04_11_S_Res =PF.add_variable(addspace,"BB04_Ln01_04_11_S_Res",variant)
BB04_Ln01_04_11_S_Res.set_writable(True)
BB04_PV01_P_Ctr =PF.add_variable(addspace,"BB04_PV01_P_Ctr",variant2)
BB04_PV01_P_Ctr.set_writable(True)
BB04_PV01_P_Res =PF.add_variable(addspace,"BB04_PV01_P_Res",variant2)
BB04_PV01_P_Res.set_writable(True)
BB04_PV01_Q_Ctr =PF.add_variable(addspace,"BB04_PV01_Q_Ctr",variant2)
BB04_PV01_Q_Ctr.set_writable(True)
BB04_PV01_Q_Res =PF.add_variable(addspace,"BB04_PV01_Q_Res",variant2)
BB04_PV01_Q_Res.set_writable(True)
BB04_PV01_S_Ctr =PF.add_variable(addspace,"BB04_PV01_S_Ctr",variant)
BB04_PV01_S_Ctr.set_writable(True)
BB04_PV01_S_Res =PF.add_variable(addspace,"BB04_PV01_S_Res",variant)
BB04_PV01_S_Res.set_writable(True)
BB04_V_Res =PF.add_variable(addspace,"BB04_V_Res",variant2)
BB04_V_Res.set_writable(True)
BB05_Ld01_S_Ctr =PF.add_variable(addspace,"BB05_Ld01_S_Ctr",variant)
BB05_Ld01_S_Ctr.set_writable(True)
BB05_Ld01_S_Res =PF.add_variable(addspace,"BB05_Ld01_S_Res",variant)
BB05_Ld01_S_Res.set_writable(True)
BB05_Ln01_04_05_P_Res =PF.add_variable(addspace,"BB05_Ln01_04_05_P_Res",variant2)
BB05_Ln01_04_05_P_Res.set_writable(True)
BB05_Ln01_04_05_Q_Res =PF.add_variable(addspace,"BB05_Ln01_04_05_Q_Res",variant2)
BB05_Ln01_04_05_Q_Res.set_writable(True)
BB05_Ln01_05_06_P_Res =PF.add_variable(addspace,"BB05_Ln01_05_06_P_Res",variant2)
BB05_Ln01_05_06_P_Res.set_writable(True)
BB05_Ln01_05_06_Q_Res =PF.add_variable(addspace,"BB05_Ln01_05_06_Q_Res",variant2)
BB05_Ln01_05_06_Q_Res.set_writable(True)
BB05_PV01_P_Ctr =PF.add_variable(addspace,"BB05_PV01_P_Ctr",variant2)
BB05_PV01_P_Ctr.set_writable(True)
BB05_PV01_P_Res =PF.add_variable(addspace,"BB05_PV01_P_Res",variant2)
BB05_PV01_P_Res.set_writable(True)
BB05_PV01_Q_Ctr =PF.add_variable(addspace,"BB05_PV01_Q_Ctr",variant2)
BB05_PV01_Q_Ctr.set_writable(True)
BB05_PV01_Q_Res =PF.add_variable(addspace,"BB05_PV01_Q_Res",variant2)
BB05_PV01_Q_Res.set_writable(True)
BB05_PV01_S_Ctr =PF.add_variable(addspace,"BB05_PV01_S_Ctr",variant)
BB05_PV01_S_Ctr.set_writable(True)
BB05_PV01_S_Res =PF.add_variable(addspace,"BB05_PV01_S_Res",variant)
BB05_PV01_S_Res.set_writable(True)
BB05_V_Res =PF.add_variable(addspace,"BB05_V_Res",variant2)
BB05_V_Res.set_writable(True)
BB06_Ld01_S_Ctr =PF.add_variable(addspace,"BB06_Ld01_S_Ctr",variant)
BB06_Ld01_S_Ctr.set_writable(True)
BB06_Ld01_S_Res =PF.add_variable(addspace,"BB06_Ld01_S_Res",variant)
BB06_Ld01_S_Res.set_writable(True)
BB06_Ln01_05_06_P_Res =PF.add_variable(addspace,"BB06_Ln01_05_06_P_Res",variant2)
BB06_Ln01_05_06_P_Res.set_writable(True)
BB06_Ln01_05_06_Q_Res =PF.add_variable(addspace,"BB06_Ln01_05_06_Q_Res",variant2)
BB06_Ln01_05_06_Q_Res.set_writable(True)
BB06_Ln01_06_07_P_Res =PF.add_variable(addspace,"BB06_Ln01_06_07_P_Res",variant2)
BB06_Ln01_06_07_P_Res.set_writable(True)
BB06_Ln01_06_07_Q_Res =PF.add_variable(addspace,"BB06_Ln01_06_07_Q_Res",variant2)
BB06_Ln01_06_07_Q_Res.set_writable(True)
BB06_PV01_P_Ctr =PF.add_variable(addspace,"BB06_PV01_P_Ctr",variant2)
BB06_PV01_P_Ctr.set_writable(True)
BB06_PV01_P_Res =PF.add_variable(addspace,"BB06_PV01_P_Res",variant2)
BB06_PV01_P_Res.set_writable(True)
BB06_PV01_Q_Ctr =PF.add_variable(addspace,"BB06_PV01_Q_Ctr",variant2)
BB06_PV01_Q_Ctr.set_writable(True)
BB06_PV01_Q_Res =PF.add_variable(addspace,"BB06_PV01_Q_Res",variant2)
BB06_PV01_Q_Res.set_writable(True)
BB06_PV01_S_Ctr =PF.add_variable(addspace,"BB06_PV01_S_Ctr",variant)
BB06_PV01_S_Ctr.set_writable(True)
BB06_PV01_S_Res =PF.add_variable(addspace,"BB06_PV01_S_Res",variant)
BB06_PV01_S_Res.set_writable(True)
BB06_V_Res =PF.add_variable(addspace,"BB06_V_Res",variant2)
BB06_V_Res.set_writable(True)
BB07_Ld01_S_Ctr =PF.add_variable(addspace,"BB07_Ld01_S_Ctr",variant)
BB07_Ld01_S_Ctr.set_writable(True)
BB07_Ld01_S_Res =PF.add_variable(addspace,"BB07_Ld01_S_Res",variant)
BB07_Ld01_S_Res.set_writable(True)
BB07_Ln01_06_07_P_Res =PF.add_variable(addspace,"BB07_Ln01_06_07_P_Res",variant2)
BB07_Ln01_06_07_P_Res.set_writable(True)
BB07_Ln01_06_07_Q_Res =PF.add_variable(addspace,"BB07_Ln01_06_07_Q_Res",variant2)
BB07_Ln01_06_07_Q_Res.set_writable(True)
BB07_Ln01_07_06_S_Ctr =PF.add_variable(addspace,"BB07_Ln01_07_06_S_Ctr",variant)
BB07_Ln01_07_06_S_Ctr.set_writable(True)
BB07_Ln01_07_06_S_Res =PF.add_variable(addspace,"BB07_Ln01_07_06_S_Res",variant)
BB07_Ln01_07_06_S_Res.set_writable(True)
BB07_Ln01_07_08_P_Res =PF.add_variable(addspace,"BB07_Ln01_07_08_P_Res",variant2)
BB07_Ln01_07_08_P_Res.set_writable(True)
BB07_Ln01_07_08_Q_Res =PF.add_variable(addspace,"BB07_Ln01_07_08_Q_Res",variant2)
BB07_Ln01_07_08_Q_Res.set_writable(True)
BB07_V_Res =PF.add_variable(addspace,"BB07_V_Res",variant2)
BB07_V_Res.set_writable(True)
BB07_WT01_P_Ctr =PF.add_variable(addspace,"BB07_WT01_P_Ctr",variant2)
BB07_WT01_P_Ctr.set_writable(True)
BB07_WT01_P_Res =PF.add_variable(addspace,"BB07_WT01_P_Res",variant2)
BB07_WT01_P_Res.set_writable(True)
BB07_WT01_Q_Ctr =PF.add_variable(addspace,"BB07_WT01_Q_Ctr",variant2)
BB07_WT01_Q_Ctr.set_writable(True)
BB07_WT01_Q_Res =PF.add_variable(addspace,"BB07_WT01_Q_Res",variant2)
BB07_WT01_Q_Res.set_writable(True)
BB07_WT01_S_Ctr =PF.add_variable(addspace,"BB07_WT01_S_Ctr",variant)
BB07_WT01_S_Ctr.set_writable(True)
BB07_WT01_S_Res =PF.add_variable(addspace,"BB07_WT01_S_Res",variant)
BB07_WT01_S_Res.set_writable(True)
BB08_Ld01_S_Ctr =PF.add_variable(addspace,"BB08_Ld01_S_Ctr",variant)
BB08_Ld01_S_Ctr.set_writable(True)
BB08_Ld01_S_Res =PF.add_variable(addspace,"BB08_Ld01_S_Res",variant)
BB08_Ld01_S_Res.set_writable(True)
BB08_Ln01_03_08_P_Res =PF.add_variable(addspace,"BB08_Ln01_03_08_P_Res",variant2)
BB08_Ln01_03_08_P_Res.set_writable(True)
BB08_Ln01_03_08_Q_Res =PF.add_variable(addspace,"BB08_Ln01_03_08_Q_Res",variant2)
BB08_Ln01_03_08_Q_Res.set_writable(True)
BB08_Ln01_07_08_P_Res =PF.add_variable(addspace,"BB08_Ln01_07_08_P_Res",variant2)
BB08_Ln01_07_08_P_Res.set_writable(True)
BB08_Ln01_07_08_Q_Res =PF.add_variable(addspace,"BB08_Ln01_07_08_Q_Res",variant2)
BB08_Ln01_07_08_Q_Res.set_writable(True)
BB08_Ln01_08_09_P_Res =PF.add_variable(addspace,"BB08_Ln01_08_09_P_Res",variant2)
BB08_Ln01_08_09_P_Res.set_writable(True)
BB08_Ln01_08_09_Q_Res =PF.add_variable(addspace,"BB08_Ln01_08_09_Q_Res",variant2)
BB08_Ln01_08_09_Q_Res.set_writable(True)
BB08_Ln01_08_14_P_Res =PF.add_variable(addspace,"BB08_Ln01_08_14_P_Res",variant2)
BB08_Ln01_08_14_P_Res.set_writable(True)
BB08_Ln01_08_14_Q_Res =PF.add_variable(addspace,"BB08_Ln01_08_14_Q_Res",variant2)
BB08_Ln01_08_14_Q_Res.set_writable(True)
BB08_PV01_P_Ctr =PF.add_variable(addspace,"BB08_PV01_P_Ctr",variant2)
BB08_PV01_P_Ctr.set_writable(True)
BB08_PV01_P_Res =PF.add_variable(addspace,"BB08_PV01_P_Res",variant2)
BB08_PV01_P_Res.set_writable(True)
BB08_PV01_Q_Ctr =PF.add_variable(addspace,"BB08_PV01_Q_Ctr",variant2)
BB08_PV01_Q_Ctr.set_writable(True)
BB08_PV01_Q_Res =PF.add_variable(addspace,"BB08_PV01_Q_Res",variant2)
BB08_PV01_Q_Res.set_writable(True)
BB08_PV01_S_Ctr =PF.add_variable(addspace,"BB08_PV01_S_Ctr",variant)
BB08_PV01_S_Ctr.set_writable(True)
BB08_PV01_S_Res =PF.add_variable(addspace,"BB08_PV01_S_Res",variant)
BB08_PV01_S_Res.set_writable(True)
BB08_V_Res =PF.add_variable(addspace,"BB08_V_Res",variant2)
BB08_V_Res.set_writable(True)
BB09_Ld01_S_Ctr =PF.add_variable(addspace,"BB09_Ld01_S_Ctr",variant)
BB09_Ld01_S_Ctr.set_writable(True)
BB09_Ld01_S_Res =PF.add_variable(addspace,"BB09_Ld01_S_Res",variant)
BB09_Ld01_S_Res.set_writable(True)
BB09_Ln01_08_09_P_Res =PF.add_variable(addspace,"BB09_Ln01_08_09_P_Res",variant2)
BB09_Ln01_08_09_P_Res.set_writable(True)
BB09_Ln01_08_09_Q_Res =PF.add_variable(addspace,"BB09_Ln01_08_09_Q_Res",variant2)
BB09_Ln01_08_09_Q_Res.set_writable(True)
BB09_Ln01_09_10_P_Res =PF.add_variable(addspace,"BB09_Ln01_09_10_P_Res",variant2)
BB09_Ln01_09_10_P_Res.set_writable(True)
BB09_Ln01_09_10_Q_Res =PF.add_variable(addspace,"BB09_Ln01_09_10_Q_Res",variant2)
BB09_Ln01_09_10_Q_Res.set_writable(True)
BB09_PV01_P_Ctr =PF.add_variable(addspace,"BB09_PV01_P_Ctr",variant2)
BB09_PV01_P_Ctr.set_writable(True)
BB09_PV01_P_Res =PF.add_variable(addspace,"BB09_PV01_P_Res",variant2)
BB09_PV01_P_Res.set_writable(True)
BB09_PV01_Q_Ctr =PF.add_variable(addspace,"BB09_PV01_Q_Ctr",variant2)
BB09_PV01_Q_Ctr.set_writable(True)
BB09_PV01_Q_Res =PF.add_variable(addspace,"BB09_PV01_Q_Res",variant2)
BB09_PV01_Q_Res.set_writable(True)
BB09_PV01_S_Ctr =PF.add_variable(addspace,"BB09_PV01_S_Ctr",variant)
BB09_PV01_S_Ctr.set_writable(True)
BB09_PV01_S_Res =PF.add_variable(addspace,"BB09_PV01_S_Res",variant)
BB09_PV01_S_Res.set_writable(True)
BB09_V_Res =PF.add_variable(addspace,"BB09_V_Res",variant2)
BB09_V_Res.set_writable(True)
BB10_Ld01_S_Ctr =PF.add_variable(addspace,"BB10_Ld01_S_Ctr",variant)
BB10_Ld01_S_Ctr.set_writable(True)
BB10_Ld01_S_Res =PF.add_variable(addspace,"BB10_Ld01_S_Res",variant)
BB10_Ld01_S_Res.set_writable(True)
BB10_Ld02_S_Ctr =PF.add_variable(addspace,"BB10_Ld02_S_Ctr",variant)
BB10_Ld02_S_Ctr.set_writable(True)
BB10_Ld02_S_Res =PF.add_variable(addspace,"BB10_Ld02_S_Res",variant)
BB10_Ld02_S_Res.set_writable(True)
BB10_Ln01_09_10_P_Res =PF.add_variable(addspace,"BB10_Ln01_09_10_P_Res",variant2)
BB10_Ln01_09_10_P_Res.set_writable(True)
BB10_Ln01_09_10_Q_Res =PF.add_variable(addspace,"BB10_Ln01_09_10_Q_Res",variant2)
BB10_Ln01_09_10_Q_Res.set_writable(True)
BB10_Ln01_10_11_P_Res =PF.add_variable(addspace,"BB10_Ln01_10_11_P_Res",variant2)
BB10_Ln01_10_11_P_Res.set_writable(True)
BB10_Ln01_10_11_Q_Res =PF.add_variable(addspace,"BB10_Ln01_10_11_Q_Res",variant2)
BB10_Ln01_10_11_Q_Res.set_writable(True)
BB10_PV01_P_Ctr =PF.add_variable(addspace,"BB10_PV01_P_Ctr",variant2)
BB10_PV01_P_Ctr.set_writable(True)
BB10_PV01_P_Res =PF.add_variable(addspace,"BB10_PV01_P_Res",variant2)
BB10_PV01_P_Res.set_writable(True)
BB10_PV01_Q_Ctr =PF.add_variable(addspace,"BB10_PV01_Q_Ctr",variant2)
BB10_PV01_Q_Ctr.set_writable(True)
BB10_PV01_Q_Res =PF.add_variable(addspace,"BB10_PV01_Q_Res",variant2)
BB10_PV01_Q_Res.set_writable(True)
BB10_PV01_S_Ctr =PF.add_variable(addspace,"BB10_PV01_S_Ctr",variant)
BB10_PV01_S_Ctr.set_writable(True)
BB10_PV01_S_Res =PF.add_variable(addspace,"BB10_PV01_S_Res",variant)
BB10_PV01_S_Res.set_writable(True)
BB10_V_Res =PF.add_variable(addspace,"BB10_V_Res",variant2)
BB10_V_Res.set_writable(True)
BB11_Ld01_S_Ctr =PF.add_variable(addspace,"BB11_Ld01_S_Ctr",variant)
BB11_Ld01_S_Ctr.set_writable(True)
BB11_Ld01_S_Res =PF.add_variable(addspace,"BB11_Ld01_S_Res",variant)
BB11_Ld01_S_Res.set_writable(True)
BB11_Ln01_04_11_P_Res =PF.add_variable(addspace,"BB11_Ln01_04_11_P_Res",variant2)
BB11_Ln01_04_11_P_Res.set_writable(True)
BB11_Ln01_04_11_Q_Res =PF.add_variable(addspace,"BB11_Ln01_04_11_Q_Res",variant2)
BB11_Ln01_04_11_Q_Res.set_writable(True)
BB11_Ln01_10_11_P_Res =PF.add_variable(addspace,"BB11_Ln01_10_11_P_Res",variant2)
BB11_Ln01_10_11_P_Res.set_writable(True)
BB11_Ln01_10_11_Q_Res =PF.add_variable(addspace,"BB11_Ln01_10_11_Q_Res",variant2)
BB11_Ln01_10_11_Q_Res.set_writable(True)
BB11_PV01_P_Ctr =PF.add_variable(addspace,"BB11_PV01_P_Ctr",variant2)
BB11_PV01_P_Ctr.set_writable(True)
BB11_PV01_P_Res =PF.add_variable(addspace,"BB11_PV01_P_Res",variant2)
BB11_PV01_P_Res.set_writable(True)
BB11_PV01_Q_Ctr =PF.add_variable(addspace,"BB11_PV01_Q_Ctr",variant2)
BB11_PV01_Q_Ctr.set_writable(True)
BB11_PV01_Q_Res =PF.add_variable(addspace,"BB11_PV01_Q_Res",variant2)
BB11_PV01_Q_Res.set_writable(True)
BB11_PV01_S_Ctr =PF.add_variable(addspace,"BB11_PV01_S_Ctr",variant)
BB11_PV01_S_Ctr.set_writable(True)
BB11_PV01_S_Res =PF.add_variable(addspace,"BB11_PV01_S_Res",variant)
BB11_PV01_S_Res.set_writable(True)
BB11_V_Res =PF.add_variable(addspace,"BB11_V_Res",variant2)
BB11_V_Res.set_writable(True)
BB12_Ld01_S_Ctr =PF.add_variable(addspace,"BB12_Ld01_S_Ctr",variant)
BB12_Ld01_S_Ctr.set_writable(True)
BB12_Ld01_S_Res =PF.add_variable(addspace,"BB12_Ld01_S_Res",variant)
BB12_Ld01_S_Res.set_writable(True)
BB12_Ld02_S_Ctr =PF.add_variable(addspace,"BB12_Ld02_S_Ctr",variant)
BB12_Ld02_S_Ctr.set_writable(True)
BB12_Ld02_S_Res =PF.add_variable(addspace,"BB12_Ld02_S_Res",variant)
BB12_Ld02_S_Res.set_writable(True)
BB12_Ln01_12_13_P_Res =PF.add_variable(addspace,"BB12_Ln01_12_13_P_Res",variant2)
BB12_Ln01_12_13_P_Res.set_writable(True)
BB12_Ln01_12_13_Q_Res =PF.add_variable(addspace,"BB12_Ln01_12_13_Q_Res",variant2)
BB12_Ln01_12_13_Q_Res.set_writable(True)
BB12_Tr01_00_12_P_Res =PF.add_variable(addspace,"BB12_Tr01_00_12_P_Res",variant2)
BB12_Tr01_00_12_P_Res.set_writable(True)
BB12_Tr01_00_12_Q_Res =PF.add_variable(addspace,"BB12_Tr01_00_12_Q_Res",variant2)
BB12_Tr01_00_12_Q_Res.set_writable(True)
BB12_V_Res =PF.add_variable(addspace,"BB12_V_Res",variant2)
BB12_V_Res.set_writable(True)
BB13_Ld01_S_Ctr =PF.add_variable(addspace,"BB13_Ld01_S_Ctr",variant)
BB13_Ld01_S_Ctr.set_writable(True)
BB13_Ld01_S_Res =PF.add_variable(addspace,"BB13_Ld01_S_Res",variant)
BB13_Ld01_S_Res.set_writable(True)
BB13_Ln01_12_13_P_Res =PF.add_variable(addspace,"BB13_Ln01_12_13_P_Res",variant2)
BB13_Ln01_12_13_P_Res.set_writable(True)
BB13_Ln01_12_13_Q_Res =PF.add_variable(addspace,"BB13_Ln01_12_13_Q_Res",variant2)
BB13_Ln01_12_13_Q_Res.set_writable(True)
BB13_Ln01_13_14_P_Res =PF.add_variable(addspace,"BB13_Ln01_13_14_P_Res",variant2)
BB13_Ln01_13_14_P_Res.set_writable(True)
BB13_Ln01_13_14_Q_Res =PF.add_variable(addspace,"BB13_Ln01_13_14_Q_Res",variant2)
BB13_Ln01_13_14_Q_Res.set_writable(True)
BB13_V_Res =PF.add_variable(addspace,"BB13_V_Res",variant2)
BB13_V_Res.set_writable(True)
BB14_Ld01_S_Ctr =PF.add_variable(addspace,"BB14_Ld01_S_Ctr",variant)
BB14_Ld01_S_Ctr.set_writable(True)
BB14_Ld01_S_Res =PF.add_variable(addspace,"BB14_Ld01_S_Res",variant)
BB14_Ld01_S_Res.set_writable(True)
BB14_Ld02_S_Ctr =PF.add_variable(addspace,"BB14_Ld02_S_Ctr",variant)
BB14_Ld02_S_Ctr.set_writable(True)
BB14_Ld02_S_Res =PF.add_variable(addspace,"BB14_Ld02_S_Res",variant)
BB14_Ld02_S_Res.set_writable(True)
BB14_Ln01_08_14_P_Res =PF.add_variable(addspace,"BB14_Ln01_08_14_P_Res",variant2)
BB14_Ln01_08_14_P_Res.set_writable(True)
BB14_Ln01_08_14_Q_Res =PF.add_variable(addspace,"BB14_Ln01_08_14_Q_Res",variant2)
BB14_Ln01_08_14_Q_Res.set_writable(True)
BB14_Ln01_13_14_P_Res =PF.add_variable(addspace,"BB14_Ln01_13_14_P_Res",variant2)
BB14_Ln01_13_14_P_Res.set_writable(True)
BB14_Ln01_13_14_Q_Res =PF.add_variable(addspace,"BB14_Ln01_13_14_Q_Res",variant2)
BB14_Ln01_13_14_Q_Res.set_writable(True)
BB14_V_Res =PF.add_variable(addspace,"BB14_V_Res",variant2)
BB14_V_Res.set_writable(True)
GEN_PSUM_RES =PF.add_variable(addspace,"GEN_PSUM_RES",variant2)
GEN_PSUM_RES.set_writable(True)
MODE =PF.add_variable(addspace,"MODE",variant)
MODE.set_writable(True)
# start the server
server.start()
print("Server started at {}".format(url))
