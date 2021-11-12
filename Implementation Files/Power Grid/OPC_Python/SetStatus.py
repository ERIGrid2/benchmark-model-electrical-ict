def Execute(oStaExtMea: "powerfactory.DataObject", iIsReader: int, iIsWriter: int) -> None:
    """
    Sets read and write status of a StaExt* object.

    :param[in] oStaExtMea: The external measurement to set status.
    :param[in] iIsReader:  Reader status: 0=no; otherwise: yes.
    :param[in] iIsWriter:  Writer status: 0=no; otherwise: yes.
    """
    STATUS_WRITE = 1073741824  # write flag
    STATUS_READ = 536870912    # read flag

    # Set the reader flag
    if iIsReader:
        oStaExtMea.SetStatusBit(STATUS_READ)

    # Set the writer flag
    if iIsWriter:
        oStaExtMea.SetStatusBit(STATUS_WRITE)
