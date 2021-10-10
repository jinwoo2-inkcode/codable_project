import requests 
from pprint import pprint

API_KEY = 'Q8oZ1WAdkXVpTint'
authentication = "vasp?API_KEY="+ API_KEY

# request_type, identifier, parameters
request_string = 'https://www.materialsproject.org/rest/v2/{}/{}/{}'

#user input compound name
user_compound_input = input("Enter Compound")

#Water Compound
temp = requests.get(request_string.format('materials',user_compound_input, authentication)) #Find how to format the compound input
# temp = requests.get(request_string.format(F'materials','mp-1234', authentication))
# print(request_string.format('materials','mp-1234', authentication))

temp_dict = temp.json()


#components to display
pprint(temp_dict['response'][0]['elements'])
pprint(temp_dict['response'][0]['energy'])
pprint(temp_dict['response'][0]['unit_cell_formula'])

print(len(temp_dict['response'][0]['elements']))



#testing with water
# h_atom = temp_dict['response'][0]['unit_cell_formula']['H']
# o_atom = temp_dict['response'][0]['unit_cell_formula']['O']


#Greatest common Denominator
"""
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

gcd_value = gcd(h_atom,o_atom)

print out water
print('H' + str(int(h_atom/gcd_value)) + 'O')
"""

#pprint(temp_dict['response'][0]['volume'])