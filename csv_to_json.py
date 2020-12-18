import os
import csv
import json

csv.register_dialect('MyDialect', quotechar='"', skipinitialspace=True,
                     quoting=csv.QUOTE_NONE, lineterminator='\n', strict=True)


def csv_to_json(csvfile):
    data = []
    with open(csvfile, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='MyDialect')
        for row in csv_reader:
            data.append(row)
            datastring = json.dumps(data, indent=2)
        return datastring


def write_json(csvfile):
    datastring = csv_to_json(csvfile)
    filename = os.path.splitext(csvfile)[0]+".json"
    with open(filename, 'w') as dict_json:
        dict_json.writelines(datastring)
