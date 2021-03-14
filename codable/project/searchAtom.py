"""
used for search algorithm of elements in periodic table
Also takes periotic table api
"""

import periodictable as pt

def getAtom(atomNumber: int) -> string, float:
    """
    Find data for element with atomic number
    args:
        atomNumber: Atomic number of wanted element
    returns:
        Returns name of element
        Returns mass of element
    """
    elem = elements[atomNumber]
    return elem.name, elem.mass