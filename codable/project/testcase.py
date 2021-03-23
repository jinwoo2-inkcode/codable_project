import Structure as sct
import searchAtom as sa
import vpython as vp

hydrogen, h_loc = sct.atoms("H", vp.color.red, 1, vp.vector(0,0,0))
oxygen1, o1_loc = sct.atoms("O", vp.color.blue, 0.5, vp.vector(2,2,2))
oxygen2, o2_loc = sct.atoms("O", vp.color.blue, 0.5, vp.vector(-2,2,2))

h2o = sct.chains(h_loc, o1_loc)
h2o = sct.chains(h_loc, o2_loc)
sct.dataDisplay('test', vp.color.white, vp.vector(4,4,4))

print(sa.getAtom(12))