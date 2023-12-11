import json
import os
# Lee el contenido del archivo JSON
ruta_completa = os.path.join(os.path.dirname(__file__), "data.json")
with open(ruta_completa, 'r') as archivo_json:
    datos_json = json.load(archivo_json)

# Modifica el valor que deseas cambiar
datos_json["ruta_pf"] = "cambio realizado"

# Guarda los cambios en el archivo JSON
with open(ruta_completa, 'w') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)