from pandas import read_json
from numpy import nan
import pandapower as pp
import numpy as np
import math
from network_v02 import *

np.set_printoptions(suppress=True)

def RemoveNull(a):
    return a[~np.isnan(a).any(axis=1)]

def ColumnSorted(a):
    e =a[np.lexsort(([1,1,1]*a[:,[2,0,1]]).T)]
    return e

def ColumnSorted_second(a):
    e =a[np.lexsort(([1,1,1]*a[:,[2,1,0]]).T)]
    return e

def Voltage_Controller (Vbusbars, cap_in_service, current_stepcap, TapTrcurrent):
    Performance =[]
    net = create_cigre_network_mv(with_der="pv_wind",tap_position = TapTrcurrent, step_cap = current_stepcap)
    Prated = net.sgen["p_mw"]
    out_Voltages = np.empty(len(Vbusbars), dtype = np.float64)
    out_Voltages.fill(np.nan)
    out_QTrafo = 0.
    Tap_init = 0
    Tap_final = 0
    voltage_dev = 0.03
    powerfactor = 0.95
    TapTmax = 3
    TapTmin = -3
    TapCmax = 3
    
    if TapTrcurrent == TapTmax:
        Tap_init = TapTrcurrent - 2
        Tap_final = TapTrcurrent
    else:
        if TapTrcurrent == TapTmin:
            Tap_init = TapTrcurrent
            Tap_final = TapTrcurrent + 2
        else:
            Tap_init = TapTrcurrent - 2
            Tap_final = TapTrcurrent + 2
    if cap_in_service == True:    
        for ttransf in range(Tap_init, Tap_final+1):
            for tcap in range(TapCmax+1):
                for Qindex in range(-1,2):
                    Qgen = Qindex * math.sin(math.acos(powerfactor)) * Prated
                    net.trafo["tap_pos"]= ttransf
                    net.load["q_mvar"][0]= -3*tcap
                    # net = pn.create_cigre_network_mv(with_der="pv_wind",tap_position = ttransf, step_cap = tcap)
                    net.sgen["q_mvar"] = Qgen
                    # print("start loadflow")
                    pp.runpp(net, calculate_voltage_angles=True, init= 'flat')
                    # print("loadflow complete")
                    out_Voltages = net.res_bus["vm_pu"][0:12]
                    out_QTrafo = net.res_trafo["q_hv_mvar"][0]
                    # print(out_Voltages)
                    Violations_num = 0
                    
                    for index in range(len(out_Voltages)):
                        # if (abs(out_Voltages-1) > voltage_dev).bool():
                        if abs(out_Voltages[index]-1) > voltage_dev:
                            Violations_num = Violations_num + 1
                    a0 = round(Violations_num,0)
                    a1 = round(abs(out_QTrafo),2)
                    a2 = round(abs(1 - np.mean(out_Voltages)),3)
                    a3 = round(ttransf,0)
                    a4 = round(tcap,0)
                    a5 = round(Qindex,0)
                    Performance.append([a0,a1,a2,a3,a4,a5])
                    # print("next iteration2")            
    else:
        for ttransf in range(Tap_init, Tap_final+1):
            for Qindex in range(-1,2):
                Qgen = Qindex * math.sin(math.acos(powerfactor)) * Prated
                # net = pn.create_cigre_network_mv(with_der="pv_wind",tap_position = ttransf, step_cap = 0)
                net.trafo["tap_pos"]= ttransf
                net.load["q_mvar"][0]= 0
                net.sgen["q_mvar"] = Qgen
                pp.runpp(net, calculate_voltage_angles=True, init= 'flat') 
                out_Voltages = net.res_bus["vm_pu"][0:12]
                out_QTrafo = net.res_trafo["q_hv_mvar"][0]
                Violations_num = 0
                
                for index in range(len(out_Voltages)):
                    if abs(out_Voltages[index]-1) > voltage_dev:
                        Violations_num = Violations_num + 1
                
                a0 = round(Violations_num,0)
                a1 = round(abs(out_QTrafo),2)
                a2 = round(abs(1 - np.mean(out_Voltages)),3)
                a3 = round(ttransf,0)
                a4 = round(0,0)
                a5 = round(Qindex,0)
                Performance.append([a0,a1,a2,a3,a4,a5])
                # print("next iteration")
    
    Performance1=sorted(Performance, key=lambda x: (x[1], x[0], x[2]))
    P1= [x for x in Performance1 if x[:][1]<=5] # 5 is reactive power window
    P2= [x for x in Performance1 if x[:][1]>5]
    P0=sorted(P1, key=lambda x: (x[0], x[1], x[2]))
    Performance=P0+P2
    for s in Performance:
        print(*s)
    return Performance[0][5] * math.sin(math.acos(powerfactor)) * Prated, Performance[0][3], Performance[0][4]