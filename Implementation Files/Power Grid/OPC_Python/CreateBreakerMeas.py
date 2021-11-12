import powerfactory                 
import ReplaceInvalidChars
import SetStatus

def Execute(pfApp: "powerfactory.Application"=None, sTagPrefix: str='PF.', sSeparator: str=',', iDebug: int=0) -> int:
    """
    Creates breaker measurements for all switches (StaSwitch):
     * base name <BASE_NAME> = <SWITCH>_<VOLTAGE>kV_<TERMINAL>_<CUBICLE>
     * StaExtbrkmea as reader from OPC server:
        - use name:  <STATION>_<BASE_NAME>
        - use tag:   <TAG_PREFIX><STATION><SEPARATOR><BASE_NAME>_BK
     * StaExtdatmea as writer to OPC server:
        - use name:  Brk_<STATION>_<BASE_NAME>_Res
        - use tag:   <TAG_PREFIX><STATION><SEPARATOR><BASE_NAME>_BK_RES
    Creates breaker measurements for all couplers (ElmCoup):
     * base name <BASE_NAME> = <CB|Disc>_<VOLTAGE>kV_<TERMINAL>_<COUPLER>
     * StaExtbrkmea as reader from OPC server:
        - use name:  <STATION>_<BASE_NAME>
        - use tag:   <TAG_PREFIX><STATION><SEPARATOR><BASE_NAME>_BK
     * StaExtdatmea as writer to OPC server:
        - use name:  Brk_<STATION>_<BASE_NAME>_Res
        - use tag:   <TAG_PREFIX><STATION><SEPARATOR><BASE_NAME>_BK_RES

    :param[in] pfApp:       The PowerFactory application.
    :param[in] sTagPrefix:  The prefix of the generated measurement tag.
    :param[in] sSeparator:  Separator in the middle of the OPC tag.
    :param[in] iDebug:      Debug output: 0=no output; otherwise=output.

    :return:                The number of created measurement objects.
    """
    # Get the PowerFactory application and the current script
    if not pfApp:
        pfApp = powerfactory.GetApplication()     # @UndefinedVariable
    script = pfApp.GetCurrentScript()


    # add external measurements (StaExtbrkmea+StaExtdatmea) to all switches (StaSwitch)
    aBreakers = pfApp.GetCalcRelevantObjects('*.StaSwitch')

    # Define a list of elements in which list values with the format [breaker, terminal] are added
    breakers = []
    # Define a set of terminals
    terminals = set()


    # breakers is filled with all the object breakers and its respective terminal. A set of terminals are also defined (unique set)
    # breakers is a list of lists with structure breakers = [[breaker 1, connected terminal][breaker 2, connected terminal]...]
    for oBreaker in aBreakers:
        oCubicle = oBreaker.GetParent()
        oTerminal = oCubicle.GetParent()
        oElement = oCubicle.GetBranch()
        if not oElement:
            continue
        else:
            terminals.add(oTerminal)
            breakers.append([oBreaker,oTerminal])

    Type_string =''

    # iteration through all the terminals that have breakers

    for terminal in terminals:

        #For each terminal restart all the counters of the elements
        counter_Tr = 0
        counter_Ln = 0
        counter_Ld = 0
        counter_PV = 0
        counter_WT = 0
        counter_DER = 0
        counter_Cap = 0
        counter_Elem = 0

        # Iteration through all the list elements [breaker, connected busbar]
        for oBreaker in breakers:
            # checks if the current terminal is connected to the breaker
            if terminal in oBreaker:
                 # get cubicle and terminal (incl. its names) of the breaker
                oCubicle = oBreaker[0].GetParent()
                oElement = oCubicle.GetBranch()

                sElement = oElement.GetAttribute('loc_name')

                # Get name of busbar connected to breaker
                sTerminal = terminal.GetAttribute('loc_name')

                # Retrieve busbars connected to branch element
                connection_busbars = oElement.GetConnectedElements()
                connection_list = list(connection_busbars)

                bus1 = connection_list[0].GetAttribute('loc_name')
                bus2 = connection_list[1].GetAttribute('loc_name') if len(connection_list) == 2 else ''

                # Removes the busbar where the switch is connected from the set
                if sTerminal == bus1:
                    sSecond_busbar = bus2
                else:
                    sSecond_busbar = bus1

                # Get class of the element connected to the switch
                ElementClass = oElement.GetClassName()
                # If the element is ElmGenStat, it retrieves the category of the DER
                DerType = getattr(oElement, 'cCategory') if hasattr(oElement, 'cCategory') else None

                sBaseName = ''
                sTerminal = sTerminal.upper()
                sTerminal = sTerminal.replace('BUS ', 'BB')

                if ElementClass == 'ElmTr2':
                    Type_string = 'Tr'
                    counter_Tr += 1
                    s_count = str(counter_Tr)
                    sBaseName = '%s_%s0%s_%s_%s_S' % (sTerminal, Type_string, s_count, sTerminal[-2:], sSecond_busbar[-2:])
                elif ElementClass == 'ElmLne':
                    Type_string = 'Ln'
                    counter_Ln += 1
                    s_count = str(counter_Ln)
                    sBaseName = '%s_%s0%s_%s_%s_S' % (sTerminal, Type_string, s_count, sTerminal[-2:], sSecond_busbar[-2:])
                elif ElementClass == 'ElmLod':
                    Type_string = 'Ld'
                    counter_Ld += 1
                    s_count = str(counter_Ld)
                    sBaseName = '%s_%s0%s_S' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmGenstat' and DerType == 'Photovoltaic':
                    Type_string = 'PV'
                    counter_PV += 1
                    s_count = str(counter_PV)
                    sBaseName = '%s_%s0%s_S' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmGenstat' and DerType == 'Wind':
                    Type_string = 'WT'
                    counter_WT += 1
                    s_count = str(counter_WT)
                    sBaseName = '%s_%s0%s_S' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmGenstat':
                    Type_string = 'DER'
                    counter_DER += 1
                    s_count = str(counter_DER)
                    sBaseName = '%s_%s0%s_S' % (sTerminal, Type_string, s_count)
                elif ElementClass == 'ElmShnt':
                    Type_string = 'Cap'
                    counter_Cap += 1
                    s_count = str(counter_Cap)
                    sBaseName = '%s_%s0%s_S' % (sTerminal, Type_string, s_count)
                else:
                    Type_string = 'Elem'
                    counter_Elem += 1
                    s_count = str(counter_Elem)
                    sBaseName = '%s_%s0%s_S' % (sTerminal, Type_string, s_count)

                sBaseName = sBaseName.replace(' ', '_')
                sBaseName = sBaseName.replace('/', '_')

            # create measurement (StaExtbrkmea) for input.
                oStaExtMea = oCubicle.CreateObject('StaExtbrkmea', sBaseName, '_Ctr')
                if iDebug:
                    pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for breaker %s." % (
                    script.loc_name, oStaExtMea, oCubicle, oBreaker[0]))

                SetStatus.Execute(oStaExtMea, 1, 0)  # set status to read (OPC -> PF)
                oStaExtMea.pObject = oBreaker[0]
                oStaExtMea.variabName = 'on_off'

                sBaseName = sBaseName.replace(' ', '_')
                sBaseName = sBaseName.replace('/', '_')
                sTagId = '%s%s_Ctr' % (sTagPrefix,sBaseName)

                oStaExtMea.sTagID = sTagId
                oStaExtMea.for_name = sTagId

                # create measurement (StaExtdatmea) for output
                oStaExtMea = oCubicle.CreateObject('StaExtdatmea', sBaseName, '_Res')
                if iDebug:
                    pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for breaker %s." % (
                    script.loc_name, oStaExtMea, oCubicle, oBreaker[0]))
                SetStatus.Execute(oStaExtMea, 0, 1)  # set status to write (PF -> OPC)
                oStaExtMea.pCalObj = oBreaker[0]
                oStaExtMea.varCal = 'on_off'
                oStaExtMea.pCalObjSim = oBreaker[0]
                oStaExtMea.varCalSim = 'on_off'
                oStaExtMea.i_dat = 1  # set type to integer
                sTagId = '%s%s_Res' % (sTagPrefix,sBaseName)
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
