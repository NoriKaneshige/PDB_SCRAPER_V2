from bs4 import BeautifulSoup
import requests
from json_pdb import Create_Json_File
from class_pdb import Protein
import json
from time import sleep
import os
import csv

# if os.path.exists("json_pdb.json"):
#   os.remove("json_pdb.json")
# else:
#   print("The file does not exist, so it is going to be created!")

JSON_FILE = "json_pdb.json"
CSV_FILE = "short_pep_pdb_data.csv"

def get_human_pdb_protein_ids():
	with open("protein_id.json", 'r') as f:
		pdb_id_human = json.loads(f.read())
		pdb_id_human_lst = pdb_id_human['http://www.rcsb.org/pdb/resultsV2/sids.jsp?qrid=55BB0FFB'].split('\n')
	return pdb_id_human_lst
	

def get_protein_with_short_peptide(num_of_protein_to_check,start_el_num,length_of_short_peptide,resolution_limit):
	el_num_protein_checked = start_el_num
	protein_inst_list = []
	c1 = Create_Json_File(JSON_FILE)
	base_url = 'https://www.rcsb.org/pdb/rest/describeMol?structureId='
	base_url_for_resolution = 'https://www.rcsb.org/pdb/rest/describePDB?structureId='
	for id_el in get_human_pdb_protein_ids()[start_el_num:num_of_protein_to_check]:
		print(el_num_protein_checked)
		el_num_protein_checked += 1
		unique_url = base_url+str(id_el)
		if unique_url in c1.cache_diction:
			resp = c1.cache_diction.get(unique_url)
		else:
			resp = requests.get(unique_url).text
			c1.cache_diction[unique_url] = resp
			c1.set(unique_url,resp)
		soup = BeautifulSoup(resp,'html.parser')
		polymer_info_list = soup.find('structureid').find_all('polymer')

		unique_url_for_resolution = base_url_for_resolution+str(id_el)
		if unique_url_for_resolution in c1.cache_diction:
			resp_res = c1.cache_diction.get(unique_url_for_resolution)
		else:
			resp_res = requests.get(unique_url_for_resolution).text
			c1.cache_diction[unique_url_for_resolution] = resp_res
			c1.set(unique_url_for_resolution,resp_res)
			sleep(0.1)
		soup_res = BeautifulSoup(resp_res,'html.parser')

		try:
			polymer_description = soup.find('macromolecule')['name']
			resolution = soup_res.find('pdb')['resolution']
			peptide_length_lst = []
			for el in polymer_info_list:
				peptide_length_lst.append(int(el['length']))
			print(id_el)
			if min(peptide_length_lst) <= int(length_of_short_peptide):
				print('Got a short peptide: '+ str(min(peptide_length_lst)))
				if float(resolution) <= float(resolution_limit):
					print('Got a good resolution: '+ str(float(resolution)))
					name = soup.find('structureid')['id']
					polymer_length = el['length']
					resolution = soup_res.find('pdb')['resolution']
					polymer_description = soup.find('macromolecule')['name']
					polymer_title = soup_res.find('pdb')['title']
					protein_inst = Protein(name,polymer_length,resolution,polymer_description,polymer_title)
					protein_inst_list.append(protein_inst)
					csvData_list = [[protein_inst.get_pdb_id(),protein_inst.get_polymer_length(), protein_inst.get_resolution(), protein_inst.get_polymer_description(), protein_inst.get_polymer_title()]]
					print(csvData_list)
					print("Saved PDB data: " + id_el)
					with open(CSV_FILE, 'a') as csvFile:
						writer = csv.writer(csvFile)
						writer.writerows(csvData_list)
					print("Saved CSV data: " + id_el)
					# csvFile.close()
					# this is overwriting data, I want to write data on top of existing data
					# I chanded 'w+' to 'a'. 'a' can create a file if the file did not exist, and can keep appending data
				else:
					with open(JSON_FILE, 'r') as f:
						c1.cache_diction = json.loads(f.read())
						del c1.cache_diction[unique_url]
						del c1.cache_diction[unique_url_for_resolution]

					with open(JSON_FILE, 'w') as cache_file:
						cache_json = json.dumps(c1.cache_diction)
						cache_file.write(cache_json)
					print('deleted_1: ' + id_el)

			else:
				
				with open(JSON_FILE, 'r') as f:
						c1.cache_diction = json.loads(f.read())
						del c1.cache_diction[unique_url]
						del c1.cache_diction[unique_url_for_resolution]

				with open(JSON_FILE, 'w') as cache_file:
					cache_json = json.dumps(c1.cache_diction)
					cache_file.write(cache_json)
				print('deleted_2: ' + id_el)

		except Exception as inst:
			print(inst)
			with open(JSON_FILE, 'r') as f:
						c1.cache_diction = json.loads(f.read())
						del c1.cache_diction[unique_url]
						del c1.cache_diction[unique_url_for_resolution]

			with open(JSON_FILE, 'w') as cache_file:
				cache_json = json.dumps(c1.cache_diction)
				cache_file.write(cache_json)
			print('deleted_3: ' + id_el)

	return protein_inst_list


# def Create_CSV_from_JSON(json_file):

# 	# inst_list = get_protein_with_short_peptide(num_of_protein_to_check,start_el_num,length_of_short_peptide,resolution_limit)
# 	# csvData_list_comp = [[el_inst.get_pdb_id(),el_inst.get_polymer_length(), el_inst.get_resolution(), el_inst.get_polymer_description(), el_inst.get_polymer_title()] for el_inst in inst_list]

# 	json_dic = ''
# 	with open(json_file, 'r') as f:
# 		json_dic = json.loads(f.read())
# 	print(type(json_dic), json_dic)	

# 	# with open(CSV_FILE, 'w+') as csvFile:
# 	#     writer = csv.writer(csvFile)
# 	#     writer.writerows(csvData_list_comp)
# 	# csvFile.close()

# 	# return protein_inst_list
# Create_CSV_from_JSON(JSON_FILE)


# read and load json file
# make a list with data
# csvFile creation with w+



