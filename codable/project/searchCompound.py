"""
used for search algorithm of compound in api
"""
from chemspipy import ChemSpider

cs = ChemSpider('J3XTYvy3MAuYai74BsJBm6krPMOWmtLY')

c = cs.get_compound(2157)

print(c.molecular_formula)
print(c.smiles)
print(c.common_name)