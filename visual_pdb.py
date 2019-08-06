"""Setting numpy"""
import numpy as np
"""Setting webbrowser"""
import webbrowser

num_proteins_input = input('Which PDB do you want to open?\nPlease type PDB IDs here: ')

id_list = num_proteins_input.split(' ')

"""open pdb site"""
def open_pdb_site(pdb_id_input):
    base_url = "http://www.rcsb.org/structure/"
    unique_url = base_url+str(pdb_id_input)
    webbrowser.open(unique_url)

for el_id in id_list:
	open_pdb_site(el_id)

