from functions_pdb import *

num_proteins_input = input('How many PDB co-crystal protein structures do you want to get?\nPDB has 42,248 human protein crystal structures: ')
start_el_num_input = input('Where to start?\nPlease input an element number here: ')
length_of_peptide_input = input('How long is the maximum length of short peptides co-crystalized with proteins?\nMany proteins were co-crystalized with short peptides!\nPlease type the maximum length of short peptides here - e.g. 10: ')
resolution_input = input('How big is the maximum resolution?\nUsually proteins with less than 2 resolution are considered high resolution proteins! Please input 2 for now!\nPlease type the maximum resolution here - e.g. 2: ')

get_protein_with_short_peptide(int(num_proteins_input),int(start_el_num_input),int(length_of_peptide_input),float(resolution_input))

print('######################################################################\n\nJSON and CSV files are created! Please find the files in the directory!\n\n######################################################################')

