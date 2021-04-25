"""
used for search algorithm of compound in api
"""
# from chemspipy import ChemSpider

# cs = ChemSpider('J3XTYvy3MAuYai74BsJBm6krPMOWmtLY')

# def getInfo(compound_number):
#     c = cs.get_compound(compound_number)
#     return c.molecular_formula + '\n' + c.smiles + '\n' + c.common_name

# # def getIDNumber():
# #     return



# print(getInfo(2157))

import pymatgen.core as mg


si = mg.Element("Si")
comp = mg.Composition("O3Fe2")

print(comp)
#print(si.atomic_mass)