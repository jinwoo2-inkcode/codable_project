"""
create objects and each function for it
"""
import vpython as vp

#atoms
def atoms(atomName, c, size, loc):
    atom = vp.sphere(pos=loc, radius=size, color = c)
    location = loc
    return atom, location
    
#chains
def chains(atom1, atom2):
    chain = vp.cylinder(pos = atom1, axis = atom2-atom1, radius=0.05)
    return chain