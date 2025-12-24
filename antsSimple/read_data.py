import csv

navaids_path = "./antsSimple/resources/navaids.csv"
navaids = []
with open(navaids_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for row in csvreader:
        navaids.append((row[2],(float(row[6]),float(row[7]))))


airports_path = "./antsSimple/resources/airports.csv"
airports = []
with open(airports_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for row in csvreader:
        airports.append((row[1],(float(row[4]),float(row[5]))))