# You can scrape [PDB](https://www.rcsb.org/) with this program

## Simply run the file named as "run_this_file.py"
1) You will be asked about how many proteins you want to scrape, where to start scraping, length of co-crystalized peptide, and resolution limit.
2) There are over 40K proteins and this program uses a list of PDBIDs. This program goes through all PDBIDs and check data based on your criteria.
3) If data meet your criteria, the data will be saved in JSON file and CSV file.
4) If the program stops for some reasons such as communication failure caused by server etc, you can just run "run_this_file.py" again and input the starting number where the program stopped.
5) When the program is started again, data will be saved on top of existing data.
6) You can use JSON file and CSV file for further analysis depending on your interests. 