import json

with open("data/datos.json", "r") as f:
    datos = json.load(f)

print(datos)
print(datos["nombre"])