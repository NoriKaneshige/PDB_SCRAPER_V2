
class Protein():
	def __init__(self, pdb_id, polymer_length, resolution, polymer_description, polymer_title):
		self.pdb_id = pdb_id
		self.polymer_length = polymer_length
		self.polymer_resolution = resolution
		self.polymer_description = polymer_description
		self.polymer_title = polymer_title

	def get_pdb_id(self):
		return self.pdb_id

	def get_polymer_length(self):
		return self.polymer_length

	def get_resolution(self):
		return self.polymer_resolution

	def get_polymer_description(self):
		return self.polymer_description

	def get_polymer_title(self):
		return self.polymer_title
		
	def __str__(self):
		return "-------------------------------------------------------\nPDB_ID:{}\nLength of short peptide:{}\nResolution:{}\nDescription:{}\nTitle:{}".format(self.pdb_id,self.polymer_length,self.polymer_resolution,self.polymer_description,self.polymer_title)



