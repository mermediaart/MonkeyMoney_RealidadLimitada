
import os
import json
import re

# Ruta donde están tus scripts de Unity (ajustar si es necesario)
SCRIPTS_DIR = "Assets/Scripts"

def analizar_scripts():
    resultado = []
    for root, _, files in os.walk(SCRIPTS_DIR):
        for archivo in files:
            if archivo.endswith(".cs"):
                path = os.path.join(root, archivo)
                with open(path, "r", encoding="utf-8") as f:
                    contenido = f.read()

                clase = re.findall(r'class\s+(\w+)', contenido)
                metodos = re.findall(r'(public|private|protected)?\s*(void|int|string|float|bool)\s+(\w+)\s*\(', contenido)
                variables_serializadas = re.findall(r'(\[SerializeField\])?\s*(public|private)?\s*(\w+)\s+(\w+);', contenido)

                resultado.append({
                    "archivo": archivo,
                    "clases": clase,
                    "metodos": [m[2] for m in metodos],
                    "variables": [v[3] for v in variables_serializadas]
                })

    return resultado

if __name__ == "__main__":
    contexto = {
        "scripts_unity": analizar_scripts()
    }
    print(json.dumps(contexto, indent=2))
