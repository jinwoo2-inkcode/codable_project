"""
used for search algorithm of compound in api
"""
from chemspipy import ChemSpider

cs = ChemSpider('J3XTYvy3MAuYai74BsJBm6krPMOWmtLY')

def getInfo(compound_number):
    c = cs.get_compound(compound_number)
    return c.molecular_formula + '\n' + c.smiles + '\n' + c.common_name


print(getInfo(2157))

# print(c.molecular_formula)
# print(c.smiles)
# print(c.common_name)