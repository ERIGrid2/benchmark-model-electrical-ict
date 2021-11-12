import powerfactory                 
import ReplaceInvalidChars
import SetStatus
def Execute(pfApp: "powerfactory.Application"=None, sTagPrefix: str='PF.', sSeparator: str=',', iDebug: int=0) -> int:
    """
    Creates external measurements for all generators (ElmSym, ElmGenstat):
     * base name <BASE_NAME> = Gen_<VOLTAGE>kV_<GENERATOR>
     * base tag <BASE_TAG> = <TAG_PREFIX><STATION><SEPARATOR><BASE_NAME>
     * StaExtdatmea for generator's P output:
        - use name:  P_<STATION>_<BASE_NAME>_Res
        - use tag:   <BASE_TAG>_P_RES
     * StaExtdatmea for generator's Q output:
        - use name:  Q_<STATION>_<BASE_NAME>_Res
        - use tag:   <BASE_TAG>_Q_RES
     * StaExtdatmea for generator's V output:
        - use name:  V_<STATION>_<BASE_NAME>_Res
        - use tag:   <BASE_TAG>_V_RES
     * StaExtdatmea for generator's P control (only if no P control at slack machine):
        - use name:  P_<STATION>_<BASE_NAME>_Ctrl
        - use tag:   <BASE_TAG>_P_CTRL
     * StaExtdatmea for generator's V control:
        - use name:  V_<STATION>_<BASE_NAME>_Ctrl
        - use tag:   <BASE_TAG>_V_CTRL

    Creates external measurements for all loads (ElmLoad):
     * base name <BASE_NAME> = Load_<VOLTAGE>kV_<LOAD>
     * base tag <BASE_TAG> = <TAG_PREFIX><STATION><SEPARATOR><BASE_NAME>
     * StaExtdatmea for load's P output:
        - use name:  P_<STATION>_<BASE_NAME>_Res
        - use tag:   <BASE_TAG>_P_RES
     * StaExtdatmea for load's Q output:
        - use name:  Q_<STATION>_<BASE_NAME>_Res
        - use tag:   <BASE_TAG>_Q_RES
     * StaExtdatmea for load's V output:
        - use name:  V_<STATION>_<BASE_NAME>_Res
        - use tag:   <BASE_TAG>_V_RES

    :param[in] pfApp:       The PowerFactory application.
    :param[in] sTagPrefix:  The prefix of the generated measurement tag.
    :param[in] sSeparator:  Separator in the middle of the OPC tag.
    :param[in] iDebug:      Debug output: 0=no output; otherwise=output.

    :return:                The number of created measurement objects.
    """
    # Gets the PowerFactory application and the current script
    if not pfApp:
        pfApp = powerfactory.GetApplication()     # @UndefinedVariable
    script = pfApp.GetCurrentScript()

    # initialise the counter
    iCounter = 0

    # add external measurements (StaExtdatmea) to all generators (ElmSym, ElmGenstat)
    aGenerators = pfApp.GetCalcRelevantObjects('*.ElmSym,*.ElmGenstat,*.ElmShnt')

    # Define a list of elements in which list values with the format [breaker, terminal] are added
    generators = []
    # Define a set of terminals
    terminals = set()


    # breakers is filled with all the object breakers and its respective terminal. A set of terminals are also defined (unique set)
    # breakers is a list of lists with structure breakers = [[breaker 1, connected terminal][breaker 2, connected terminal]...]
    for oGenerator in aGenerators:
        oCubicle = oGenerator.GetCubicle(0)
        oTerminal = oCubicle.GetParent()
        terminals.add(oTerminal)
        generators.append([oGenerator,oTerminal])


    for terminal in terminals:

        # For each terminal restart all the counters of the elements
        counter_Gn = 0
        counter_PV = 0
        counter_WT = 0
        counter_DER = 0
        counter_Cap = 0

        # Iteration through all the list elements [breaker, connected busbar]
        for oGenerator in generators:
            # Checks if the current terminal is connected to the breaker
            if terminal in oGenerator:
                # get cubicle
                oCubicle = oGenerator[0].GetCubicle(0)
                # Get name of busbar connected to breaker
                sTerminal = terminal.GetAttribute('loc_name')
                # Get class of the element connected to the switch
                ElementClass = oGenerator[0].GetClassName()
                # If the element is ElmGenStat, it retrieves the category of the DER
                DerType = getattr(oGenerator[0], 'cCategory') if hasattr(oGenerator[0], 'cCategory') else None
                sBaseName = ''
                sTerminal = sTerminal.upper()
                sTerminal = sTerminal.replace('BUS ', 'BB')
                if ElementClass == 'ElmGenstat' and DerType == 'Photovoltaic':
                    Type_string = 'PV'
                    counter_PV += 1
                    s_count = str(counter_PV)
                    sBaseName = '%s_%s0%s_P_' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmGenstat' and DerType == 'Wind':
                    Type_string = 'WT'
                    counter_WT += 1
                    s_count = str(counter_WT)
                    sBaseName = '%s_%s0%s_P_' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmGenstat':
                    Type_string = 'DER'
                    counter_DER += 1
                    s_count = str(counter_DER)
                    sBaseName = '%s_%s0%s_P_' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmShnt':
                    Type_string = 'Cap'
                    counter_Cap += 1
                    s_count = str(counter_Cap)
                    sBaseName = '%s_%s0%s_P_' % (sTerminal, Type_string, s_count)
                else:
                    Type_string = 'Gn'
                    counter_GnGn += 1
                    s_count = str(counter_Gn)
                    sBaseName = '%s_%s0%s_P_' % (sTerminal, Type_string, s_count)
                sBaseName = sBaseName.replace(' ', '_')
                sBaseName = sBaseName.replace('/', '_')

                # create measurement (StaExtdatmea) for generator's P output
                oStaExtMea = oCubicle.CreateObject('StaExtdatmea', sBaseName, 'Res')
                if iDebug:
                    pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for generator %s."
                                    % (script.loc_name, oStaExtMea, oCubicle, oGenerator[0]))

                SetStatus.Execute(oStaExtMea, 0, 1)    # set status to write (PF -> OPC)
                oStaExtMea.pCalObj = oGenerator[0]
                oStaExtMea.varCal = 'm:P:bus1'
                oStaExtMea.pCalObjSim = oGenerator[0]
                oStaExtMea.varCalSim = 'm:P:bus1'
                oStaExtMea.i_dat = 3    # set type to real

                sTagId = '%s%sRes' % (sTagPrefix, sBaseName)
                oStaExtMea.sTagID = sTagId
                oStaExtMea.for_name = sTagId

                # create measurement (StaExtdatmea) for generator's Q output

                sBaseName = sBaseName.replace('_P_','_Q_') #change the basename to Q

                oStaExtMea = oCubicle.CreateObject('StaExtdatmea', sBaseName, 'Res')
                if iDebug:
                    pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for generator %s."
                                    % (script.loc_name, oStaExtMea, oCubicle, oGenerator[0]))

                SetStatus.Execute(oStaExtMea, 0, 1)    # set status to write (PF -> OPC)
                oStaExtMea.pCalObj = oGenerator[0]
                oStaExtMea.varCal = 'm:Q:bus1'
                oStaExtMea.pCalObjSim = oGenerator[0]
                oStaExtMea.varCalSim = 'm:Q:bus1'
                oStaExtMea.i_dat = 3    # set type to real

                sTagId = '%s%sRes' % (sTagPrefix, sBaseName)
                oStaExtMea.sTagID = sTagId
                oStaExtMea.for_name = sTagId

                # create measurement (StaExtdatmea) for generator's P control
                sBaseName = sBaseName.replace('_Q_', '_P_')  # change the basename to Q

                pfApp.PrintInfo("%s" % (Type_string))
                if Type_string != 'Cap':
                    if oGenerator[0].ip_ctrl == 0: # no P control at slack machine
                        oStaExtMea = oCubicle.CreateObject('StaExtdatmea', sBaseName, 'Ctr')
                        SetStatus.Execute(oStaExtMea, 1, 0)    # set status to read (OPC -> PF)
                        oStaExtMea.pObject = oGenerator[0]
                        oStaExtMea.variabName = 'pgini'
                        oStaExtMea.pCalObj = oGenerator[0]
                        oStaExtMea.varCal = 'pgini'
                        oStaExtMea.pCalObjSim = oGenerator[0]
                        oStaExtMea.varCalSim = 'pgini'
                        oStaExtMea.i_mode = 1
                        oStaExtMea.i_dat = 3    # set type to real

                        sTagId = '%s%sCtr' % (sTagPrefix, sBaseName)
                        oStaExtMea.sTagID = sTagId
                        oStaExtMea.for_name = sTagId

                if Type_string == 'Cap':
                    sBaseName = sBaseName.replace('_P_', '_Step_')  # change the basename to step if capacitor
                else:
                    sBaseName = sBaseName.replace('_P_', '_Q_')  # change the basename to Q

                oStaExtMea = oCubicle.CreateObject('StaExtdatmea', sBaseName, 'Ctr')
                if iDebug:
                    pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for generator %s."
                                    % (script.loc_name, oStaExtMea, oCubicle, oGenerator[0]))

                SetStatus.Execute(oStaExtMea, 1, 0)  # set status to read (OPC -> PF)
                oStaExtMea.pObject = oGenerator[0]
                if Type_string == 'Cap':
                    oStaExtMea.variabName = 'e:ncapa'
                else:
                    oStaExtMea.variabName = 'qgini'

                oStaExtMea.pCalObj = oGenerator[0]
                if Type_string == 'Cap':
                    oStaExtMea.varCal = 'e:ncapa'
                else:
                    oStaExtMea.varCal = 'qgini'
                oStaExtMea.pCalObjSim = oGenerator[0]
                if Type_string == 'Cap':
                    oStaExtMea.varCalSim = 'e:ncapa'
                else:
                    oStaExtMea.varCalSim = 'qgini'
                oStaExtMea.i_mode = 1
                oStaExtMea.i_dat = 3  # set type to real

                sTagId = '%s%sCtr' % (sTagPrefix, sBaseName)
                oStaExtMea.sTagID = sTagId
                oStaExtMea.for_name = sTagId


if __name__ == "__main__":
    PF_APP = powerfactory.GetApplication()  
    SCRIPT = PF_APP.GetCurrentScript()
    S_TAG_PREFIX = SCRIPT.sTagPrefix if hasattr(SCRIPT, 'sTagPrefix') else 'PF.'
    S_SEPARATOR = SCRIPT.sSeparator if hasattr(SCRIPT, 'sSeparator') else ','
    I_DEBUG = int(SCRIPT.iDebug) if hasattr(SCRIPT, 'iDebug') else 0
    Execute(PF_APP, S_TAG_PREFIX, S_SEPARATOR, I_DEBUG)
    PF_APP = None
