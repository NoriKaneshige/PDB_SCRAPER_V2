import unittest
from class_pdb import Protein
from functions_pdb import get_human_pdb_protein_ids

print('\n\n--------------------------------------------------------------\nWarning: If data is not in cache, \nthis will take more than couple minutes to complete the testing!\nSorry for the inconvenience!\n--------------------------------------------------------------')

class TestProtein(unittest.TestCase):
# pdb_id, polymer_length, resolution, polymer_description, url=None
	def setUp(self):
		self.protein_ex = Protein('Z19A',125,2.5,'KRAS', 'www.pdb.com')

	def testProteinInst(self):
		self.assertEqual(self.protein_ex.pdb_id, 'Z19A')
		self.assertEqual(self.protein_ex.polymer_resolution, 2.5)
		self.assertEqual(self.protein_ex.polymer_length, 125)
		self.assertEqual(self.protein_ex.polymer_description, 'KRAS')
		self.assertEqual(self.protein_ex.url, 'www.pdb.com')


class TestProteinFunction(unittest.TestCase):

	def testGetHumanPDBProteinIDs(self):
		res = get_human_pdb_protein_ids()[0]
		self.assertEqual(res, '10GS')


if __name__ == "__main__":
	unittest.main(verbosity=2)
