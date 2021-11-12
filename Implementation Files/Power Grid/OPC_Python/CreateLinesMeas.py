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
    # Gets the PowerFactory application and the current script
    if not pfApp:
        pfApp = powerfactory.GetApplication()     # @UndefinedVariable
    script = pfApp.GetCurrentScript()

    # add external measurements (StaExtbrkmea+StaExtdatmea) to all switches (StaSwitch)
    aLines = pfApp.GetCalcRelevantObjects('*.ElmLne,*.ElmTr2')

    # Define a list of elements in which list values with the format [breaker, terminal] are added
    lines = []
    # Define a set of terminals
    for oline in aLines:
        oCubicle1 = oline.GetCubicle(0)
        oCubicle2 = oline.GetCubicle(1)
        oTerminal1 = oCubicle1.GetParent()
        oTerminal2 = oCubicle2.GetParent()
        sTerminal1 = oTerminal1.GetAttribute('loc_name')
        sTerminal2 = oTerminal2.GetAttribute('loc_name')
        if sTerminal1 < sTerminal2:
            lines.append([oline,oTerminal1,oTerminal2,1])
        else:
            lines.append([oline, oTerminal2, oTerminal1,0])

    # Iteration through all the terminals that have breakers
    rep_check = []
    for line in lines:
        # For each terminal restart all the counters of the elements
        counter_Ln = 1
        counter_Tr = 1
        oCubicle1 = line[0].GetCubicle(0)
        oCubicle2 = line[0].GetCubicle(1)
        sTerminal1 = line[1].GetAttribute('loc_name')
        sTerminal2 = line[2].GetAttribute('loc_name')
        pfApp.PrintInfo("%s" % (sTerminal1))
        pfApp.PrintInfo("%s" % (sTerminal2))
        sBaseName1 = ''
        sBaseName2 = ''
        sTerminal1 = sTerminal1.upper()
        sTerminal1 = sTerminal1.replace('BUS ', 'BB')
        sTerminal2 = sTerminal2.upper()
        sTerminal2 = sTerminal2.replace('BUS ', 'BB')
        ElementClass = line[0].GetClassName()
        pfApp.PrintInfo("%s" % (sTerminal1))
        pfApp.PrintInfo("%s" % (sTerminal2))

        # Create meas for voltage in busbars
        sBaseName = 'BB%s_V_Res' % (sTerminal1[-2:])
        if sBaseName not in rep_check:
            # create measurement (StaExtdatmea) for bus V output
            pfApp.PrintInfo("%s" % (sTerminal1))
            pfApp.PrintInfo("%s" % (sTerminal2))
            oStaExtMea = oCubicle1.CreateObject('StaExtdatmea', sBaseName)
            SetStatus.Execute(oStaExtMea, 0, 1)  # set status to write (PF -> OPC)
            oStaExtMea.pCalObj = line[0]
            if ElementClass == 'ElmTr2':
                if line[3] == 1:
                    oStaExtMea.varCal = 'm:u1:bushv'
                else:
                    oStaExtMea.varCal = 'm:u1:buslv'
            else:
                if line[3] == 1:
                    oStaExtMea.varCal = 'm:u1:bus1'
                else:
                    oStaExtMea.varCal = 'm:u1:bus2'
            oStaExtMea.pCalObjSim = line[0]

            if ElementClass == 'ElmTr2':
                if line[3] == 1:
                    oStaExtMea.varCalSim = 'm:u1:bushv'
                else:
                    oStaExtMea.varCalSim = 'm:u1:buslv'
            else:
                if line[3] == 1:
                    oStaExtMea.varCalSim = 'm:u1:bus1'
                else:
                    oStaExtMea.varCalSim = 'm:u1:bus2'
            oStaExtMea.i_dat = 3  # set type to real
            sTagId = '%s%s' % (sTagPrefix, sBaseName)
            oStaExtMea.sTagID = sTagId
            oStaExtMea.for_name = sTagId
            rep_check.append(sBaseName)

        sBaseName = 'BB%s_V_Res' % (sTerminal2[-2:])

        if sBaseName not in rep_check:

            # create measurement (StaExtdatmea) for bus V output
            pfApp.PrintInfo("%s" % (sTerminal2))
            oStaExtMea = oCubicle2.CreateObject('StaExtdatmea', sBaseName)
            SetStatus.Execute(oStaExtMea, 0, 1)  # set status to write (PF -> OPC)
            oStaExtMea.pCalObj = line[0]
            if ElementClass == 'ElmTr2':
                if line[3] == 1:
                    oStaExtMea.varCal = 'm:u1:buslv'
                else:
                    oStaExtMea.varCal = 'm:u1:bushv'
            else:
                if line[3] == 1:
                    oStaExtMea.varCal = 'm:u1:bus2'
                else:
                    oStaExtMea.varCal = 'm:u1:bus1'
            oStaExtMea.pCalObjSim = line[0]
            if ElementClass == 'ElmTr2':
                if line[3] == 1:
                    oStaExtMea.varCalSim = 'm:u1:buslv'
                else:
                    oStaExtMea.varCalSim = 'm:u1:bushv'
            else:
                if line[3] == 1:
                    oStaExtMea.varCalSim = 'm:u1:bus2'
                else:
                    oStaExtMea.varCalSim = 'm:u1:bus1'

            oStaExtMea.i_dat = 3  # set type to real
            sTagId = '%s%s' % (sTagPrefix, sBaseName)
            oStaExtMea.sTagID = sTagId
            oStaExtMea.for_name = sTagId
            rep_check.append(sBaseName)
        # Create rest of the tags
        if ElementClass == 'ElmTr2':
            sBaseName1 = '%s_Tr0%s_%s_%s_P' % (sTerminal1, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
            sBaseName2 = '%s_Tr0%s_%s_%s_P' % (sTerminal2, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
            if sBaseName1 in rep_check:
                counter_Tr += 1
                sBaseName1 = '%s_Tr0%s_%s_%s_P' % (sTerminal1, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
                sBaseName2 = '%s_Tr0%s_%s_%s_P' % (sTerminal2, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
                rep_check.append(sBaseName1)
                rep_check.append(sBaseName2)
            else:
                rep_check.append(sBaseName1)
                rep_check.append(sBaseName2)

        elif ElementClass == 'ElmLne':
            sBaseName1 = '%s_Ln0%s_%s_%s_P' % (sTerminal1, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
            sBaseName2 = '%s_Ln0%s_%s_%s_P' % (sTerminal2, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
            if sBaseName1 in rep_check:
                counter_Ln += 1
                sBaseName1 = '%s_Ln0%s_%s_%s_P' % (sTerminal1, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
                sBaseName2 = '%s_Ln0%s_%s_%s_P' % (sTerminal2, counter_Tr, sTerminal1[-2:], sTerminal2[-2:])
                rep_check.append(sBaseName1)
                rep_check.append(sBaseName2)
            else:
                rep_check.append(sBaseName1)
                rep_check.append(sBaseName2)

        sBaseName1 = sBaseName1.replace(' ', '_')
        sBaseName1 = sBaseName1.replace('/', '_')
        sBaseName2 = sBaseName2.replace(' ', '_')
        sBaseName2 = sBaseName2.replace('/', '_')

        # Create meas for P in cubicle 1 and 2
        oStaExtMea1 = oCubicle1.CreateObject('StaExtdatmea', sBaseName1, '_Res')
        oStaExtMea2 = oCubicle2.CreateObject('StaExtdatmea', sBaseName2, '_Res')
        if iDebug:
            pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for load %s."
                            % (script.loc_name, oStaExtMea1, oCubicle1, line[0]))

        SetStatus.Execute(oStaExtMea1, 0, 1)    # set status to write (PF -> OPC)
        SetStatus.Execute(oStaExtMea2, 0, 1)  # set status to write (PF -> OPC)
        oStaExtMea1.pCalObj = line[0]
        oStaExtMea2.pCalObj = line[0]
        if ElementClass == 'ElmTr2':
            if line[3] == 1:
                oStaExtMea1.varCal = 'm:P:bushv'
                oStaExtMea2.varCal = 'm:P:buslv'
            else:
                oStaExtMea1.varCal = 'm:P:buslv'
                oStaExtMea2.varCal = 'm:P:bushv'
        else:
            if line[3] == 1:
                oStaExtMea1.varCal = 'm:P:bus1'
                oStaExtMea2.varCal = 'm:P:bus2'
            else:
                oStaExtMea1.varCal = 'm:P:bus2'
                oStaExtMea2.varCal = 'm:P:bus1'
        oStaExtMea1.pCalObjSim = line[0]
        oStaExtMea2.pCalObjSim = line[0]
        if ElementClass == 'ElmTr2':
            if line[3] == 1:
                oStaExtMea1.varCalSim = 'm:P:bushv'
                oStaExtMea2.varCalSim = 'm:P:buslv'
            else:
                oStaExtMea1.varCalSim = 'm:P:buslv'
                oStaExtMea2.varCalSim = 'm:P:bushv'
        else:
            if line[3] == 1:
                oStaExtMea1.varCalSim = 'm:P:bus1'
                oStaExtMea2.varCalSim = 'm:P:bus2'
            else:
                oStaExtMea1.varCalSim = 'm:P:bus2'
                oStaExtMea2.varCalSim = 'm:P:bus1'
        oStaExtMea1.i_dat = 3    # set type to real
        oStaExtMea2.i_dat = 3  # set type to real

        sTagId1 = '%s%s_Res' % (sTagPrefix, sBaseName1)
        sTagId2 = '%s%s_Res' % (sTagPrefix, sBaseName2)
        oStaExtMea1.sTagID = sTagId1
        oStaExtMea1.for_name = sTagId1
        oStaExtMea2.sTagID = sTagId2
        oStaExtMea2.for_name = sTagId2

        # Create meas for Q in cubicle 1 and 2

        sBaseName1 = sBaseName1.replace('_P', '_Q')
        sBaseName2 = sBaseName2.replace('_P', '_Q')

        oStaExtMea1 = oCubicle1.CreateObject('StaExtdatmea', sBaseName1, '_Res')
        oStaExtMea2 = oCubicle2.CreateObject('StaExtdatmea', sBaseName2, '_Res')

        SetStatus.Execute(oStaExtMea1, 0, 1)  # set status to write (PF -> OPC)
        SetStatus.Execute(oStaExtMea2, 0, 1)  # set status to write (PF -> OPC)
        oStaExtMea1.pCalObj = line[0]
        oStaExtMea2.pCalObj = line[0]
        if ElementClass == 'ElmTr2':
            if line[3] == 1:
                oStaExtMea1.varCal = 'm:Q:bushv'
                oStaExtMea2.varCal = 'm:Q:buslv'
            else:
                oStaExtMea1.varCal = 'm:Q:buslv'
                oStaExtMea2.varCal = 'm:Q:bushv'
        else:
            if line[3] == 1:
                oStaExtMea1.varCal = 'm:Q:bus1'
                oStaExtMea2.varCal = 'm:Q:bus2'
            else:
                oStaExtMea1.varCal = 'm:Q:bus2'
                oStaExtMea2.varCal = 'm:Q:bus1'
        oStaExtMea1.pCalObjSim = line[0]
        oStaExtMea2.pCalObjSim = line[0]
        if ElementClass == 'ElmTr2':
            if line[3] == 1:
                oStaExtMea1.varCalSim = 'm:Q:bushv'
                oStaExtMea2.varCalSim = 'm:Q:buslv'
            else:
                oStaExtMea1.varCalSim = 'm:Q:buslv'
                oStaExtMea2.varCalSim = 'm:Q:bushv'
        else:
            if line[3] == 1:
                oStaExtMea1.varCalSim = 'm:Q:bus1'
                oStaExtMea2.varCalSim = 'm:Q:bus2'
            else:
                oStaExtMea1.varCalSim = 'm:Q:bus2'
                oStaExtMea2.varCalSim = 'm:Q:bus1'
        oStaExtMea1.i_dat = 3  # set type to real
        oStaExtMea2.i_dat = 3  # set type to real

        sTagId1 = '%s%s_Res' % (sTagPrefix, sBaseName1)
        sTagId2 = '%s%s_Res' % (sTagPrefix, sBaseName2)
        oStaExtMea1.sTagID = sTagId1
        oStaExtMea1.for_name = sTagId1
        oStaExtMea2.sTagID = sTagId2
        oStaExtMea2.for_name = sTagId2

        # Create tags for Tap position if the branch element is a transformer

        if ElementClass == 'ElmTr2':

            sBaseName1 = sBaseName1.replace('_Q', '_Tap')

            # create measurement (StaExttapmea) for tap input
            oStaExtMea = oCubicle1.CreateObject('StaExttapmea', sBaseName1)

            oTransformerType = line[0].typ_id
            if not oTransformerType:
                pfApp.PrintWarn('%s - The transformer %o has no type, so the measurement %o has no measurement table.'
                                % (script.loc_name, line[0], oStaExtMea))
            else:
                iTapMin = getattr(oTransformerType, 'ntpmn') if hasattr(oTransformerType, 'ntpmn') else None
                iTapMax = getattr(oTransformerType, 'ntpmx') if hasattr(oTransformerType, 'ntpmx') else None
                if iTapMin and iTapMax:
                    taps = list(range(iTapMin, iTapMax + 1))  # list(range(iTapMax, iTapMin - 1, -1))
                    oStaExtMea.Tap = taps
                    oStaExtMea.Exttap = taps
                # change measurement value
                if hasattr(oTransformerType, 'nntap0'):
                    iTapPos = getattr(oTransformerType, 'nntap0')
                    setattr(oStaExtMea, 'Tapmea', iTapPos)  # default value

            SetStatus.Execute(oStaExtMea, 1, 0)  # set status to read (OPC -> PF)
            oStaExtMea.pObject = line[0]
            oStaExtMea.variabName = 'nntap'

            sTagId = '%s%s' %(sTagPrefix, sBaseName1)
            oStaExtMea.sTagID = sTagId
            oStaExtMea.for_name = sTagId

            # create measurement (StaExtdatmea) for tap output
            oStaExtMea = oCubicle1.CreateObject('StaExtdatmea', sBaseName1, '_Res')
            if iDebug:
                pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for transformer %s."
                                % (script.loc_name, oStaExtMea, oCubicle1, line[0]))

            SetStatus.Execute(oStaExtMea, 0, 1)  # set status to write (PF -> OPC)
            oStaExtMea.pCalObj = line[0]
            oStaExtMea.varCal = 'nntap'
            oStaExtMea.pCalObjSim = line[0]
            oStaExtMea.varCalSim = 'nntap'
            oStaExtMea.i_dat = 1  # set type to integer

            sTagId = ('%s%s_Res' % (sTagPrefix, sBaseName1))
            oStaExtMea.sTagID = sTagId
            oStaExtMea.for_name = sTagId

            # create measurement (StaExtdatmea) for tap control
            oStaExtMea = oCubicle1.CreateObject('StaExtdatmea', sBaseName1, '_Ctrl')
            if iDebug:
                pfApp.PrintInfo("%s - Create measurement %s in cubicle %s for transformer %s."
                                % (script.loc_name, oStaExtMea, oCubicle1, line[0]))

            SetStatus.Execute(oStaExtMea, 1, 0)  # set status to read (OPC -> PF)
            oStaExtMea.pObject = line[0]
            oStaExtMea.variabName = 'nntap'
            oStaExtMea.pCtrl = line[0]  # work-around for not using a tap controller
            oStaExtMea.varName = 'nntap_int'
            oStaExtMea.pCalObj = line[0]
            oStaExtMea.varCal = 'nntap'
            oStaExtMea.pCalObjSim = line[0]
            oStaExtMea.varCalSim = 'nntap'
            oStaExtMea.i_mode = 1  # set mode to incremental
            oStaExtMea.i_dat = 1  # set type to integer

            sTagId = '%s%s_Ctr' % (sTagPrefix, sBaseName1)
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
