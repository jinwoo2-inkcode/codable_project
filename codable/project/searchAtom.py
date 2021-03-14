"""
used for search algorithm of elements in periodic table
Also takes periotic table api
"""

import periodictable as pt

def getAtom(atomNumber):
    elem = elements[atomNumber]
    return elem.name, elem.mass