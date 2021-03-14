"""
used for search algorithm of elements in periodic table
Also takes periotic table api
"""

import periodictable as pt

def getAtom(atomNumber: int):
    """
    Find data for element with atomic number
    args:
        atomNumber: Atomic number of wanted element
    returns:
        Returns name of element
        Returns mass of element
    """
    elem = pt.elements[atomNumber]
    return elem.name, elem.mass

print(getAtom(12))