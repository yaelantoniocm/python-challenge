import os
import csv

election_cvs = os.path.join("..", "Resources", "election_data.vs")

# Read in the CSV file
with open(election_cvs, 'r') as csvfile:
    # Crea un lector CSV
    csv_reader = csv.reader(csvfile)
