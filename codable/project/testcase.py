import Structure as sct
#import searchAtom as sa
import vpython as vp
#import searchCompound as sc
import api_demo as ad

#create water
oxygen, o_loc = sct.atoms("O", vp.color.red, 1, vp.vector(0,0,0))
hydrogen1, h1_loc = sct.atoms("H", vp.color.blue, 0.5, vp.vector(2,2,2))
hydrogen2, h2_loc = sct.atoms("H", vp.color.blue, 0.5, vp.vector(-2,2,2))

h2o = sct.chains(o_loc, h1_loc)
h2o = sct.chains(o_loc, h2_loc)

# name = sa.getAtom(1)[0]
# mass = sa.getAtom(1)[1]

# data = sc.getInfo(2157)
data = ad.temp_dict['response'][0]['energy'] #only input string, not array
# print(name)
# print(mass)

na = sct.dataDisplay(data, vp.color.white, vp.vector(3,3,3))