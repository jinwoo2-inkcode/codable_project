import Structure as sct
import searchAtom as sa
import vpython as vp

oxygen, o_loc = sct.atoms("H", vp.color.red, 1, vp.vector(0,0,0))
hydrogen1, h1_loc = sct.atoms("O", vp.color.blue, 0.5, vp.vector(2,2,2))
hydrogen2, h2_loc = sct.atoms("O", vp.color.blue, 0.5, vp.vector(-2,2,2))

h2o = sct.chains(o_loc, h1_loc)
h2o = sct.chains(o_loc, h2_loc)
sct.dataDisplay('test', vp.color.white, vp.vector(4,4,4))

name = sa.getAtom(1)[0]
mass = sa.getAtom(1)[1]

# print(name)
# print(mass)

# sct.dataDisplay(name, vp.color.white, vp.vector(4,4,4))
# sct.dataDisplay(str(mass), vp.color.yellow, vp.vector(0,0,0))