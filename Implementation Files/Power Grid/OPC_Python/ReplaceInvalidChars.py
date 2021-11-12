def Execute(sText: str) -> str:
    """
    Changes invalid chars so that sText is a regular OPC tag id:
      * replace all spaces by '_'
      * replace all '/' by '_'
      * convert sText to upper case

    :param[in] sText: The text to replace.

    :return:          A regular OPC tag id for the given text.
    """
    # replace all spaces by '_'
    sText = sText.replace(' ', '_')

    # replace all '/' by '_'
    sText = sText.replace('/', '_')

    # to upper case
    sText = sText.upper()

    # return text
    return sText
