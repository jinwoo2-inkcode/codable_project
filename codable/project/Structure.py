"""
create objects and each function for it
"""
import vpython as vp

#atoms
def atoms(atomName, c, size, loc):
    """
    Creates sphere objects for atoms
    args:
        atomName: name of atom
        c: color of sphere object
        size: radius of sphere object
        loc: vector of location of sphere object
    returns:
        Creates sphere object within 3D space
        Returns vector location of sphere object
    """
    atom = vp.sphere(pos=loc, radius=size, color = c)
    location = loc
    return atom, location

#chains
def chains(atom1, atom2):
    """
    Creates cylinder objects for chains
    args:
        atom1: vector location of first atom
        atom2: vector location of second atom
    returns:
        Creates cylinder object within 3D space
    """
    chain = vp.cylinder(pos = atom1, axis = atom2-atom1, radius=0.05)
    return chain

#Text Display
def dataDisplay(data, loc, c):
    """
    Displays data as 3D text
    args:
        data: text of atom data
    returns:
        Creates 3D text within 3D space
    """
    atomData = vp.text(text = data, pos = loc, color = c)
    return atomData
