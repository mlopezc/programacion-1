import csv

with open("data/datos.csv", newline="") as f:
    lector = csv.reader(f)

    for fila in lector:
        print(fila)